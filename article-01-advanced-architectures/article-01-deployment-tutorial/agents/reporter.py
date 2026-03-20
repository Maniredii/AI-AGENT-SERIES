from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

reporter = Agent(
    role="Report Writer",
    goal="Write a complete professional report using all MCP context",
    backstory="Technical writer who turns data into clean reports.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)
