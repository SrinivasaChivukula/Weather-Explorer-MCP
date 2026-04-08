import asyncio
import json
from colorama import init, Fore, Style
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Initialize colorama for Windows terminal color support
init(autoreset=True)

async def main():
    import sys
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding='utf-8')
    # 1. Print the required header with formatting
    print(Fore.CYAN + Style.BRIGHT + "==========================================")
    print(Fore.WHITE + "🌍 Live Weather Dashboard V2")
    print(Fore.YELLOW + "Submitted by: Srinivasa Saidatta Chivukula")
    print(Fore.YELLOW + "EUID: ssc0167")
    print(Fore.CYAN + Style.BRIGHT + "==========================================\n")
    
    # Meaningful Revision: Interactive City Selection
    print("Which city would you like to check?")
    print("  1. Denton, TX")
    print("  2. New York, NY")
    print("  3. London, UK")
    choice = input(Fore.GREEN + "Enter 1, 2, or 3 (default 1): " + Fore.WHITE).strip()
    
    # Set coordinates based on user input
    if choice == "2":
        lat, lon, city = 40.71, -74.00, "New York, NY"
    elif choice == "3":
        lat, lon, city = 51.50, -0.12, "London, UK"
    else:
        lat, lon, city = 33.21, -97.13, "Denton, TX"

    # Fix: Instead of npx, we invoke the python-native fetch server!
    server = StdioServerParameters(
        command="mcp-server-fetch",
        args=[]
    )

    print(Fore.MAGENTA + f"\n[System] Launching Fetch MCP Server targeting {city}...")
    
    # Meaningful Revision: Robust Error Handling
    try:
        async with stdio_client(server) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
                print(Fore.BLUE + f"[Fetch] Retrieving live data from Open-Meteo via MCP...\n")
                
                # Fetch MCP tool call
                result = await session.call_tool("fetch", {"url": url})
                raw_text = result.content[0].text
                
                # Parse JSON
                weather_data = json.loads(raw_text)
                current = weather_data.get('current_weather', {})
                temp = current.get('temperature', 'N/A')
                wind = current.get('windspeed', 'N/A')
                time_val = current.get('time', 'N/A')
                
                # Display output with dynamic color coding based on temp
                print(Fore.CYAN + Style.BRIGHT + f"--- Current Weather in {city} ---")
                print(Fore.WHITE + f"Reading Time: {time_val}")
                
                # Temperature logic for colors
                if isinstance(temp, (int, float)) and temp > 25:
                    temp_color = Fore.RED       # Hot!
                elif isinstance(temp, (int, float)) and temp < 10:
                    temp_color = Fore.BLUE      # Cold!
                else:
                    temp_color = Fore.YELLOW    # Mild
                    
                print(f"Temperature:  {temp_color}{temp} °C")
                print(Fore.WHITE + f"Wind Speed:   {wind} km/h")
                print(Fore.CYAN + Style.BRIGHT + "--------------------------------------")

    except Exception as e:
        # Graceful degradation if something goes wrong
        print(Fore.RED + Style.BRIGHT + "\n[Error] The dashboard encountered a problem!")
        print(Fore.RED + f"Details: {str(e)}")
        print(Fore.RED + "Please ensure you installed the MCP tool correctly: 'pip install mcp-server-fetch'")

if __name__ == "__main__":
    asyncio.run(main())
