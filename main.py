import time
import streamlit as st

from news_agentic.pipeline import run_pipeline
from news_agentic.config import settings

st.set_page_config(page_title="News Agentic — Streamlit", layout="wide")
st.title("📰 Agentic News")

# --- Sidebar controls ---
with st.sidebar:
    st.header("Options")
    topic = st.text_input("Topic", value=settings.default_topic, help="e.g., India’s tech policy")
    run_btn = st.button("🚀 Generate Report", type="primary", use_container_width=True)

# --- State for progress log ---
if "log_lines" not in st.session_state:
    st.session_state.log_lines = []

def log(msg: str):
    st.session_state.log_lines.append(msg)

# --- Layout containers ---
status_box = st.container()
output_box = st.container()

# Initial status
if not st.session_state.log_lines:
    status_box.info("Enter a topic and click Generate.")

# Render current log
def render_log():
    if st.session_state.log_lines:
        status_box.markdown("\n".join(f"- {line}" for line in st.session_state.log_lines))

render_log()

# --- Action ---
if run_btn:
    # reset log for a fresh run
    st.session_state.log_lines = []
    log(f"Initializing pipeline for **{topic}**…")
    render_log()
    try:
        start = time.time()
        log("Fetching headlines and scraping articles…")
        render_log()

        path, md = run_pipeline(topic)

        elapsed = time.time() - start
        log(f"✅ Done in {elapsed:.1f}s")
        log(f"📄 Saved to `{path}`")
        render_log()

        with output_box:
            st.subheader("Report")
            st.markdown(md, help="Generated Markdown report")

            st.download_button(
                "⬇️ Download Markdown",
                data=md.encode("utf-8"),
                file_name=f"news_report_{time.strftime('%Y-%m-%d')}.md",
                mime="text/markdown",
                use_container_width=True
            )
    except Exception as e:
        log("❌ Failed")
        render_log()
        st.error(str(e))