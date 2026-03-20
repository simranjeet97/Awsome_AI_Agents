import pathlib
import os
import httpx
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.skills import load_skill_from_dir, models
from google.adk.tools import skill_toolset

# ─────────────────────────────────────────────────────────────────────────────
# ENVIRONMENT
# load_dotenv() reads your .env file and puts GOOGLE_API_KEY and NEWS_API_KEY
# into os.environ - this must happen before anything tries to read those values
# ─────────────────────────────────────────────────────────────────────────────
load_dotenv()

# ─────────────────────────────────────────────────────────────────────────────
# TOOL FUNCTIONS
# These are the actual executors - they make real network calls and return data.
# The skills tell the agent WHEN and WHY to call them.
# The tools tell the agent HOW to call them (schema, arguments, return shape).
# ─────────────────────────────────────────────────────────────────────────────

def get_weather(city: str) -> dict:
    """
    Fetches current weather for a given city using the wttr.in API.

    Args:
        city: The name of the city to fetch weather for.

    Returns:
        A dictionary containing weather data or an error message.
    """
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = httpx.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data["current_condition"][0]
        area = data["nearest_area"][0]

        return {
            "city": area["areaName"][0]["value"],
            "country": area["country"][0]["value"],
            "temp_c": current["temp_C"],
            "feels_like_c": current["FeelsLikeC"],
            "condition": current["weatherDesc"][0]["value"],
            "wind_kmph": current["windspeedKmph"],
            "humidity": current["humidity"],
        }
    except httpx.HTTPError as e:
        return {"error": f"Could not fetch weather: {str(e)}"}
    except KeyError:
        return {"error": f"Location '{city}' not found. Please check the city name."}

def get_news(category: str = "general", page_size: int = 5) -> dict:
    """
    Fetches the latest news headlines from NewsAPI.

    Args:
        category: News category (technology, business, sports, health,
                  science, general). Defaults to 'general'.
        page_size: Number of headlines to return (1-20). Defaults to 5.

    Returns:
        A dictionary with a list of articles or an error message.
    """
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        return {"error": "NEWS_API_KEY not configured"}

    try:
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": api_key,
            "category": category,
            "language": "en",
            "pageSize": page_size,
        }

        response = httpx.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        articles = []
        for article in data.get("articles", []):
            articles.append({
                "title": article.get("title", "No title"),
                "description": article.get("description", "No description"),
                "source": article.get("source", {}).get("name", "Unknown"),
                "published_at": article.get("publishedAt", ""),
                "url": article.get("url", ""),
            })

        return {
            "category": category,
            "total_results": data.get("totalResults", 0),
            "articles": articles,
        }

    except httpx.HTTPError as e:
        return {"error": f"News API request failed: {str(e)}"}

def create_news_skill(api_key: str) -> models.Skill:
    """Creates the news summarizer skill with runtime API configuration."""

    return models.Skill(
        frontmatter=models.Frontmatter(
            name="news-summarizer",
            description=(
                "Fetches and summarizes the latest news headlines. "
                "Use this skill when the user asks about news, current events, "
                "headlines, what's happening, trending topics, or sports results. "
                "Can filter by category: technology, business, sports, health, science."
            ),
        ),
        instructions=(
            "You are a news briefing specialist. Your job is to fetch and present "
            "the latest news in a clear, concise format.\n\n"
            "## Steps\n"
            "Step 1: Use the `get_news` function tool to fetch headlines.\n"
            "Step 2: Group headlines by topic if multiple categories were requested.\n"
            "Step 3: For each headline, provide:\n"
            "  - 📰 Headline title\n"
            "  - One sentence summary of what happened\n"
            "  - Source name\n\n"
            "## Rules\n"
            "- Present a maximum of 5 headlines unless the user asks for more.\n"
            "- Always mention when the news was published (e.g., '2 hours ago').\n"
            "- If no news is found for a category, say so clearly.\n"
            "- Never editorialize or add personal opinions to the news."
        ),
        resources=models.Resources(
            references={
                "CATEGORIES.md": (
                    "# Available News Categories\n"
                    "- technology: Tech, AI, software, hardware news\n"
                    "- business: Finance, markets, economy\n"
                    "- sports: All sports news including cricket, football, tennis\n"
                    "- health: Medical, wellness, public health\n"
                    "- science: Research, space, discoveries\n"
                    "- general: Top stories across all topics (default)\n"
                ),
            }
        ),
    )

