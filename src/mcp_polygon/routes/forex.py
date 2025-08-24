from mcp_polygon.polygonClient import polygon_client

from typing import Optional, Dict, Any
import json
from ..server import poly_mcp

@poly_mcp.tool()
async def get_last_forex_quote(
    from_: str,
    to: str,
    params: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """
    Get the most recent forex quote.
    """
    try:
        results = polygon_client.get_last_forex_quote(
            from_=from_, to=to, params=params, raw=True
        )

        data_str = results.data.decode("utf-8")
        return json.loads(data_str)
    except Exception as e:
        return {"error": str(e)}

