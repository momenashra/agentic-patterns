# 🕸️ Autonomous Multi-Agent Web Scraping Framework

This project demonstrates an **autonomous multi-agent system** that performs complex web data collection and reporting with minimal human intervention. It blends **task-driven workflow** with **code-level setup instructions**, making it easy to understand **what** the system does and **how** to run it.

---

## 🎯 Task Overview

1. **Search Phase**  
   - A **Search Agent** queries target websites (e.g., Amazon.eg, Jumia, Noon) for products matching specific criteria (e.g., waterproof crossbody bags under 500 EGP).  
   - Parallel search queries ensure broad coverage.

2. **Scraping Phase**  
   - A **Scraper Agent** visits each URL, extracting structured details: title, price, image URL, specifications.  
   - Filters out incomplete or irrelevant entries.

3. **Aggregation Phase**  
   - An **Aggregator Agent** compiles cleaned data into a uniform JSON format, ready for downstream analysis.

4. **Reporting Phase**  
   - A **Writer Agent** generates a **summary report** (HTML, Markdown, PDF) with price comparisons, key findings, and top recommendations.

---

## 🔄 Workflow

1. **Define Agents & Tasks**  
   - Roles: Searcher, Scraper, Aggregator, Reporter.  
   - Task definitions specify inputs, outputs, and order.

2. **Initialize Crew**  
   - Use CrewAI to assemble agents and tasks into a pipeline.  
   - Choose **sequential** or **parallel** execution.

3. **Execute Pipeline**  
   - Run the crew: data flows automatically from search to report generation.

4. **Review Outputs**  
   - Check `/output` for:
     - **JSON** with top 10 products and specifications
     - **HTML/Markdown report** highlighting procurement insights

---

## 🔧 Prerequisites

- Python 3.10–3.12  
- API keys for required services (e.g., Cohere, AgentOps)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/auto-web-scraper.git
cd auto-web-scraper

# Install dependencies
pip install -qU crewai[tools,agentops]
pip install -qU tavily-python scrapegraph-py
```

---

## 🚀 Usage

1. **Set API Keys**  
   ```bash
   export COHERE_API_KEY="your-cohere-key"
   export AGENTOPS_API_KEY="your-agentops-key"
   ```

2. **Run the Pipeline**  
   ```bash
   python run_pipeline.py
   ```

3. **View Results**  
   ```bash
   ls output/
   cat output/report.md
   ```

---

## 🗂️ Project Structure

```
├── run_pipeline.py      # Script to launch the multi-agent crew
├── tasks.py             # Definitions of agents and tasks
├── tools.py             # Custom tool implementations (e.g., write_to_json)
├── output/              # Generated JSON and reports
├── README.md            # This file
└── requirements.txt     # Pinned dependencies
```

---

## 🌟 Key Benefits

- **Scalable**: Easily add or replace agents/tasks  
- **Modular**: Swap search/scrape strategies per agent  
- **Reproducible**: Version-controlled configs and requirements

---

## 📖 References

- [CrewAI](https://github.com/joaomdmoura/crewai)  
- [AgentOps Documentation](https://app.agentops.ai/docs)  
- [Tavily Python](https://pypi.org/project/tavily-python/)  
- [ScrapeGraph Py](https://pypi.org/project/scrapegraph-py/)  

---

## 📜 License

MIT License. See `LICENSE` file for details.
