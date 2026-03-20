# Multi-Agent Market Analyst with MCP Context Sharing

A production-ready multi-agent system built with CrewAI that demonstrates advanced agent orchestration using Model Context Protocol (MCP) for shared memory. This system coordinates three specialized AI agents to research, analyze, and generate comprehensive market reports.

## Overview

This project showcases a hierarchical multi-agent architecture where agents collaborate through a shared context system (MCP) to produce professional market analysis reports. The system is designed for scalability and can be deployed as a standalone script, REST API, or containerized service.

### Key Features

- **Multi-Agent Collaboration**: Three specialized agents (Researcher, Analyst, Reporter) working in sequence
- **MCP Context Sharing**: Shared memory system allowing agents to access and build upon each other's work
- **Hierarchical Process**: Manager-coordinated workflow ensuring quality and consistency
- **Multiple Deployment Options**: Local execution, FastAPI REST API, Docker, and Vercel-ready
- **Production-Ready**: Includes health checks, error handling, and containerization

## Architecture

### Agents

1. **Senior Market Researcher**
   - Role: Gathers latest trends and market data
   - Output: Key facts, market size, key players, and trends
   - Uses MCP to store findings for downstream agents

2. **Data Analyst**
   - Role: Analyzes research data and identifies opportunities
   - Output: Top 3 trends and opportunities with structured analysis
   - Reads from MCP context and adds analytical insights

3. **Report Writer**
   - Role: Synthesizes all information into professional reports
   - Output: Complete markdown-formatted market report
   - Consumes all MCP context to create comprehensive documentation

### MCP Context System

The `MCPContext` class provides a simple but effective shared memory system:
- Agents can store and retrieve information using key-value pairs
- Enables seamless information flow between agents
- Prevents information loss during multi-step workflows

## Project Structure

```
article-01-deployment-tutorial/
├── agents/
│   ├── __init__.py
│   ├── researcher.py      # Market research agent
│   ├── analyst.py         # Data analysis agent
│   └── reporter.py        # Report generation agent
├── tools/
│   ├── __init__.py
│   └── mcp_context.py     # Shared context management
├── deploy/
│   └── app.py             # FastAPI application
├── main.py                # Local execution entry point
├── crew.py                # Agent orchestration logic
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── Dockerfile             # Container configuration
└── vercel.json            # Vercel deployment config
```

## Installation

### Prerequisites

- Python 3.11 or higher
- OpenAI API key

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd article-01-deployment-tutorial
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Local Execution

Run the market analyst on a specific topic:

```bash
python main.py
```

By default, it analyzes "AI Agents in India 2026". Modify `main.py` to change the topic:

```python
result = run_crew("Your Custom Topic Here")
```

### REST API

Start the FastAPI server:

```bash
uvicorn deploy.app:app --reload
```

The API will be available at `http://localhost:8000`

#### API Endpoints

**POST /analyze**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI Agents in India 2026"}'
```

**GET /health**
```bash
curl http://localhost:8000/health
```

Interactive API documentation: `http://localhost:8000/docs`

### Docker Deployment

Build and run the container:

```bash
docker build -t market-analyst .
docker run -p 8000:8000 --env-file .env market-analyst
```

Access the API at `http://localhost:8000`

### Vercel Deployment

This project is configured for Vercel serverless deployment:

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

3. Set environment variables in Vercel dashboard:
   - `OPENAI_API_KEY`

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Agent Configuration

Agents are configured in the `agents/` directory. You can customize:
- `role`: Agent's professional role
- `goal`: What the agent aims to achieve
- `backstory`: Context that shapes agent behavior
- `temperature`: LLM creativity (0 = deterministic, 1 = creative)

### Crew Configuration

In `crew.py`, you can modify:
- Task descriptions and expected outputs
- Process type (hierarchical, sequential, etc.)
- Manager LLM model
- Verbosity level

## How It Works

1. **Initialization**: The crew is created with three agents and three sequential tasks
2. **Research Phase**: Researcher agent gathers market data and stores in MCP
3. **Analysis Phase**: Analyst reads MCP context, identifies trends, and adds insights
4. **Reporting Phase**: Reporter synthesizes all MCP data into a final report
5. **Output**: Complete markdown report with research, analysis, and recommendations

The hierarchical process ensures a manager LLM coordinates the workflow, maintaining quality and consistency across all agent outputs.

## Dependencies

- `crewai>=0.51.0`: Multi-agent orchestration framework
- `langchain-openai`: OpenAI integration for LangChain
- `langchain-core`: Core LangChain functionality
- `fastapi`: Modern web framework for APIs
- `uvicorn`: ASGI server for FastAPI
- `python-dotenv`: Environment variable management

## Troubleshooting

**Issue**: "OpenAI API key not found"
- Solution: Ensure `.env` file exists with valid `OPENAI_API_KEY`

**Issue**: "Module not found" errors
- Solution: Run `pip install -r requirements.txt` in your virtual environment

**Issue**: API returns 500 errors
- Solution: Check logs for agent execution errors, verify API key is valid

## Related Article

This code accompanies the Medium article: [Hands-On Tutorial: Deploying Your First Scalable Multi-Agent System](https://medium.com/@sivareddyevuri92/hands-on-tutorial-deploying-your-first-scalable-multi-agent-system-with-mcp-optimization-5c0beda9d372)

## Author

**Manideep Reddy Eevuri**

- [LinkedIn](https://linkedin.com/in/manideep-reddy-eevuri-661659268)
- [Medium](https://medium.com/@sivareddyevuri92)
- [GitHub](https://github.com/Maniredii)

## License

This project is open source and available for educational purposes.
