class MCPContext:
    def __init__(self):
        self.shared_context = {}
    
    def update(self, key: str, value: str):
        self.shared_context[key] = value
        print(f"✅ MCP updated: {key}")
    
    def get(self, key: str):
        return self.shared_context.get(key, "No context yet")

mcp = MCPContext()
