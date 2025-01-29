import os
import json
from crewai import Crew, Agent, Task, LLM, Process
from crewai_tools import SerperDevTool
from pydantic import BaseModel



# 1. Setting OPENAI_API_KEY env
api_key_path = "api.json"

with open(api_key_path, 'r') as f:
    api_key = json.load(f).get('Knovel', 0)
    
with open(api_key_path, 'r') as f:
    serper_api = json.load(f).get('serper_api', 0)

os.environ["OPENAI_API_KEY"] = api_key
os.environ["SERPER_API_KEY"] = serper_api

# 2. Setting LLM
llm = LLM(
    model="gpt-4o-mini",
    temperature=0.7,        # Higher for more creative outputs
    timeout=120,           # Seconds to wait for response
    max_tokens=4000,       # Maximum length of response
    top_p=0.9,            # Nucleus sampling parameter
    frequency_penalty=0.1, # Reduce repetition
    presence_penalty=0.1,  # Encourage topic diversity
    seed=42               # For reproducible results
)

# 3. Create an agent with all available parameters
research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company. You're responsible for analyzing data and providing insights to the business.""",
  verbose=True,
  llm=llm,
)

# 4. Task
search_tool = SerperDevTool()

# Example task
task = Task(
    description='Find and summarize the latest AI news',
    expected_output='A bullet list summary of the top 5 most important AI news today',
    agent=research_agent,
    tools=[search_tool],
    output_file="single_agent_output1.txt"
)

# Execute the crew
crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
# print(result)











# class Blog(BaseModel):
#     title: str
#     content: str


# # Define the agent
# blog_agent = Agent(
#     role="Blog Content Generator Agent",
#     goal="Generate a blog title and content",
#     backstory="""You are an expert content creator, skilled in crafting engaging and informative blog posts.""",
#     verbose=False,
#     allow_delegation=False,
#     llm="gpt-4o",
# )

# # Define the task with output_json set to the Blog model
# task1 = Task(
#     description="""Create a blog title and content on a given topic. Make sure the content is under 200 words.""",
#     expected_output="A JSON object with 'title' and 'content' fields.",
#     agent=blog_agent,
#     output_json=Blog,
#     output_file= "single_agent_output.json"
# )

# # Instantiate the crew with a sequential process
# crew = Crew(
#     agents=[blog_agent],
#     tasks=[task1],
#     verbose=True,
#     process=Process.sequential,
# )

# # Kickoff the crew to execute the task
# result = crew.kickoff()