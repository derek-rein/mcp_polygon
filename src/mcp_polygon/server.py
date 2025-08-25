import os
from mcp.server.fastmcp import FastMCP
import asyncio
from dotenv import load_dotenv
import logging
from datetime import datetime, timedelta
from pydantic import AnyHttpUrl

from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings

logger = logging.getLogger(__name__)

load_dotenv()

class SimpleTokenVerifier(TokenVerifier):
    """Simple token verifier for demonstration."""

    async def verify_token(self, token: str) -> AccessToken | None:
        if token == os.environ.get("MCP_TOKEN"):
            return True
        return False


poly_mcp = FastMCP(
    "Polygon", 
    dependencies=["polygon"], 
    host=os.environ.get("HOST", "0.0.0.0"), 
    port=int(os.environ.get("PORT", "8000")),
    # Token verifier for authentication
    token_verifier=SimpleTokenVerifier(),
    # Auth settings for RFC 9728 Protected Resource Metadata
    # auth=AuthSettings(
    #     issuer_url=AnyHttpUrl("https://auth.example.com"),  # Authorization Server URL
    #     resource_server_url=AnyHttpUrl("http://localhost:3001"),  # This server's URL
    #     required_scopes=["user"],
    # ),
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
    transport = os.environ.get("MCP_TRANSPORT", "streamable-http").lower()

    if transport == "sse":
        asyncio.run(poly_mcp.run_sse_async('/sse'))
    elif transport == "streamable-http":
        asyncio.run(poly_mcp.run_streamable_http_async())
    else:
        logger.error(f"Unknown MCP_TRANSPORT value: {transport}. Must be 'sse', 'streamable-http', or 'both'.")
        raise ValueError(f"Unknown MCP_TRANSPORT value: {transport}")