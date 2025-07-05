from crewai import Task
from tools import youtube_channel_tool
from agents import blog_researcher, blog_writer

#researcher task

researcher_task=Task(
    description=(
        'Identify the video{topic}'
        'get the detailed information about the video from the channel'
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the topic {topic} of video content',
    tools=[youtube_channel_tool],
    agent=blog_researcher
)

#writer task

writer_task=Task(
    description=(
        'get the information from the youtube channel on the topic {topic}'
    ),
    expected_output='summarize the information from the youtube channel video on the topic {topic}',
    tools=[youtube_channel_tool],
    agent=blog_writer,
    async_execution=False,
    output_file='new-blog-file.md'
)