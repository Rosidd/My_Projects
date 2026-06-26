from agentspan.agents import Agent, tool, run

@tool
def search_web(query: str) -> str:
    """Search the web for information."""
    ...

@tool
def fetch_page(url: str) -> dict:
    """Fetch and parse a webpage."""
    ...

researcher = Agent(
    name="researcher",
    model="anthropic/claude-sonnet-4-6",
    tools=[search_web, fetch_page],
    instructions="Research the topic thoroughly.",
)

writer = Agent(
    name="writer",
    model="openai/gpt-4o",
    instructions="Write a clear article from the research.",
)

result = run(researcher >> writer, "AI agents in production")
result.print_result()