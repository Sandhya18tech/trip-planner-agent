 trip-planner-agent
Trip Planner Agent — An AI agent that uses Google's ADK to research destinations and create trip plans. It searches for destinations, attractions, accommodations, transportation, and local information, then generates a plan based on user requirements.
Features

- Trip Research Agent: Automatically researches destinations, attractions, accommodations, transportation, and local information
- Google Search Integration: Uses Google Search tool to gather up-to-date information
- Sequential Agent Architecture: Orchestrates multiple agents to create comprehensive trip plans
- Environment-based Configuration: Secure API key management using environment variables

 Prerequisites

- Python 3.8 or higher
- Google API Key (Gemini API Key)
- pip package manager

 Installation

1. Clone this repository:
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd Agent-learning2. Install the required dependencies:
pip install -r requirement.txt
3. Create a `.env` file in the root directory:
GOOGLE_API_KEY=your_api_key_here
GOOGLE_GENAI_MODEL=gemini-2.0-flashAlternatively, you can set the environment variables directly:
- `GOOGLE_API_KEY` or `GEMINI_API_KEY`: Your Google Gemini API key
- `GOOGLE_GENAI_MODEL`: Model name (default: `gemini-2.0-flash`)
