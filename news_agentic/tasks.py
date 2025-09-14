from __future__ import annotations
from crewai import Task
from .config import settings

def make_research_task(agent) -> Task:
    return Task(
        description=(
            "Search the web for recent, credible articles about the topic: '{topic}'. "
            f"Return 5–{settings.max_articles} unique items with fields: title, source, url, published_date "
            f"(prefer items from the past {settings.recency_days} days). "
            "Exclude duplicates and low-credibility sites."
        ),
        expected_output=(
            "JSON list named 'headlines' with objects: "
            "{'title': str, 'source': str, 'url': str, 'published_date': 'YYYY-MM-DD'}"
        ),
        agent=agent
    )

def make_summarize_task(agent, research_task) -> Task:
    return Task(
        description=(
            "Given prior output 'headlines', open each URL and extract the main article text. "
            "Produce a 120–180 word summary per article capturing who/what/when/where/why. "
            "Return JSON list 'summaries' with objects: "
            "{'title': str, 'source': str, 'url': str, 'summary': str}."
        ),
        expected_output="JSON list named 'summaries' aligned with 'headlines'.",
        agent=agent,
        context=[research_task]
    )

def make_insight_task(agent, summarize_task) -> Task:
    return Task(
        description=(
            "Read 'summaries' and synthesize 3–6 insights (themes, trends, contradictions, watch-fors). "
            "Output a JSON object with key 'insights' whose value is a list[str]."
        ),
        expected_output="{'insights': [str, ...]}",
        agent=agent,
        context=[summarize_task]
    )

def make_compile_task(agent, research_task, summarize_task, insight_task) -> Task:
    return Task(
        description=(
            "Assemble the final Markdown report with this exact structure:\n"
            "Title: 'News Report on {topic}'\n"
            "Date: today's date (YYYY-MM-DD)\n"
            "Section 1: Headlines (numbered: title + source + url)\n"
            "Section 2: Summaries (1..N matching headlines)\n"
            "Section 3: Final Insights (bulleted)\n\n"
            "Return ONLY the Markdown string."
        ),
        expected_output="A Markdown string of the final report.",
        agent=agent,
        context=[research_task, summarize_task, insight_task]
    )
