from __future__ import annotations
from crewai import Crew, Process
from .agents import build_researcher, build_summarizer, build_analyst, build_compiler
from .tasks import make_research_task, make_summarize_task, make_insight_task, make_compile_task

def make_crew():
    researcher = build_researcher()
    summarizer = build_summarizer()
    analyst    = build_analyst()
    compiler   = build_compiler()

    research_task  = make_research_task(researcher)
    summarize_task = make_summarize_task(summarizer, research_task)
    insight_task   = make_insight_task(analyst, summarize_task)
    compile_task   = make_compile_task(compiler, research_task, summarize_task, insight_task)

    return Crew(
        agents=[researcher, summarizer, analyst, compiler],
        tasks=[research_task, summarize_task, insight_task, compile_task],
        process=Process.sequential,
        verbose=True,
    )
