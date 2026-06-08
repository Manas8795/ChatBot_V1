# Gemini AI Chatbot

A command-line chatbot built using Python and Google's Gemini API. The chatbot supports interactive conversations and maintains context using Gemini chat sessions, enabling multi-turn conversations.

## Features

* Interactive command-line chat interface
* Real-time AI-generated responses
* Conversation memory using Gemini chat sessions
* Lightweight and easy to use
* Built using the Google GenAI SDK
* Basic error handling

## Technologies Used

* Python 3.12+
* Google GenAI SDK
* Gemini 2.5 Flash Lite
* Git
* GitHub

## Project Structure

```
ChatBot/
├── chatbot.py
├── script.py
├── README.md
└── .gitignore
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/Manas8795/ChatBot.git
cd ChatBot
```

### Install Dependencies

```bash
pip install google-genai
```

## Configuration

Generate a Gemini API key from Google AI Studio and configure it in your application.

Google AI Studio:
https://aistudio.google.com

## Running the Chatbot

```bash
python chatbot.py
```

### Example

```text
You: Hello

Gemini: Hello! How can I help you today?

You: My name is Manas

Gemini: Nice to meet you, Manas!

You: What name did I tell you?

Gemini: You told me your name is Manas.
```

## Learning Outcomes

This project demonstrates:

* Working with Generative AI APIs
* Building conversational applications
* Managing conversation context and memory
* Using Git for version control
* Publishing projects on GitHub

## Future Improvements

* Save chat history to files
* Load previous conversations
* Add custom chatbot personalities
* Build a graphical user interface (GUI)
* Voice input and speech output
* PDF summarization
* Research paper analysis

## Author

**Manas Agrawal**
Computer Science Student, VIT Chennai
