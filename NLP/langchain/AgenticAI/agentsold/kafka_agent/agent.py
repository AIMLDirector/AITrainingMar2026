import os
import re
from collections import Counter
from google.adk.agents.llm_agent import Agent


# -------------------------------
# Resolve File Path (ANY FILE)
# -------------------------------
def resolve_path(file_name: str) -> str:
    if not file_name:
        file_name = "kafka.log"

    if os.path.isabs(file_name):
        return file_name

    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, file_name)


# -------------------------------
# Tool 1: Read ANY Log File
# -------------------------------
def read_log_file(file_name: str = "kafka.log") -> str:
    try:
        file_path = resolve_path(file_name)

        if not os.path.exists(file_path):
            return f"File not found: {file_path}"

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if not content.strip():
            return "Log file is empty."

        return content[:3000]

    except Exception as e:
        return f"Error reading file: {str(e)}"


# -------------------------------
# Tool 2: Analyze ANY Log File
# -------------------------------
def analyze_log_file(file_name: str = "kafka.log") -> str:
    try:
        file_path = resolve_path(file_name)

        if not os.path.exists(file_path):
            return f"File not found: {file_path}"

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            logs = f.readlines()

        if not logs:
            return "Log file is empty."

        error_lines = []
        warn_lines = []
        info_lines = []

        for line in logs:
            lower = line.lower()

            if "error" in lower:
                error_lines.append(line.strip())
            elif "warn" in lower:
                warn_lines.append(line.strip())
            elif "info" in lower:
                info_lines.append(line.strip())

        report = f"""
Log Analysis Report

File: {file_path}

Total Lines: {len(logs)}
Errors: {len(error_lines)}
Warnings: {len(warn_lines)}
Info Logs: {len(info_lines)}

Sample Errors:
{error_lines[:5] if error_lines else "None"}
"""

        if error_lines:
            report += "\nInsight: Errors detected. Check system components."

        if len(warn_lines) > 5:
            report += "\nInsight: High warnings. Possible instability."

        if not error_lines and not warn_lines:
            report += "\nSystem looks healthy."

        return report.strip()

    except Exception as e:
        return f"Error analyzing file: {str(e)}"


# -------------------------------
# Tool 3: Analyze PASTED Logs
# -------------------------------
def analyze_raw_logs(log_text: str) -> str:
    try:
        logs = log_text.split("\n")

        error_count = sum(1 for l in logs if "error" in l.lower())
        warn_count = sum(1 for l in logs if "warn" in l.lower())
        info_count = sum(1 for l in logs if "info" in l.lower())

        return f"""
Raw Log Analysis

Total Lines: {len(logs)}
Errors: {error_count}
Warnings: {warn_count}
Info Logs: {info_count}
"""

    except Exception as e:
        return f"Error analyzing raw logs: {str(e)}"


# -------------------------------
# ADK Agent (FINAL)
# -------------------------------
root_agent = Agent(
    model="gemini-2.5-flash",
    name="universal_log_analyzer",
    description="Analyze ANY log file dynamically.",
    instruction="""
You are a log analysis expert.

Rules:
- If user provides a file path → use it
- If user provides a file name → use it
- If user pastes logs → analyze directly
- Default file: kafka.log

Examples:
- analyze app.log
- analyze server.log
- analyze /Users/.../error.log
- analyze this log: <pasted text>

Use:
- analyze_log_file for file-based logs
- analyze_raw_logs for pasted logs
- read_log_file if user asks to view logs

Always return structured output.
""",
    tools=[read_log_file, analyze_log_file, analyze_raw_logs]
)