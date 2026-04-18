<<<<<<< HEAD
# Voice Command Based AI Assistant

A Python-based AI assistant that listens to voice commands and executes system tasks offline.

## Features
- **Voice Recognition**: Listens via microphone.
- **Intent Understanding**: Uses spaCy NLP to understand "open chrome", "search google", etc.
- **System Control**: Open apps, shutdown/restart, get time.
- **Web Interaction**: Search Google, play YouTube videos, read Wikipedia.
- **Feedback**: Text-to-Speech responses.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    ```
    *Note: If you have trouble installing `pyaudio` on Windows, try:*
    ```bash
    pip install pipwin
    pipwin install pyaudio
    ```

2.  **Run the Assistant**:
    ```bash
    python main.py
    ```

## Commands
- **Wake Word**: "Hey Assistant" (Optional, currently active listening loop)
- "Open Chrome" / "Open Notepad"
- "Open YouTube" / "Open GitHub"
- "Search for [query] on Google"
- "What time is it?"
- "Tell me about [topic] from Wikipedia"
- "Play [song] on YouTube"
- "Shutdown system" / "Restart system"
- "Exit"

## Project Structure
- `main.py`: Entry point.
- `listener.py`: Microphone handling.
- `speaker.py`: TTS output.
- `intent_engine.py`: NLP logic.
- `actions.py`: Task execution functions.
=======
# Voice-Command-Based-AI-Assistant
ml project
>>>>>>> 6e2564a122cf011757093050e2d8da0b29b2795e
