from crewai import Agent
from tools import youtube_channel_tool
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
llm=ChatOpenAI(model="gpt-4",temperature=0.7)

#blog researcher agent

blog_researcher=Agent(
    role='Blog researcher from youtube videos',
    goal='get the relevant video content for the topic {topic} from the YT channel',
    verbose=True,
    memory=True,
    backstory=(
       "Expert in understanding and gathering information from the youtube videos especially in the topics of Artificial Intelligence, Data Science, Machine Learning and Deep Learning"
    ),
    llm=llm,
    tools=[youtube_channel_tool],
    allow_delegation=True
)

#blog writer agent

blog_writer=Agent(
    role='Writer',
    goal='Narrate compelling tech stories about the video topic {topic}from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing me"
        "discoveries to light in an accessible manner"
    ),
    tools=[youtube_channel_tool],
    llm=llm,
    allow_delegation=False
)