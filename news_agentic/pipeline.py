from __future__ import annotations
from typing import Tuple
from .crew import make_crew
from .utils.io import save_markdown

def run_pipeline(topic: str) -> Tuple[str, str]:
    crew = make_crew()
    result = crew.kickoff(inputs={"topic": topic})
    md = str(result).strip()
    path = save_markdown(md, topic)
    return path, md