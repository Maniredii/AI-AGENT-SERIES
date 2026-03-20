
# Financial analyst agent using Yahoo Finance data

from langchain_openai import ChatOpenAI
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
finance_tool = YahooFinanceNewsTool()

def get_financials(ticker):
    """Fetches latest financial news for a stock ticker."""
    return finance_tool.run(ticker)

def analyze_stock(ticker):
    """
    Analyzes a stock using Yahoo Finance data.
    Returns: investment recommendation with reasoning.
    """
    print(f"\n📈 Analyzing {ticker}...")

    # Get financial data
    raw_data = get_financials(ticker)

    # Ask LLM to analyze
    prompt = f"""
    Based on this financial news for {ticker}:
    {raw_data}
    
    Please provide:
    1. Key financial highlights
    2. Recent developments
    3. Brief investment outlook (bullish/bearish/neutral)
    
    Keep it concise and factual.
    """

    response = llm.invoke(prompt)
    return response.content


# Demo
if __name__ == "__main__":
    # Analyze a tech stock
    result = analyze_stock("NVDA")  # NVIDIA
    print("\n=== FINANCIAL ANALYSIS ===")
    print(result)