from google.adk.agents import LlmAgent

capital_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="capital_agent",
    description="Answers capital city questions",  # fixed typo 'descripition'
    instruction="""You're an expert in geography. Detect the country in the user query. Use the tool to respond with the capital."""
)

def get_capital_city(country: str) -> str:
    return {
        "france": "Paris",
        "japan": "Tokyo"
    }.get(country.lower(), "Unknown")

capital_agent.register_tool(get_capital_city)
capital_agent.memory.set("last_country", "France")
capital_agent.memory.get("last_country")

response = capital_agent.run("What's the capital of Japan?")
print(response)