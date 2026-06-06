from crewai import Crew
from tasks import analyze_kafka_logs_task, solution_task


def run_kafka_analyzer():
    crew = Crew(
        name="Kafka Log Analysis Crew",
        description="A crew of agents that analyze Kafka logs and design solutions based on the analysis.",
        tasks=[analyze_kafka_logs_task, solution_task],
        verbose=True
    )

    result = crew.kickoff(inputs={"log_file_path": "kafka.log"})
    print("Final Result:", result )



if __name__ == "__main__":
    run_kafka_analyzer()