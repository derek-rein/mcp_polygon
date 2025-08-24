from mcp_polygon.polygonClient import polygon_client

from typing import Optional, Dict, Any, Union
from datetime import datetime, date
import json
from ..server import poly_mcp

@poly_mcp.tool()
async def get_option_chain_snapshot(
    underlying_asset: str,
    strike_price: Optional[float] = None,
    expiration_date: Optional[str] = None,
    contract_type: Optional[str] = None,
    order: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get a comprehensive snapshot of all options contracts for a specified underlying asset.
    """
    try:
        # Build params dict with the query parameters
        query_params = {}
        if strike_price is not None:
            query_params["strike_price"] = strike_price
        if expiration_date is not None:
            query_params["expiration_date"] = expiration_date
        if contract_type is not None:
            query_params["contract_type"] = contract_type
        if order is not None:
            query_params["order"] = order
        if limit is not None:
            query_params["limit"] = limit
        if sort is not None:
            query_params["sort"] = sort
        if params:
            query_params.update(params)

        results = polygon_client.list_snapshot_options_chain(
            underlying_asset=underlying_asset,
            params=query_params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_option_aggs(
    options_ticker: str,
    multiplier: int,
    timespan: str,
    from_: Union[str, int, datetime, date],
    to: Union[str, int, datetime, date],
    adjusted: Optional[bool] = None,
    sort: Optional[str] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get aggregated historical OHLC data for a specified options contract.
    """
    try:
        results = polygon_client.get_aggs(
            ticker=options_ticker,
            multiplier=multiplier,
            timespan=timespan,
            from_=from_,
            to=to,
            adjusted=adjusted,
            sort=sort,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_option_contract_overview(
    options_ticker: str,
    as_of: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get detailed information about a specific options contract.
    """
    try:
        # Build params dict with the query parameters
        query_params = {}
        if as_of is not None:
            query_params["as_of"] = as_of
        if params:
            query_params.update(params)

        results = polygon_client.get_options_contract(
            ticker=options_ticker,
            params=query_params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_option_contracts(
    underlying_ticker: Optional[str] = None,
    contract_type: Optional[str] = None,
    expiration_date: Optional[str] = None,
    as_of: Optional[str] = None,
    strike_price: Optional[float] = None,
    expired: Optional[bool] = None,
    order: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get a comprehensive index of options contracts with filtering capabilities.
    """
    try:
        # Build params dict with the query parameters
        query_params = {}
        if underlying_ticker is not None:
            query_params["underlying_ticker"] = underlying_ticker
        if contract_type is not None:
            query_params["contract_type"] = contract_type
        if expiration_date is not None:
            query_params["expiration_date"] = expiration_date
        if as_of is not None:
            query_params["as_of"] = as_of
        if strike_price is not None:
            query_params["strike_price"] = strike_price
        if expired is not None:
            query_params["expired"] = expired
        if order is not None:
            query_params["order"] = order
        if limit is not None:
            query_params["limit"] = limit
        if sort is not None:
            query_params["sort"] = sort
        if params:
            query_params.update(params)

        results = polygon_client.list_options_contracts(
            params=query_params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def get_option_contract_snapshot(
    underlying_asset: str,
    option_contract: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get a comprehensive snapshot of a specified options contract.
    """
    try:
        results = polygon_client.get_snapshot_option(
            underlying_asset=underlying_asset,
            option_contract=option_contract,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}

@poly_mcp.tool()
async def get_snapshot_option(
    underlying_asset: str,
    option_contract: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get snapshot for a specific option contract.
    """
    try:
        results = polygon_client.get_snapshot_option(
            underlying_asset=underlying_asset,
            option_contract=option_contract,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}
