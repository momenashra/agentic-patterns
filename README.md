
# 🧠 Multi-Agent Framework with CrewAI

This project demonstrates a multi-agent system using [CrewAI](https://github.com/joaomdmoura/crewai), AgentOps, Tavily, and ScrapeGraph for autonomous web tasks and data extraction.

## 📦 Requirements

Ensure the following dependencies are installed:

```bash
pip install -qU crewai[tools,agentops]
pip install -qU tavily-python scrapegraph-py
```

## 🔐 API Keys Setup

Register for API keys and set them using `userdata` (e.g., in Google Colab):

```python
os.environ["COHERE_API_KEY"] = userdata.get('cohere-colab')
os.environ["AGENTOPS_API_KEY"] = userdata.get('agentops-colab')
```

You can get your AgentOps key here: [AgentOps Setup](https://app.agentops.ai/get-started)

## 🚀 Initialize AgentOps

```python
import agentops

agentops.init(
    api_key=userdata.get('agentops-colab'),
    skip_auto_end_session=True,
    default_tags=['crewai']
)
```

## 🧰 Framework Components

- **LLM Integration** with Cohere
- **Search Agents** powered by Tavily
- **Scraping Tools** via ScrapeGraph
- **Custom Tools** defined with `@tool` decorators
- **Knowledge Sources** using in-memory strings

## 📁 Output

Outputs are stored in:

```python
output_dir = "./ai-agent-output"
os.makedirs(output_dir, exist_ok=True)
```

## 🛠️ Define Tools

```python
@tool
def write_to_json(data: dict, filename: str) -> str:
    path = os.path.join(output_dir, filename)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    return f"Written to {path}"
```

## 👥 Create Agents

Agents include:

- `SearchAgent`: Queries using Tavily
- `ScraperAgent`: Extracts structured data from pages
- `WriterAgent`: Converts findings into structured output

```python
search_agent = Agent(role="Searcher", ...)
scraper_agent = Agent(role="Scraper", ...)
writer_agent = Agent(role="Writer", ...)
```

## 🧩 Define Tasks

Each agent has associated tasks:

```python
search_task = Task(description="Search for top Python frameworks", agent=search_agent, ...)
scrape_task = Task(description="Scrape details from URLs", agent=scraper_agent, ...)
write_task = Task(description="Write JSON summary", agent=writer_agent, ...)
```

## 🧠 Crew Execution

```python
crew = Crew(
    agents=[search_agent, scraper_agent, writer_agent],
    tasks=[search_task, scrape_task, write_task],
    process=Process.sequential
)
result = crew.kickoff()
print(result)
```

## 🧪 Bash (Colab or Local)

```bash
python3 --version
mkdir -p ai-agent-output
```

## 📄 Notes

- Ensure your API keys are set securely
- You can modify tasks to target different search queries or output formats
- Ideal for autonomous agents and LLM task chaining demos
