from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import writer_task, researcher_task
from tools import youtube_channel_tool


#forming the crew with the required agents, tasks and tools
crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[researcher_task, writer_task],
    tools=[youtube_channel_tool],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True,
    verbose=True,
)

#starting the execution
result=crew.kickoff(inputs={'topic': 'AI vs ML vs DL vs Datascience'})
print(result)