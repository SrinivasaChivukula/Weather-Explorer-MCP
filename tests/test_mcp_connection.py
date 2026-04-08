import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server = StdioServerParameters(
        command="mcp-server-fetch",
        args=[]
    )
    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("Successfully initialized python mcp-server-fetch!")
            
            url = "https://api.open-meteo.com/v1/forecast?latitude=33.21&longitude=-97.13&current_weather=true"
            result = await session.call_tool("fetch", {"url": url})
            print(result.content[0].text[:100])

if __name__ == "__main__":
    asyncio.run(main())
