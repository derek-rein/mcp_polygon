from mcp_polygon.polygonClient import polygon_client
from typing import Optional, Dict, Any, Union
from datetime import datetime, date
import json
from ..server import poly_mcp


@poly_mcp.tool()
async def list_stock_financials(
    ticker: Optional[str] = None,
    cik: Optional[str] = None,
    company_name: Optional[str] = None,
    company_name_search: Optional[str] = None,
    sic: Optional[str] = None,
    filing_date: Optional[Union[str, datetime, date]] = None,
    filing_date_lt: Optional[Union[str, datetime, date]] = None,
    filing_date_lte: Optional[Union[str, datetime, date]] = None,
    filing_date_gt: Optional[Union[str, datetime, date]] = None,
    filing_date_gte: Optional[Union[str, datetime, date]] = None,
    period_of_report_date: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_lt: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_lte: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_gt: Optional[Union[str, datetime, date]] = None,
    period_of_report_date_gte: Optional[Union[str, datetime, date]] = None,
    timeframe: Optional[str] = None,
    include_sources: Optional[bool] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get fundamental financial data for companies.
    """
    try:
        results = polygon_client.vx.list_stock_financials(
            ticker=ticker,
            cik=cik,
            company_name=company_name,
            company_name_search=company_name_search,
            sic=sic,
            filing_date=filing_date,
            filing_date_lt=filing_date_lt,
            filing_date_lte=filing_date_lte,
            filing_date_gt=filing_date_gt,
            filing_date_gte=filing_date_gte,
            period_of_report_date=period_of_report_date,
            period_of_report_date_lt=period_of_report_date_lt,
            period_of_report_date_lte=period_of_report_date_lte,
            period_of_report_date_gt=period_of_report_date_gt,
            period_of_report_date_gte=period_of_report_date_gte,
            timeframe=timeframe,
            include_sources=include_sources,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_ipos(
    ticker: Optional[str] = None,
    listing_date: Optional[Union[str, datetime, date]] = None,
    listing_date_lt: Optional[Union[str, datetime, date]] = None,
    listing_date_lte: Optional[Union[str, datetime, date]] = None,
    listing_date_gt: Optional[Union[str, datetime, date]] = None,
    listing_date_gte: Optional[Union[str, datetime, date]] = None,
    ipo_status: Optional[str] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retrieve upcoming or historical IPOs.
    """
    try:
        results = polygon_client.vx.list_ipos(
            ticker=ticker,
            listing_date=listing_date,
            listing_date_lt=listing_date_lt,
            listing_date_lte=listing_date_lte,
            listing_date_gt=listing_date_gt,
            listing_date_gte=listing_date_gte,
            ipo_status=ipo_status,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_short_interest(
    ticker: Optional[str] = None,
    settlement_date: Optional[Union[str, datetime, date]] = None,
    settlement_date_lt: Optional[Union[str, datetime, date]] = None,
    settlement_date_lte: Optional[Union[str, datetime, date]] = None,
    settlement_date_gt: Optional[Union[str, datetime, date]] = None,
    settlement_date_gte: Optional[Union[str, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retrieve short interest data for stocks.
    """
    try:
        results = polygon_client.list_short_interest(
            ticker=ticker,
            settlement_date=settlement_date,
            settlement_date_lt=settlement_date_lt,
            settlement_date_lte=settlement_date_lte,
            settlement_date_gt=settlement_date_gt,
            settlement_date_gte=settlement_date_gte,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_short_volume(
    ticker: Optional[str] = None,
    date: Optional[Union[str, datetime, date]] = None,
    date_lt: Optional[Union[str, datetime, date]] = None,
    date_lte: Optional[Union[str, datetime, date]] = None,
    date_gt: Optional[Union[str, datetime, date]] = None,
    date_gte: Optional[Union[str, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    order: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Retrieve short volume data for stocks.
    """
    try:
        results = polygon_client.list_short_volume(
            ticker=ticker,
            date=date,
            date_lt=date_lt,
            date_lte=date_lte,
            date_gt=date_gt,
            date_gte=date_gte,
            limit=limit,
            sort=sort,
            order=order,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_splits(
    ticker: Optional[str] = None,
    execution_date: Optional[Union[str, datetime, date]] = None,
    reverse_split: Optional[bool] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get historical stock splits.
    """
    try:
        results = polygon_client.list_splits(
            ticker=ticker,
            execution_date=execution_date,
            reverse_split=reverse_split,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


@poly_mcp.tool()
async def list_dividends(
    ticker: Optional[str] = None,
    ex_dividend_date: Optional[Union[str, datetime, date]] = None,
    frequency: Optional[int] = None,
    dividend_type: Optional[str] = None,
    limit: Optional[int] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get historical cash dividends.
    """
    try:
        results = polygon_client.list_dividends(
            ticker=ticker,
            ex_dividend_date=ex_dividend_date,
            frequency=frequency,
            dividend_type=dividend_type,
            limit=limit,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}

