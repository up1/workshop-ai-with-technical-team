from fastmcp import Client
import asyncio

client = Client("demo_server.py")

async def call_tool():
    async with client:
        result = await client.call_tool("get_weather", {"latitude": 13.7563, "longitude": 100.5018})
        print(result)

asyncio.run(call_tool())