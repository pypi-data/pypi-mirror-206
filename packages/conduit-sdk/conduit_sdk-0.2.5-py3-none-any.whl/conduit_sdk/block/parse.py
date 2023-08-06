import json
from json import JSONDecodeError
from typing import Any, Mapping, Optional, cast
from urllib.parse import urlparse

from conduit_sdk.common.schema import AggregationType, ColumnKind, ColumnType, DataColumnSchema
from conduit_sdk.errors import ValidationError

from .schema import LocalizationSchema, QueryParams, RequestSchema


def parse_query_params(
    query_params: Mapping[str, Any],
    vault_required: bool = True,
) -> QueryParams:
    origin = cast(str, _get_query_param(query_params, 'origin'))
    vault_token = _get_query_param(query_params, 'vault_token', vault_required)
    vault_url = _get_query_param(query_params, 'vault_url', vault_required)
    payload = _get_payload(query_params)

    _validate_origin(origin)

    return QueryParams(
        origin=origin,
        vault_token=vault_token,
        vault_url=vault_url,
        payload=payload,
    )


def parse_request_schema(body: dict[str, Any]) -> RequestSchema:
    config = _get_body_field(body, 'config')
    columns = _parse_columns(_get_body_field(body, 'columns'))
    date_from = _get_body_field(body, 'date_from')
    date_to = _get_body_field(body, 'date_to')
    secrets = _get_body_field(body, 'secrets')
    timezone = _get_body_field(body, 'timezone')
    localization = _parse_localization(_get_body_field(body, 'localization'))

    return RequestSchema(
        config=config,
        columns=columns,
        date_from=date_from,
        date_to=date_to,
        secrets=secrets,
        timezone=timezone,
        localization=localization,
    )


def _get_field(fields: Mapping[str, Any], field_name: str, required: bool, err_template: str) -> Any:
    try:
        return fields[field_name]
    except KeyError:
        if required:
            raise ValidationError(err_template.format(field_name=field_name))

    return None


def _get_query_param(fields: Mapping[str, str], field_name: str, required: bool = True) -> Optional[str]:
    return _get_field(fields, field_name, required, err_template='Query parameter `{field_name}` is required')


def _get_body_field(fields: Mapping[str, Any], field_name: str) -> Any:
    return _get_field(fields, field_name, required=True, err_template='Field `{field_name}` is required')


def _get_column_field(fields: Mapping[str, str], field_name: str, col_number: int) -> str:
    err_template = f'Field `{{field_name}}` is required for column {col_number}'
    return _get_field(fields, field_name, required=True, err_template=err_template)


def _get_payload(params: Mapping[str, Any]) -> Optional[dict[str, Any]]:
    if payload := params.get('payload'):
        try:
            return json.loads(payload)
        except JSONDecodeError:
            raise ValidationError('Query parameter `payload` has bad format (must be JSON)')

    return None


def _validate_origin(origin: str) -> None:
    url = urlparse(origin)
    if (
        url.netloc.endswith('.getconduit.app')
        or url.netloc.endswith('.cndt.work')
        or url.netloc.startswith('localhost:')
    ):
        return

    raise ValidationError(f'Bad origin: {origin}')


def _parse_columns(columns: list[dict[str, Any]]) -> list[DataColumnSchema]:
    parsed_columns = []

    if not isinstance(columns, list):
        raise ValidationError('Columns field must be a list instance')

    for col_number, col in enumerate(columns, 1):
        if not isinstance(col, dict):
            raise ValidationError(f'Column {col_number} must be a dict instance')

        name = _get_column_field(col, 'name', col_number)
        type_key = _get_column_field(col, 'type', col_number)
        kind_key = _get_column_field(col, 'kind', col_number)
        agg_key = _get_column_field(col, 'agg', col_number)

        parsed_columns.append(
            DataColumnSchema(
                name=name,
                type=ColumnType[type_key],
                kind=ColumnKind[kind_key],
                agg=AggregationType[agg_key],
            ),
        )
    return parsed_columns


def _parse_localization(localization: dict[str, Any]) -> LocalizationSchema:
    if not isinstance(localization, dict):
        raise ValidationError('Localization field must be a dict instance')

    week_start = _get_body_field(localization, 'week_start')
    locale = _get_body_field(localization, 'locale')
    currency = _get_body_field(localization, 'currency')
    decimal_digits = _get_body_field(localization, 'decimal_digits')
    money_digits = _get_body_field(localization, 'money_digits')
    percent_digits = _get_body_field(localization, 'percent_digits')

    return LocalizationSchema(
        week_start=week_start,
        locale=locale,
        currency=currency,
        decimal_digits=decimal_digits,
        money_digits=money_digits,
        percent_digits=percent_digits,
    )
