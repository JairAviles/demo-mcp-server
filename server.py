from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(
    name="Demo",
    host="0.0.0.0",
    port=8050,
)

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool(description="A simple echo tool")
def echo(message: str) -> str:
    return f"Echo: {message}"

# Run the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")