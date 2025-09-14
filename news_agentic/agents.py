from __future__ import annotations
from crewai import Agent
from .tools import get_search_tool, get_site_search_tool, get_scrape_tool

def build_researcher() -> Agent:
    return Agent(
        role="News Researcher",
        goal="Find relevant, recent, credible articles; return clean metadata.",
        backstory="Meticulous journalist; prefers trustworthy sources and recency; deduplicates links.",
        tools=[get_search_tool(), get_site_search_tool()],
        allow_delegation=False,
    )

def build_summarizer() -> Agent:
    return Agent(
        role="Article Summarizer",
        goal="Open each URL and produce a faithful 120–180 word summary with key facts.",
        backstory="Fast, accurate distiller of news; avoids speculation.",
        tools=[get_scrape_tool()],
        allow_delegation=False,
    )

def build_analyst() -> Agent:
    return Agent(
        role="Insight Analyst",
        goal="Synthesize 3–6 cross-article insights: consensus, disagreements, trends, watch-fors.",
        backstory="Connects dots across sources and surfaces what matters.",
        allow_delegation=False,
    )

def build_compiler() -> Agent:
    return Agent(
        role="Report Editor",
        goal="Assemble a polished Markdown report with required sections and formatting.",
        backstory="Precise editor ensuring completeness and clarity.",
        allow_delegation=False,
    )
