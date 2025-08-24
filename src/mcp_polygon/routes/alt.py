from mcp_polygon.polygonClient import polygon_client

from typing import Optional, Dict, Any, Union
from datetime import datetime, date
import json
from ..server import poly_mcp

__all__ = ["list_treasury_yields", "list_inflation"]

@poly_mcp.tool()
async def list_treasury_yields(
    date: Optional[Union[str, datetime, date]] = None,
    date_any_of: Optional[str] = None,
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
    Retrieve treasury yield data.
    """
    try:
        results = polygon_client.list_treasury_yields(
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
async def list_inflation(
    date: Optional[Union[str, datetime, date]] = None,
    date_any_of: Optional[str] = None,
    date_gt: Optional[Union[str, datetime, date]] = None,
    date_gte: Optional[Union[str, datetime, date]] = None,
    date_lt: Optional[Union[str, datetime, date]] = None,
    date_lte: Optional[Union[str, datetime, date]] = None,
    limit: Optional[int] = None,
    sort: Optional[str] = None,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get inflation data from the Federal Reserve.
    """
    try:
        results = polygon_client.list_inflation(
            date=date,
            date_any_of=date_any_of,
            date_gt=date_gt,
            date_gte=date_gte,
            date_lt=date_lt,
            date_lte=date_lte,
            limit=limit,
            sort=sort,
            params=params,
            raw=True,
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}

