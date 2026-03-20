from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

researcher = Agent(
    role="Senior Market Researcher",
    goal="Gather latest trends and data using MCP context",
    backstory="Expert researcher with perfect memory via MCP.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)
