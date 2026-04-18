import os
import webbrowser
import datetime
import subprocess
import wikipedia
import pywhatkit

def open_chrome():
    # Attempt to open Chrome; path might need adjustment based on system
    try:
        os.system("start chrome")
    except Exception:
        print("Could not open Chrome")

def open_notepad():
    try:
        os.system("start notepad")
    except Exception:
        print("Could not open Notepad")

def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_github():
    webbrowser.open("https://www.github.com")

def wiki_search(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return "There are multiple results for that topic."
    except wikipedia.exceptions.PageError:
        return "I couldn't find any information on that topic."

def shutdown_system():
    os.system("shutdown /s /t 1")

def restart_system():
    os.system("shutdown /r /t 1")

def play_song(song):
    pywhatkit.playonyt(song)
