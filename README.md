Local LLM Chatbot 🤖

An interactive local AI chatbot built with Python, Streamlit, Ollama, and the Qwen 0.5B language model.

The application provides a simple chat interface where users can send prompts and receive AI-generated responses from a language model running locally through Ollama.

✨ Features

- 💬 Interactive chat interface
- 🤖 Local AI inference with Ollama
- 🧠 Powered by Qwen 0.5B
- 🗂️ Conversation history during the session
- ⚡ Simple and lightweight architecture
- 🔒 Runs the language model locally without requiring a cloud AI API

🛠️ Technologies

- Python
- Streamlit
- Ollama
- Qwen 0.5B
- Requests

📁 Project Structure

local-llm-chatbot/
│
├── src/
│   ├── app.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/local-llm-chatbot.git
cd local-llm-chatbot

Replace "YOUR_USERNAME" with your GitHub username.

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\activate

3. Install Python dependencies

pip install -r requirements.txt

4. Install and set up Ollama

Install Ollama on your system and make sure it is running.

Then download the Qwen model:

ollama pull qwen:0.5b

5. Run the application

From the project root directory:

streamlit run src/app.py

The application will open in your browser.

🔄 How It Works

The application follows a simple workflow:

User
  ↓
Streamlit Chat Interface
  ↓
Python Application
  ↓
Ollama API
  ↓
Qwen 0.5B
  ↓
Generated Response
  ↓
Streamlit Chat Interface

The user's message is sent from the Streamlit interface to the local Ollama API.

Ollama processes the prompt using the Qwen 0.5B model and returns the generated response to the application.

The conversation history is maintained during the current session using Streamlit's "session_state".

🚀 Future Improvements

- [ ] Add model selection
- [ ] Add a clear chat button
- [ ] Improve prompt handling
- [ ] Support multiple Ollama models
- [ ] Add persistent conversation history
- [ ] Improve the chatbot UI/UX
- [ ] Add streaming responses

👩‍💻 Author

Sara Ayough

⭐ If you find this project useful, feel free to explore the repository.

