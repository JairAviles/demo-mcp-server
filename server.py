"""
Implementation of a simple MCP server with calculator tools.
"""
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP(
    name="Demo",
    host="0.0.0.0",
    port=8050,
)

# Add an addition tool
@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts two numbers and returns the result."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers and returns the result."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divides two numbers and returns the result.

    Error:
        ValueError: If b is zero, a division by zero error is raised.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Run the server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")