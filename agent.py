import os
try:
    from dotenv import load_dotenv
    # Try loading from current directory and agents folder
    load_dotenv()
    # Try loading from agents folder if .env exists there
    try:
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(env_path):
            load_dotenv(env_path)
    except (NameError, AttributeError):
        pass  # __file__ might not be available in all contexts
    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL","gemini-2.0-flash")
    API_KEY = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
except ImportError:
    print("Error: dotenv module not found. Please install it using 'pip install python-dotenv'.")
    MODEL_NAME = "gemini-2.0-flash"
    API_KEY = None

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY or GEMINI_API_KEY environment variable is required. Please set it in your .env file.")

# Set the API key as environment variables for the library to use
os.environ["GOOGLE_API_KEY"] = API_KEY
os.environ["GEMINI_API_KEY"] = API_KEY  # Some libraries check for this name

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search
from agents.instructions import (
    TRIP_RESEARCH_INSTRUCTION,
    tripplanninginstructions
)
trip_research_agent = LlmAgent(
    name="TripResearchAgent",
    model=MODEL_NAME,
    instruction=TRIP_RESEARCH_INSTRUCTION,
    tools=[google_search],
    output_key="trip_research_summary"
)
trip_planner=SequentialAgent(
    name="TripPlanner",
    description=tripplanninginstructions,
    sub_agents=[trip_research_agent]
)
root_agent=trip_planner