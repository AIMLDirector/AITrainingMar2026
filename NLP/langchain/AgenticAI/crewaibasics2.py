import os
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from crewai_tools import WebSearchTool, CodeExecutionTool
load_dotenv()

# 1. Define your Agents
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge developments in {topic}',
  backstory="""You are an expert at finding hidden trends. 
  You provide raw, factual data for others to process.""",
  verbose=True,
  allow_delegation=False
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft a compelling blog post about {topic}',
  backstory="""You take raw research data and turn it into 
  engaging, easy-to-read articles for a tech audience.""",
  verbose=True
)

research_task= Task(
      description='Analyze the current state of {topic}. Focus on 3 key breakthroughs.',
      expected_output='A detailed list of 3 bullet points with supporting evidence.',
      agent=researcher
    )

write_task = Task(
  description='Using the research provided, write a 300-word blog post.',
  expected_output='A markdown formatted blog post.',
  agent=writer,
  context=[research_task] 
)

test_task = Task(

  context = [research_task, write_task],
)

crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential, 
  verbose=True
)


result = crew.kickoff(inputs={'topic': 'AI Agents in Production'})
print(result)
