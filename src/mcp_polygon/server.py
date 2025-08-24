import os
from mcp.server.fastmcp import FastMCP
import asyncio
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

load_dotenv()

poly_mcp = FastMCP(
    "Polygon", 
    dependencies=["polygon"], 
    host=os.environ.get("HOST", "0.0.0.0"), 
    port=int(os.environ.get("PORT", "8000")),
)

# Add health check endpoint for monitoring
@poly_mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    """Health check endpoint for deployment monitoring"""
    from starlette.responses import JSONResponse
    return JSONResponse({
        "status": "healthy", 
        "service": "polygon-mcp-server",
    })


def run_stdio():
    asyncio.run(poly_mcp.run_stdio_async())

def run_web():
    try:
        # Use FastMCP's built-in run method with SSE transport
        poly_mcp.run(transport="sse", host=os.environ.get("HOST", "0.0.0.0"), port=int(os.environ.get("PORT", "8000")))
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        raise
    # asyncio.run(poly_mcp.run_sse_async())