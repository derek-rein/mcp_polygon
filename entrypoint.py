#!/usr/bin/env python
import os

from src.mcp_polygon.server import run_web
from dotenv import load_dotenv

load_dotenv()


# Ensure the server process doesn't exit immediately when run as an MCP server
def start_server():
    polygon_api_key = os.environ.get("POLYGON_API_KEY", "")

    if not polygon_api_key:
        print("Warning: POLYGON_API_KEY environment variable not set.")
    else:
        print("Starting Polygon MCP server with API key configured.")

    run_web()


if __name__ == "__main__":
    start_server()