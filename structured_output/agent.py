# Example for Output Schema
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field # Library to define these schematics
from google.adk.agents import Agent

# Define the output structure
class GreetingOutput(BaseModel):
    greeting: str = Field(description="A greeting message to the person.")

# Agent that must return structured output
root_agent = Agent(
    name="output_schema_agent", # Names cannot have spaces in them!
    model="gemini-2.0-flash",
    instruction="Given a person's name, respond with a JSON object like {\"greeting\": \"Hello, name!\"}",
    output_schema=GreetingOutput,  # Enforces structured output
    output_key="final_greeting"
)