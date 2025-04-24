### mcp.json config

## 怎么获取MCP服务

[smithery](https://smithery.ai)

```
{
  "mcpServers": {
    "toolbox": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@smithery/toolbox",
        "--config",
        "{\"dynamic\":false,\"smitheryApiKey\":\"1e09e677-f537-43b3-bf2f-cb71442c7e40\"}"
      ]
    },
    "server-sequential-thinking": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@smithery-ai/server-sequential-thinking",
        "--key",
        "1e09e677-f537-43b3-bf2f-cb71442c7e40"
      ]
    },
    "fetch": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@smithery-ai/fetch",
        "--key",
        "1e09e677-f537-43b3-bf2f-cb71442c7e40"
      ]
    },
    "files": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/Yotoha/Desktop/"
      ]
    },
    "mcp-server-hotnews": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@wopal/mcp-server-hotnews",
        "--key",
        "1e09e677-f537-43b3-bf2f-cb71442c7e40"
      ]
    },
    "playwright-mcp": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@microsoft/playwright-mcp",
        "--key",
        "1e09e677-f537-43b3-bf2f-cb71442c7e40"
      ]
    },
    "hn-server": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@pskill9/hn-server"
      ]
    },
    "duckduckgo-mcp-server": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@smithery/cli@latest",
        "run",
        "@nickclyde/duckduckgo-mcp-server"
      ]
    }
  }
}
```
