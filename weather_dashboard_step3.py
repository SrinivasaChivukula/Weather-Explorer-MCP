import asyncio
import json
from colorama import init, Fore, Style
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Initialize colorama for Windows terminal color support
init(autoreset=True)

async def main():
    import sys
    import shutil
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding='utf-8')
    
    term_width = shutil.get_terminal_size().columns
    sep = "═" * min(term_width - 2, 60)
    
    # Premium Header with Gradient-like colors
    print(Fore.CYAN + Style.BRIGHT + "╔" + sep + "╗")
    print(Fore.CYAN + Style.BRIGHT + "║" + " LIVE WEATHER & CITY EXPLORER ".center(len(sep)) + "║")
    print(Fore.CYAN + Style.DIM + "╠" + sep + "╣")
    print(Fore.WHITE + "║" + f" User: {Fore.YELLOW}SSC0167 (Srinivasa Saidatta)".center(len(sep) + 10) + Fore.WHITE + "║")
    print(Fore.CYAN + Style.BRIGHT + "╚" + sep + "╝\n")
    
    # Interactive selection of city
    print(Fore.WHITE + Style.BRIGHT + "📍 Select a destination to explore:")
    print(f"  {Fore.CYAN}1. {Fore.WHITE}Denton, TX {Style.DIM}(The Horse Capital)")
    print(f"  {Fore.CYAN}2. {Fore.WHITE}New York, NY {Style.DIM}(The Big Apple)")
    print(f"  {Fore.CYAN}3. {Fore.WHITE}London, UK {Style.DIM}(The Foggy City)")
    print(f"  {Fore.CYAN}4. {Fore.WHITE}Tokyo, Japan {Style.DIM}(The Neon City)")
    print(f"  {Fore.CYAN}5. {Fore.WHITE}Custom Search {Style.DIM}(Search any city)")
    
    choice = input(f"\n{Fore.GREEN}❯ Enter choice (1-5): {Style.RESET_ALL}").strip()
    if not choice:
        choice = "1"
    
    # Mapping choices to coordinates and Wikipedia slugs
    locations = {
        "1": {"lat": 33.21, "lon": -97.13, "city": "Denton, TX", "wiki": "Denton,_Texas"},
        "2": {"lat": 40.71, "lon": -74.00, "city": "New York City", "wiki": "New_York_City"},
        "3": {"lat": 51.50, "lon": -0.12, "city": "London", "wiki": "London"},
        "4": {"lat": 35.68, "lon": 139.65, "city": "Tokyo", "wiki": "Tokyo"}
    }
    
    # Custom Search Logic
    if choice == "5":
        city_search = input(f"{Fore.GREEN}🔍 Search City: {Style.RESET_ALL}").strip()
        import requests
        print(f"{Fore.BLUE}🌐 Discovering {city_search}... ", end="", flush=True)
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_search}&count=1"
        try:
            geo_res = requests.get(geo_url, timeout=10).json()
            if not geo_res.get("results"):
                print(f"{Fore.RED}Failed!")
                print(f"{Fore.RED}City not found. Defaulting to Denton.")
                loc = locations["1"]
            else:
                res = geo_res["results"][0]
                loc = {
                    "lat": res["latitude"],
                    "lon": res["longitude"],
                    "city": f"{res['name']}, {res.get('country', '')}",
                    "wiki": res["name"].replace(" ", "_")
                }
                print(f"{Fore.GREEN}Found!")
        except:
            print(f"{Fore.RED}Error! Defaulting to Denton.")
            loc = locations["1"]
    else:
        loc = locations.get(choice, locations["1"])

    city_name = loc["city"]
    wiki_slug = loc["wiki"]

    # Modern User-Agent to avoid blocks
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

    server = StdioServerParameters(
        command="python",
        args=["-m", "mcp_server_fetch", "--ignore-robots-txt", "--user-agent", user_agent]
    )

    print(f"\n{Fore.MAGENTA}✨ Initializing MCP Engine for {Fore.WHITE}{city_name}...")
    
    try:
        async with stdio_client(server) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()

                # ---- Fetch Wikipedia summary ----
                print(f"{Fore.BLUE}🔍 Scanning Wikipedia archives... ", end="", flush=True)
                wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{wiki_slug}"
                wiki_res = await session.call_tool("fetch", {"url": wiki_url})
                print(f"{Fore.GREEN}Done!")
                
                if wiki_res.isError:
                    summary = "Unable to retrieve city overview via MCP."
                else:
                    wiki_data = json.loads(wiki_res.content[0].text)
                    summary = wiki_data.get("extract", "No summary available.")

                # ---- Fetch weather data ----
                print(f"{Fore.BLUE}🌤  Consulting meteorological satellites... ", end="", flush=True)
                weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={loc['lat']}&longitude={loc['lon']}&current_weather=true"
                weather_res = await session.call_tool("fetch", {"url": weather_url})
                print(f"{Fore.GREEN}Done!")

                if weather_res.isError:
                    current = {}
                else:
                    weather_data = json.loads(weather_res.content[0].text)
                    current = weather_data.get('current_weather', {})
                
                temp = current.get('temperature', 'N/A')
                wind = current.get('windspeed', 'N/A')

                # ---- Combined, nicely formatted output ----
                print(f"\n{Fore.CYAN}{Style.BRIGHT}╔" + sep + "╗")
                print(f"{Fore.CYAN}{Style.BRIGHT}║ {city_name.upper()} INTELLIGENCE REPORT".center(len(sep)) + "║")
                print(f"{Fore.CYAN}{Style.BRIGHT}╚" + sep + "╝")
                
                print(f"\n{Fore.YELLOW}📜 OVERVIEW")
                desc = (summary[:300] + "..." if len(summary) > 300 else summary)
                print(f"{Fore.WHITE}{desc}")
                
                print(f"\n{Fore.YELLOW}🌡  METRICS")
                # Temperature colour logic
                if isinstance(temp, (int, float)):
                    if temp > 25:
                        temp_color = Fore.RED
                    elif temp < 10:
                        temp_color = Fore.BLUE
                    else:
                        temp_color = Fore.GREEN
                else:
                    temp_color = Fore.WHITE
                print(f"  {Fore.WHITE}Temperature: {temp_color}{temp} °C")
                print(f"  {Fore.WHITE}Wind Speed:  {wind} km/h")
                
                # Activity recommendation
                print(f"\n{Fore.YELLOW}💡 INSIGHT")
                if isinstance(temp, (int, float)) and 15 <= temp <= 25 and wind < 20:
                    print(f"  {Fore.GREEN}★ Perfect weather for exploration and outdoor activities!")
                elif isinstance(temp, (int, float)) and temp > 25:
                    print(f"  {Fore.RED}★ High temperature warning. Stay hydrated and seek shade.")
                elif isinstance(temp, (int, float)) and temp < 10:
                    print(f"  {Fore.BLUE}★ Brisk conditions. A warm jacket is highly recommended.")
                else:
                    print(f"  {Fore.WHITE}★ Standard conditions. Dress appropriately for the day.")
                
                print(f"\n{Fore.CYAN}{Style.DIM}{sep}")
    except Exception as e:
        import requests
        print(f"\n{Fore.YELLOW}⚠️  MCP Engine unavailable {Style.DIM}({str(e)[:50]}...)")
        print(f"{Fore.MAGENTA}⚡ Switching to Direct Transmission Mode...")
        
        try:
            # Wikipedia fallback with proper User-Agent
            wiki_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{wiki_slug}"
            headers = {"User-Agent": user_agent}
            wiki_res = requests.get(wiki_url, headers=headers, timeout=10)
            wiki_res.raise_for_status()
            wiki_data = wiki_res.json()
            summary = wiki_data.get("extract", "No summary available.")
            
            # Weather fallback
            weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={loc['lat']}&longitude={loc['lon']}&current_weather=true"
            weather_res = requests.get(weather_url, timeout=10)
            weather_res.raise_for_status()
            weather_data = weather_res.json()
            current = weather_data.get('current_weather', {})
            temp = current.get('temperature', 'N/A')
            wind = current.get('windspeed', 'N/A')
            
            # Display Report with Fallback banner
            print(f"\n{Fore.CYAN}{Style.BRIGHT}╔" + sep + "╗")
            print(f"{Fore.CYAN}{Style.BRIGHT}║ {city_name.upper()} INTELLIGENCE REPORT (LITE)".center(len(sep)) + "║")
            print(f"{Fore.CYAN}{Style.BRIGHT}╚" + sep + "╝")
            
            print(f"\n{Fore.YELLOW}📜 OVERVIEW")
            desc = (summary[:300] + "..." if len(summary) > 300 else summary)
            print(f"{Fore.WHITE}{desc}")
            
            print(f"\n{Fore.YELLOW}🌡  METRICS")
            if isinstance(temp, (int, float)):
                temp_color = Fore.RED if temp > 25 else Fore.BLUE if temp < 10 else Fore.GREEN
            else:
                temp_color = Fore.WHITE
            print(f"  {Fore.WHITE}Temperature: {temp_color}{temp} °C")
            print(f"  {Fore.WHITE}Wind Speed:  {wind} km/h")
            
            print(f"\n{Fore.YELLOW}💡 INSIGHT")
            if isinstance(temp, (int, float)) and 15 <= temp <= 25 and wind < 20:
                print(f"  {Fore.GREEN}★ Perfect weather for exploration!")
            else:
                print(f"  {Fore.WHITE}★ Conditions are stable. Enjoy your visit.")
            
            print(f"\n{Fore.CYAN}{Style.DIM}{sep}")

        except Exception as e2:
            print(f"\n{Fore.RED}{Style.BRIGHT}❌ CRITICAL ERROR: Communication Link Severed")
            print(f"{Fore.RED}Details: {str(e2)}")

if __name__ == "__main__":
    asyncio.run(main())
