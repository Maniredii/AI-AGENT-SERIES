from crewai import Crew, Task, Process
from langchain_openai import ChatOpenAI
from agents.researcher import researcher
from agents.analyst import analyst
from agents.reporter import reporter
from tools.mcp_context import mcp
from dotenv import load_dotenv

load_dotenv()

def run_crew(topic: str):
    mcp.shared_context.clear()
    
    task1 = Task(
        description=f"Research this topic thoroughly: {topic}. Store findings in MCP.",
        agent=researcher,
        expected_output="Key facts, market size, key players, trends"
    )
    task2 = Task(
        description="Analyze MCP context. Find top 3 trends and opportunities.",
        agent=analyst,
        expected_output="Structured analysis stored in MCP",
        context=[task1]
    )
    task3 = Task(
        description="Read all MCP context. Write a complete market report.",
        agent=reporter,
        expected_output="Final professional markdown report",
        context=[task1, task2]
    )
    
    crew = Crew(
        agents=[researcher, analyst, reporter],
        tasks=[task1, task2, task3],
        process=Process.hierarchical,
        manager_llm=ChatOpenAI(model="gpt-4o-mini"),
        verbose=2
    )
    
    return crew.kickoff(inputs={"topic": topic})
