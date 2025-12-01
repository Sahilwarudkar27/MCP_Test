from fastmcp import FastMCP
import random

mcp = FastMCP("Simple MCP Server")

@mcp.tool
def add_two_numbers(a: float, b: float):
    return {"a": a, "b": b, "result": a + b}

@mcp.tool
def random_number():
    return {"value": random.randint(1, 100)}

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)