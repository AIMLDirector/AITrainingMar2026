
import os
import re
from collections import Counter
from google.adk.agents.llm_agent import Agent

# -------------------------------
# 📂 Resolve Log File Path (FIXED)
# -------------------------------
def get_log_path(file_name: str = "kafka.log") -> str:
    """
    Always resolve kafka.log relative to THIS agent file.
    This avoids ADK working directory issues.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, file_name)


# -------------------------------
# 📖 Tool 1: Read Kafka Log
# -------------------------------
def read_kafka_log(file_name: str = "kafka.log") -> str:
    """
    Reads Kafka log file content.
    """
    try:
        file_path = get_log_path(file_name)

        if not os.path.exists(file_path):
            return f"❌ Log file not found at: {file_path}"

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if not content.strip():
            return "⚠️ Log file is empty. Please add Kafka logs."

        return content[:5000]  # limit size for LLM

    except Exception as e:
        return f"Error reading log file: {str(e)}"


# -------------------------------
# 🔍 Tool 2: Analyze Kafka Logs
# -------------------------------
def analyze_kafka_logs(file_name: str = "kafka.log") -> str:
    """
    Analyze Kafka logs and generate insights.
    """
    try:
        file_path = get_log_path(file_name)

        if not os.path.exists(file_path):
            return f"❌ Log file not found at: {file_path}"

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            logs = f.readlines()

        if not logs:
            return "⚠️ Log file is empty."

        error_lines = []
        warn_lines = []
        info_lines = []
        topics = []

        for line in logs:
            lower = line.lower()

            if "error" in lower:
                error_lines.append(line.strip())
            elif "warn" in lower:
                warn_lines.append(line.strip())
            elif "info" in lower:
                info_lines.append(line.strip())

            # Extract Kafka topic names
            topic_match = re.findall(r'topic[=\s:]+([a-zA-Z0-9._-]+)', lower)
            topics.extend(topic_match)

        topic_counts = Counter(topics).most_common(5)

        # -------------------------------
        # 📊 Build Report
        # -------------------------------
        report = f"""
📊 Kafka Log Analysis Report

📁 File: {file_path}

🔢 Total Lines: {len(logs)}
❌ Errors: {len(error_lines)}
⚠️ Warnings: {len(warn_lines)}
ℹ️ Info Logs: {len(info_lines)}

📌 Top Topics:
{topic_counts if topic_counts else "No topics found"}

🚨 Sample Errors:
{error_lines[:5] if error_lines else "No errors found"}
"""

        # -------------------------------
        # 🧠 Add Insights
        # -------------------------------
        if len(error_lines) > 0:
            report += "\n⚠️ Insight: Errors detected → Possible broker issues, topic misconfiguration, or network failures.\n"

        if len(warn_lines) > 5:
            report += "⚠️ Insight: High warnings → System instability or performance issues.\n"

        if len(error_lines) == 0 and len(warn_lines) == 0:
            report += "✅ System looks healthy.\n"

        return report.strip()

    except Exception as e:
        return f"Error analyzing logs: {str(e)}"


# -------------------------------
# 🤖 ADK Agent (MANDATORY NAME)
# -------------------------------
root_agent = Agent(
    model="gemini-2.5-flash",
    name="kafka_log_analyzer",
    description="AI agent to analyze Kafka log files and provide insights.",
    instruction="""
You are a Kafka log analysis expert.

- Use analyze_kafka_logs when user asks to analyze logs.
- Use read_kafka_log if raw logs are requested.
- Identify errors, warnings, anomalies.
- Provide clear insights and possible root causes.
- Keep responses structured and easy to read.

If log file is missing or empty, clearly inform the user.
""",
    tools=[read_kafka_log, analyze_kafka_logs]
)