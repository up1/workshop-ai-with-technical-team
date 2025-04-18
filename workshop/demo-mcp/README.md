# Workshop with [MCP (Model Context Protocol)](https://modelcontextprotocol.io/)
* [FastMCP](https://gofastmcp.com/)

## 1. Install
```
$pip install -r requirements.txt

$fastmcp version
```

## 2. Run MCP server
```
$python demo_server.py

or

$fastmcp run demo_server.py:mcp
```

## 3. Run client
```
$python demo_client.py
```

## 4. Run with MCP client + LLM
* [mcphost](https://github.com/mark3labs/mcphost)

```
$export OPENAI_API_KEY="your api key"
$mcphost -m openai:gpt-4 --config mcp.json
```

Example Inputs
* weather in Thailand
* อากาศของไทยกรุงเทพ