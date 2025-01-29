import os
import json
from crewai import Crew, Agent, Task, LLM, Process
from crewai_tools import SerperDevTool, VisionTool
from pydantic import BaseModel


search_tool = SerperDevTool()
vision_tool = VisionTool()
image_url = '000000581357.jpg'


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

def researcher(self) -> Agent:
    '''
    This agent uses the VisionTool to extract text from images.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[vision_tool]
    )

research_agent = Agent(
  role='Image Text Extraction Specialist',
  goal= f"Extract and analyze text from images efficiently using AI-powered tools. You should get the text from {image_url}",
  backstory="""You are an expert in text extraction, specializing in using AI to process and analyze textual content from images. Make sure you use the tools provided.""",
  verbose=True,
  llm=llm,
)



# 4. Task
# Example task
task = Task(
    description=f"Extract and analyze text from images efficiently using AI-powered tools.",
    expected_output='A string containing the full text extracted from the image.',
    agent=research_agent,
    tools=[vision_tool],
    allow_delegation=False,
    output_file="vision_task.txt",
)

# Execute the crew
crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()
# print(result)
