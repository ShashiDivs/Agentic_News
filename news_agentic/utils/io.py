from __future__ import annotations
from datetime import datetime
from pathlib import Path

def save_markdown(md: str, topic: str) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_topic = "".join(c for c in topic if c.isalnum() or c in (" ", "-", "_")).strip().replace(" ", "_")
    fname = f"news_report_{safe_topic}_{date_str}.md"
    out = Path(fname).resolve()
    out.write_text(md, encoding="utf-8")
    return str(out)