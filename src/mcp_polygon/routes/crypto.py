
from typing import Optional, Dict, Any
from mcp_polygon.polygonClient import polygon_client
import json
from ..server import poly_mcp

__all__ = ["get_last_crypto_trade", "get_snapshot_crypto_book"]

@poly_mcp.tool()
async def get_last_crypto_trade(
    from_: str,
    to: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get the most recent trade for a crypto pair.
    """
    try:
        results = polygon_client.get_last_crypto_trade(
            from_=from_, to=to, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}
 



@poly_mcp.tool()
async def get_snapshot_crypto_book(
    ticker: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get snapshot for a crypto ticker's order book.
    """
    try:
        results = polygon_client.get_snapshot_crypto_book(
            ticker=ticker, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}


