
# Research agent with web search + context enrichment

from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

search = DuckDuckGoSearchRun()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- Context Engine ---
def enrich_context(query, user_id="default"):
    """Adds user context to the query."""
    # Simulated user profiles (in production, read from database)
    profiles = {
        "beginner": {"technical_level": "basic", "preferred_sources": ["blogs"]},
        "advanced": {"technical_level": "advanced", "preferred_sources": ["arxiv", "papers"]},
        "default":  {"technical_level": "standard", "preferred_sources": ["general"]},
    }
    profile = profiles.get(user_id, profiles["default"])
    return {**{"query": query}, **profile}

# --- Router ---
def route_task(context):
    """Selects tools based on user technical level."""
    if context['technical_level'] == "advanced":
        return [search_web, analyze_topic]
    return [search_web]

# --- Tools ---
def search_web(query):
    return search.run(query)

def analyze_topic(query):
    """Deeper analysis for advanced users."""
    return search.run(f"{query} research paper technical deep dive")

# --- Synthesizer ---
prompt = ChatPromptTemplate.from_template(
    "Based on this research: {materials}\n\nAnswer this question clearly: {query}"
)
synthesizer = prompt | llm | StrOutputParser()

# --- Full Research Agent ---
def research_agent(query, user_id="default"):
    """
    Complete research agent:
    1. Enriches context based on user profile
    2. Routes to appropriate tools
    3. Gathers materials
    4. Synthesizes final answer
    """
    print(f"\n🔍 Researching: '{query}' for user: {user_id}")

    context = enrich_context(query, user_id)
    tools = route_task(context)

    print(f"📦 Using {len(tools)} tool(s) for {context['technical_level']} level")

    materials = [tool(query) for tool in tools]
    combined = "\n\n".join(materials)

    result = synthesizer.invoke({"materials": combined, "query": query})
    return result


# Run it
if __name__ == "__main__":
    # Basic user
    print(research_agent("What is an AI agent?", user_id="beginner"))

    # Advanced user - uses more tools
    print(research_agent("How does LangGraph work internally?", user_id="advanced"))