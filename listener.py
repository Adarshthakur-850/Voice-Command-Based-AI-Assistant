import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recognizer.pause_threshold = 0.8  # Reduced slightly
            recognizer.energy_threshold = 300 # Reduced for better sensitivity
            recognizer.dynamic_energy_threshold = True
            
            print(f"Listening... (Threshold: {recognizer.energy_threshold})")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5) # Reduced phrase limit
                print("Audio captured! Processing...")
                text = recognizer.recognize_google(audio)
                print(f"Recognized: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                print("Timeout - no speech detected")
                return ""
            except sr.UnknownValueError:
                print("Unknown Value - speech unintelligible")
                return ""
            except sr.RequestError as e:
                print(f"API Unavailable: {e}")
                return "API unavailable"
    except OSError as e:
        print(f"Microphone error: {e}")
        return "API unavailable"
    except Exception as e:
        print(f"Error in listener: {e}")
        return ""
