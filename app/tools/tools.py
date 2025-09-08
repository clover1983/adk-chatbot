from datetime import datetime
import pytz

from app import env_import

from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams, StdioConnectionParams
# from mcp import StdioServerParameters


def get_current_date(tz: str) -> dict:
    """
    Get the current date in the format YYYY-MM-DD
    """
    tzinfo = pytz.timezone(tz)
    return {"current_date": datetime.now(tzinfo).strftime("%Y-%m-%d")}


mcp = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="http://localhost:5001/mcp",
    ),
    # Read only tools
    # tool_filter=[
    #     "xxx",
    # ],
)