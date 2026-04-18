import listener
import speaker
import intent_engine
import actions
import time

def main():
    speaker.speak("Assistant is starting...")
    print("Assistant started. Say 'Hey Assistant' to wake me up.")
    
    while True:
        text = listener.listen()
        
        if not text:
            continue
            
        if text == "API unavailable":
             print("Microphone not available. Exiting.")
             speaker.speak("Microphone not available. Exiting.")
             break
            
        print(f"Heard: {text}")
        
        # Wake word check or direct command if already active? 
        # Requirements say: Wake word support: “Hey Assistant”
        if "hey assistant" in text or "assistant" in text:
            speaker.speak("Yes?")
            command = listener.listen()
            if not command:
                speaker.speak("I didn't hear a command.")
                continue
                
            print(f"Command: {command}")
            intent, entity = intent_engine.parse_intent(command)
            
            if intent == "OPEN_APP":
                if entity == "chrome":
                    speaker.speak("Opening Chrome")
                    actions.open_chrome()
                elif entity == "notepad":
                    speaker.speak("Opening Notepad")
                    actions.open_notepad()
            elif intent == "OPEN_WEBSITE":
                if entity == "youtube":
                    speaker.speak("Opening YouTube")
                    actions.open_youtube()
                elif entity == "github":
                    speaker.speak("Opening GitHub")
                    actions.open_github()
            elif intent == "SEARCH_GOOGLE":
                speaker.speak(f"Searching Google for {entity}")
                actions.search_google(entity)
            elif intent == "GET_TIME":
                current_time = actions.get_time()
                speaker.speak(f"The time is {current_time}")
            elif intent == "WIKI_SEARCH":
                speaker.speak(f"Searching Wikipedia for {entity}")
                summary = actions.wiki_search(entity)
                speaker.speak(summary)
            elif intent == "SYSTEM_CONTROL":
                if entity == "shutdown":
                    speaker.speak("Shutting down the system")
                    actions.shutdown_system()
                elif entity == "restart":
                    speaker.speak("Restarting the system")
                    actions.restart_system()
            elif intent == "PLAY_SONG":
                speaker.speak(f"Playing {entity} on YouTube")
                actions.play_song(entity)
            elif intent == "EXIT":
                speaker.speak("Goodbye!")
                break
            else:
                speaker.speak("Sorry, I didn't understand execution command.")

if __name__ == "__main__":
    main()
