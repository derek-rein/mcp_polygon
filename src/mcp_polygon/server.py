import os
from mcp.server.fastmcp import FastMCP
import asyncio
from dotenv import load_dotenv
import logging

from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings

logger = logging.getLogger(__name__)
load_dotenv()


class BearerAuthenticator(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        logger.info(f"Verifying token: {token}")
        if token == os.environ.get("MCP_TOKEN"):
            # You must return token, client_id, scopes
            # You can optionally set an expiration timestamp and resource string
            return AccessToken(
                token=token,
                client_id="mcppolygon",
                scopes=["authenticated"],
            )
        return None


# Note: A stub config means that some /.well-known/ endpoints will be
# missconfigured
auth_settings = AuthSettings(
    issuer_url="https://mcppolygon-production.up.railway.app/",  # stub

    # Bug: resource_server_url should be None if the MCP has tools
    # somebody forgot to add a default value  in the field(...) function (:
    resource_server_url=None,
)

poly_mcp = FastMCP(
    "Polygon", 
    instructions="This server provides stock and option data from Polygon.io",
    dependencies=["polygon"], 
    host=os.environ.get("HOST", "0.0.0.0"), 
    port=int(os.environ.get("PORT", "8000")),
    # Token verifier for authentication
    token_verifier=BearerAuthenticator(),
    # Auth settings for RFC 9728 Protected Resource Metadata
    auth=auth_settings,
    stateless_http=True
)



def run():
    transport = os.environ.get("MCP_TRANSPORT", "streamable-http").lower()

    if transport == "sse":
        asyncio.run(poly_mcp.run_sse_async('/sse'))
    elif transport == "streamable-http":
        asyncio.run(poly_mcp.run_streamable_http_async())
    elif transport == "stdio":
        asyncio.run(poly_mcp.run_stdio_async())
    else:
        logger.error(f"Unknown MCP_TRANSPORT value: {transport}. Must be 'sse', 'streamable-http', or 'both'.")
        raise ValueError(f"Unknown MCP_TRANSPORT value: {transport}")