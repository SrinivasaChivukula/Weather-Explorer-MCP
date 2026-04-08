# Weather & City Explorer 🌍

Hey there! 👋 This is a project I've been working on to explore how we can bridge the gap between AI assistants and the live, breathing web. It's a Python-based intelligence tool that doesn't just rely on static training data—it actually goes out and "grabs" the world as it's happening.

## 🧐 So, what's this all about?
I wanted to build something that felt more like a "digital investigator" than just a simple weather app. This tool hits multiple data streams at once:
- **Wikipedia:** For the history and "vibe" of a city.
- **Open-Meteo:** For the raw, real-time meteorological data.

It's all wrapped in a premium CLI that looks awesome in the terminal (I'm a big fan of ASCII headers and clean, color-coded metrics).

---

## 🛠 The Tech Under the Hood
Don't let the casual look fool you—there's some serious engineering going on here:

- **Model Context Protocol (MCP):** This is the star of the show. I'm using an MCP server (`@modelcontextprotocol/server-fetch`) to let the app interact with external tools in a structured way. It basically gives the AI a set of "hands" to reach out and touch the internet.
- **Asyncio:** Everything is asynchronous. Why? Because waiting for network I/O is a waste of time. I used Python's `asyncio` to ensure the UI stays snappy while data is being fetched in the background.
- **Iterative Prompting:** I didn't just write this in one go. I used an iterative process with Google Antigravity, refining the logic, the error handling, and the UI over multiple rounds until it felt just right.
- **Resilient Engineering:** Life happens. Servers go down. Internet clips. I built in a "Direct Transmission Mode" fallback that bypasses the MCP engine and hits the REST APIs directly using `requests` if things go sideways.

---

## 🚀 Lessons Learned (and Skills I Gained)
- **Living Web Interaction:** Moving past standard API calls into the world of MCP felt like a level-up. It's a much more flexible way to connect tools.
- **Prompt Engineering as an Art:** I learned that being precise with my goals (like asking for specific ASCII table alignments or custom fallback logic) gets way better results than just saying "make it better."
- **Failure is a Feature:** Implementing graceful degradation (the Lite/Direct mode) taught me how to build software that doesn't just crash when the world isn't perfect.

---

## 🎰 What's Next?
I've got a few ideas to take this further:
- **Map Visualizations:** I'd love to generate static maps directly in the terminal.
- **More Layers:** Bringing in exchange rates and local news feeds to turn this into a full-scale "Travel Intelligence Report."
- **GUI Upgrade:** Maybe a sleek Streamlit dashboard for a more visual experience.

---

## 🛠 Prerequisites & Dependencies
To get this engine running on your machine, you'll need the following:

### Software
- **Python 3.10+**: The core language.
- **Node.js**: Required to run the MCP Fetch server via `npx`.

### Libraries (Python)
You can install all requirements using:
```bash
pip install mcp colorama requests
```
*Wait, what are these?*
- `mcp`: The official Python SDK for interacting with Model Context Protocol servers.
- `colorama`: For all those flashy terminal colors.
- `requests`: Used for the Direct Transmission fallback mode.

---

## 🚀 How to Run
Ready to explore? Follow these steps:

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/SrinivasaChivukula/Weather-Explorer-MCP.git
   cd Weather-Explorer-MCP
   ```
2. **Setup Dependencies:**
   ```bash
   pip install mcp colorama requests
   ```
3. **Ignition:**
   ```bash
   python main.py
   ```
   *Note: On your first run, it might take a second to initialize the MCP server via npx.*

---

## 📂 Project Structure
I've revamped the file structure to keep things clean and professional:
- `main.py`: The primary application entry point (formerly `weather_dashboard_step3.py`).
- `archive/`: Contains earlier iterations of the dashboard logic.
- `tests/`: Specialized scripts for verifying network stability and MCP connectivity.
- `README.md`: You are here!

---

## 👨‍💻 About Me
**Srinivasa Chivukula**  
I'm a **Computer Science major** with my head in the clouds—literally. I'm concentrating on **AIML, CyberSecurity, and Cloud Technologies**, and I love building tools that solve real problems with modern tech stacks.

---
Built with 🐍 and ☕. All data is sourced from public archives (Wikipedia, Open-Meteo).
