# Xeto - Your AI-Powered Virtual Assistant 🤖

Xeto is a sophisticated virtual assistant built in Python that combines speech recognition, natural language processing, and various system control capabilities to provide a hands-free computing experience.

## 🌟 Features

- **Voice Interaction**: Fully voice-controlled interface using speech recognition
- **Natural Language Processing**: Intelligent response system using deep learning
- **Social Media Integration**: Quick access to popular platforms
  - Facebook
  - WhatsApp
  - Instagram
  - Discord
  - Twitter
  - YouTube
  - Telegram

- **System Controls**:
  - Volume control (up/down/mute/unmute)
  - System resource monitoring (CPU usage, battery status)
  - Application management (open/close various applications)

- **Personal Organization**:
  - College timetable management
  - Calendar integration
  - Schedule tracking

- **Entertainment**:
  - YouTube song playback
  - Web browsing assistance
  - Casual conversation capabilities

## 🛠️ Technical Requirements

### Dependencies
```
pyttsx3
speech_recognition
datetime
pyautogui
pycaw
comtypes
psutil
tensorflow
numpy
pywhatkit
```

### System Requirements
- Windows 10/11
- Python 3.7+
- Microphone access
- Internet connection for speech recognition and web features

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/29Krishna/Xeto_MyAIAssistant
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Ensure you have the following model files in your project directory:
- chat_model.h5
- tokenizer.pkl
- label_encoder.pkl
- intents.json

## 💻 Usage

1. Run the main script:
```bash
python main.py
```

2. Wait for the initial greeting from Xeto

3. Start speaking commands! Some example commands:
- "Open YouTube"
- "What's the system condition?"
- "Play a song"
- "Show my schedule"
- "Open calculator"
- "Volume up/down"

## 🎯 Key Features Explained

### Voice Control
The assistant uses `speech_recognition` for converting speech to text and `pyttsx3` for text-to-speech responses.

### Application Control
Can manage various Windows applications:
- Calculator
- Notepad
- Paint
- Calendar
- VS Code
- Microsoft Word

### System Monitoring
Monitors:
- CPU usage
- Battery percentage
- Volume levels
- System conditions

### Smart Conversations
Uses a trained deep learning model to understand and respond to various types of queries including:
- General questions
- Greetings
- Jokes
- Time and date queries
- Programming-related questions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Note

This project is designed primarily for Windows systems. Some features may require administrator privileges.

## 👥 Author

**Krishna**
- Email: krishnagupta2380@gmail.com 