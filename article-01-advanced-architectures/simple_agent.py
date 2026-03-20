
# Demonstrates the basic Perceive → Decide → Act loop

from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from dotenv import load_dotenv
import os

load_dotenv()

# PERCEIVE: tool to sense the environment
search = DuckDuckGoSearchRun()
tools = [search]

# DECIDE: LLM as the brain
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ACT: ReAct loop - Reason then Act
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run it
result = executor.invoke({
    "input": "What are the top 3 AI agent frameworks in 2026?"
})

print("\n=== AGENT RESULT ===")
print(result["output"])