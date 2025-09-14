FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY news_agent /app/news_agent
COPY scripts /app/scripts

# Expose Streamlit port
EXPOSE 8501

# Default command: run the Streamlit app
CMD ["streamlit", "run", "scripts/ui_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]
