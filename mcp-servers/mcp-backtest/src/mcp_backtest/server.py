"""MCP Backtest Server"""

from fastmcp import FastMCP

mcp = FastMCP(name="mcp-backtest")

@mcp.tool
def ping() -> dict[str, str]:
    """Health check tool. Returns a status dict to verify the MCP server is reachable."""
    return {"status": "ok", "server": mcp.name}


def main() -> None: 
    mcp.run()


if __name__ == "__main__":
    main()