def create_joke_skill() -> models.Skill:
    """Creates a joke-of-the-day skill powered entirely by instructions."""
    return models.Skill(
        frontmatter=models.Frontmatter(
            name="joke-of-the-day",
            description=(
                "Tells a joke, pun, or funny observation on demand. "
                "Use this skill when the user asks for a joke, something funny, "
                "a pun, humour, or wants to be entertained."
            ),
        ),
        instructions=(
            "You are a stand-up comedian specialising in clean, clever humour.\n\n"
            "## How to tell a joke\n"
            "Step 1: Read FORMATS.md to choose an appropriate joke format.\n"
            "Step 2: Generate an original joke in that format.\n"
            "Step 3: Deliver the punchline on a new line after a short pause "
            "(represented by '...').\n\n"
            "## Rules\n"
            "- Keep all humour clean and inoffensive.\n"
            "- Never repeat a joke you've told in the same session.\n"
            "- If the user specifies a topic (tech, food, animals), use it.\n"
            "- End with an optional brief follow-up offer: "
            "'Want another one?'"
        ),
        resources=models.Resources(
            references={
                "FORMATS.md": (
                    "# Joke Formats\n\n"
                    "## Setup / Punchline\n"
                    "Classic two-liner. Setup creates expectation, "
                    "punchline subverts it.\n"
                    "Example structure: 'Why did X do Y?\\n...Because Z.'\n\n"
                    "## Pun\n"
                    "Wordplay based on multiple meanings or similar sounds.\n"
                    "Best for: tech topics, food, everyday objects.\n\n"
                    "## Observational\n"
                    "A funny observation about something universal and relatable.\n"
                    "Best for: programming, meetings, coffee, deadlines.\n\n"
                    "## One-liner\n"
                    "Single sentence, complete joke. High difficulty, high reward.\n"
                    "Best for: confident delivery, short responses.\n"
                ),
            }
        ),
    )

# ─────────────────────────────────────────────────────────────────────────────
# SKILL 1: Weather - File-Based
# load_skill_from_dir() reads the SKILL.md and references/ folder and builds
# a Skill object from them. Same result as models.Skill(...), different source.
# ─────────────────────────────────────────────────────────────────────────────
weather_skill = load_skill_from_dir(
    pathlib.Path(__file__).parent / "skills" / "weather-skill"
)

# ─────────────────────────────────────────────────────────────────────────────
# SKILL 2: News - Inline
# Constructed at runtime by the factory function you wrote in Section 4.
# ─────────────────────────────────────────────────────────────────────────────
news_skill = create_news_skill(api_key=os.getenv("NEWS_API_KEY", ""))

# ─────────────────────────────────────────────────────────────────────────────
# SKILL 3: Joke of the Day - Inline
# ─────────────────────────────────────────────────────────────────────────────
joke_skill = create_joke_skill()

# ─────────────────────────────────────────────────────────────────────────────
# SKILL TOOLSET
# SkillToolset bundles both skills into a single object the Agent can hold.
# Think of it as the agent's "skills menu" - the complete list of specialist
# knowledge modules available to it.
# ─────────────────────────────────────────────────────────────────────────────
my_toolset = skill_toolset.SkillToolset(
    skills=[weather_skill, news_skill, joke_skill]
)

# ─────────────────────────────────────────────────────────────────────────────
# THE AGENT
# This is the variable ADK looks for when you run `adk web` or `adk run`.
# It must be named `root_agent` at module level for the CLI to find it.
# ─────────────────────────────────────────────────────────────────────────────
root_agent = Agent(
    model="gemini-2.5-flash",
    name="daily_briefing_agent",
    description=(
        "A helpful daily briefing assistant that provides weather updates "
        "and news summaries for any location and topic."
    ),
    instruction=(
        "You are a friendly daily briefing assistant. "
        "You help users stay informed by providing accurate weather information "
        "and the latest news headlines. "
        "When answering, always be concise and well-organized. "
        "Use your weather skill for weather queries, your news skill for news queries, "
        "and your joke skill for entertainment. "
        "If the user asks for multiple things in a single question, answer all of them."
    ),
    tools=[
        my_toolset,    # the skills menu - tells the agent WHEN to use each skill
        get_weather,   # the actual executor - called by the weather skill
        get_news,      # the actual executor - called by the news skill
    ],
)
