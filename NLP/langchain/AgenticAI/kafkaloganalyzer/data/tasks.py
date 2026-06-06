from crewai import Task
from agents import log_analyzer_agent, solution_architect_agent

analyze_kafka_logs_task = Task(
        description="""Analyze Kafka logs and extract:
                        - Key issues
                        - Insights
                        - Recommendations""",
        agent=log_analyzer_agent,
        expected_output="structured summary of kafka log analysis including key issues, insights, and recommendations"
)


solution_task = Task(
        description="""Design a solution based on the insights provided by the Kafka Log Analyzer.""",
        agent=solution_architect_agent,
        expected_output="strategic long term solutiion recommendations based on the insights from the Kafka log analysis and also useful links to relevant documentation or resources that can help implement the solution"
)

