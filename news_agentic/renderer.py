from __future__ import annotations
from datetime import datetime
from .schemas import Headlines, Summaries, Insights

def render_report(topic: str, headlines: Headlines, summaries: Summaries, insights: Insights) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    lines = []
    lines.append(f"# News Report on {topic}")
    lines.append(f"*Date: {date_str}*")
    lines.append("")
    lines.append("## Section 1: Headlines")
    for i, h in enumerate(headlines.headlines, start=1):
        lines.append(f"{i}. **{h.title}** — {h.source}  \n   {h.url}")
    if not headlines.headlines:
        lines.append("_No headlines found._")
    lines.append("")
    lines.append("## Section 2: Summaries")
    if summaries.summaries:
        for i, s in enumerate(summaries.summaries, start=1):
            lines.append(f"### {i}. {s.title} — {s.source}\n{s.url}\n")
            lines.append(s.summary.strip())
            lines.append("")
    else:
        lines.append("_No summaries produced._\n")
    lines.append("## Section 3: Final Insights")
    if insights.insights:
        for it in insights.insights:
            lines.append(f"- {it}")
    else:
        lines.append("_No insights identified._")
    return "\n".join(lines)
