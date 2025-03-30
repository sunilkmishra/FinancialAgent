import os
from agno.playground import Playground, serve_playground_app
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Set API keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

## Online Search Agent
online_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search online for information",
    model = Groq(id="llama-3.3-70b-specdec",api_key=GROQ_API_KEY),
    tools = [DuckDuckGoTools()],
    instructions=["Always include search"],
    show_tool_calls=True,
    markdown=True,
)

## Stock Price Analyser Agent
finance_agent = Agent(
    name="Finance Agent",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    show_tool_calls=True,
    model = Groq(id="llama-3.3-70b-specdec",api_key=GROQ_API_KEY),
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True,
)

## Multi AI-Agent
app = Playground(agents=[finance_agent,online_search_agent]).get_app()

if __name__== "__main__":
    serve_playground_app(app)
