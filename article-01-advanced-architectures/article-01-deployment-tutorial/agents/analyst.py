from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

analyst = Agent(
    role="Data Analyst",
    goal="Read MCP context and identify top 3 trends and opportunities",
    backstory="Expert at turning raw research into clear insights.",
    llm=llm,
    allow_delegation=False,
    verbose=True
)
