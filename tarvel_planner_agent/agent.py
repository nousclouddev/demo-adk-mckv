import os

try:
    from dotenv import load_dotenv
    load_dotenv()

    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.0-flash")
except ImportError:
    print("Warning: python-dotenv not installed. Ensure API key is set")
    MODEL_NAME = "gemini-2.0-flash"

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

from tarvel_planner_agent.instructions import (
    ITINERARY_PLANNER_AGENT_INSTRUCTIONS,
    BUDGET_AGENT_INSTRUCTIONS,
    DEMO_ORCHESTRATOR_INSTRUCTION
)

itinerary_planner_agent = LlmAgent(
    name="ItineraryPlanner",
    model=MODEL_NAME,
    description="An agent that creates a detailed, personalized travel itinerary based on user input.",
    instruction=ITINERARY_PLANNER_AGENT_INSTRUCTIONS,
    tools=[google_search],
    output_key="itinerary_summary"  # Save result to state under this key
)

budget_agent = LlmAgent(
    name="BudgetAgent",
    model=MODEL_NAME,  # Using environment variable
    description="An agent that creates a detailed financial budget for a trip based on the itinerary provided by the Itinerary Planner Agent.", 
    instruction=BUDGET_AGENT_INSTRUCTIONS,
    tools=[google_search],  # This agent can also use the Google Search tool
    # This agent will automatically receive the output of the previous agent 
    output_key="budget_summary"  # Save result to state under this key
)



Demo_orchestrator = SequentialAgent(
    name="TravelPlannerAgent",
    description=DEMO_ORCHESTRATOR_INSTRUCTION,
    sub_agents=[
        itinerary_planner_agent,
        budget_agent,
    ]
)

root_agent = Demo_orchestrator