🤖 AI-Powered Blog Generator from YouTube Videos<br>
<br>
<br>
🧠 Project Overview<br>
This project uses multi-agent AI architecture with CrewAI to generate blog content from YouTube video topics. It includes two agents:<br>
🧑‍💼 Researcher Agent: Extracts insights and detailed content from the specified YouTube channel<br>
✍️ Writer Agent: Summarizes the findings into a well-written blog post<br>
Powered by LangChain, OpenAI GPT-4, and the YoutubeChannelSearchTool, this AI workflow turns video content into publish-ready blog articles.<br>
<br>
<br>
🛠️ Features<br>
🔍 Extracts content from specific YouTube channel videos<br>
✒️ Automatically writes blog articles from the retrieved video content<br>
🧠 Multi-agent architecture using CrewAI<br>
🤖 Integrates OpenAI GPT-4 via LangChain<br>
📺 Uses YoutubeChannelSearchTool for topic-based video search<br>
💾 Saves final output as a Markdown blog file<br>
<br>
<br>
🔧 Setup Instructions<br>
<br>
1. Clone the Repository<br>
git clone https://github.com/your-username/youtube-blog-generator.git<br>
cd youtube-blog-generator<br>
<br>
<br>
2. Install Requirements<br>
pip install -r requirements.txt<br>
<br>
<br>
3. Add Your Environment Variables<br>
Create a .env file:<br>
OPENAI_API_KEY=your_openai_key_here<br>
<br>
<br>
4. Set Your YouTube Channel Handle<br>
In tools.py, replace the channel handle with your actual one:<br>
youtube_channel_tool = YoutubeChannelSearchTool(<br>
    youtube_channel_handle='@yourchannel'<br>
)<br>
<br>
<br>
5. Run the Crew<br>
python crew.py<br>
<br>
📄 Output Example<br>
The blog will be saved to a file like:<br>
new-blog-file.md<br>
Containing 3+ paragraph blog content based on the selected YouTube video.<br>
<br>
<br>
🧰 Tech Stack<br>
CrewAI<br>
LangChain<br>
OpenAI GPT-4<br>
YoutubeChannelSearchTool<br>
Python<br>
<br>
<br>
🔓 License<br>
MIT License<br>
