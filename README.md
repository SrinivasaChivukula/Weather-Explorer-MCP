# Weather & City Explorer 🌍

## Overview
The **Weather & City Explorer** is a high-performance Python application designed to provide instantaneous intelligence reports for cities worldwide. By leveraging the **Model Context Protocol (MCP)**, the application fetches live data from multi-source streams, including **Wikipedia** for historical and cultural context and **Open-Meteo** for real-time meteorological conditions.

The project demonstrates the synergy between modern AI architectural patterns and traditional software engineering, featuring a robust, interactive CLI and a sophisticated error-handling system with redundant communication modes.

---

## 🚀 Key Features
- **Real-Time Data Streaming:** Uses the `fetch` MCP server to retrieve live, non-stale data directly from the web.
- **Dynamic City Intelligence:** Provides interactive selection and custom search functionality using geocoding APIs.
- **Intelligent Insight Engine:** Analyzes weather metrics (temperature, wind speed) to provide situational recommendations.
- **Fault-Tolerant Architecture:** Includes a "Direct Transmission Mode" fallback that switches to standard REST API calls if the MCP engine is compromised.
- **Premium User Experience:** A meticulously styled terminal interface using `colorama`, featuring ASCII banners and dynamic color-coded metrics.

---

## 🛠 Skills & Expertise Gained
Through the development of this project, I have significantly expanded my technical repertoire in several key domains:

- **Model Context Protocol (MCP):** Mastered the integration of MCP servers to extend AI/Application logic into the live web, moving beyond static knowledge bases.
- **Iterative Prompt Engineering:** Refined complex code structures through multiple rounds of iterative prompting, learning how to guide AI toward high-fidelity architectural goals.
- **Asynchronous Architecture:** Implemented Python's `asyncio` for non-blocking I/O operations, ensuring a smooth and responsive user experience.
- **API & Data Ecosystems:** Deepened understanding of RESTful API consumption, JSON schema parsing, and geocoding services.
- **Software Resilience:** Developed robust error-handling patterns, including graceful degradation and multi-layer fallback systems.

---

## 🎯 Efficiency & Performance Goals
- **Modular Codebase:** Achieved a high degree of modularity, allowing for easy expansion of data sources.
- **Optimized Latency:** Streamlined fetching operations to reduce the overhead of multi-source data retrieval.
- **User-Centric Design:** Focused on a zero-learning-curve interface that provides high-density information in an easily digestible format.

---

## 🔮 Future Roadmap
- **Expanded Information Layers:** Integrate financial data (exchange rates) and local news feeds.
- **Geographic Visualizations:** Implement static map generation in the terminal or export to HTML maps.
- **Advanced MCP Integration:** Utilize specialized MCP servers for secure localized file storage of weather history.
- **GUI Evolution:** Transition from a CLI to a modern dashboard using frameworks like Streamlit or PyQt.

---

## 👨‍💻 Author
**Srinivasa Chivukula**  
*Computer Science Major*  
*Concentrations: AI/ML, CyberSecurity, and Cloud Technologies*

---

## 📄 License
This project is for educational purposes. All data is sourced from public APIs (Wikipedia, Open-Meteo).
