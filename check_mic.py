import speech_recognition as sr

def list_microphones():
    print("Available Microphones:")
    mics = sr.Microphone.list_microphone_names()
    for i, mic_name in enumerate(mics):
        print(f"{i}: {mic_name}")

def test_mic(index=None):
    r = sr.Recognizer()
    try:
        with sr.Microphone(device_index=index) as source:
            print(f"\nTesting Microphone (Index: {index if index is not None else 'Default'})...")
            print("Please speak something...")
            # r.adjust_for_ambient_noise(source, duration=1) # Reduced duration for testing
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            print("Audio captured. Recognizing...")
            try:
                text = r.recognize_google(audio)
                print(f"Success! Heard: {text}")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Request error: {e}")
    except OSError as e:
        print(f"Error accessing microphone: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    list_microphones()
    # You can manually change the index in the call below if you identify the correct mic from the list
    test_mic()
