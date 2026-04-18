import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def parse_intent(text):
    doc = nlp(text)
    intent = None
    entity = None

    # Simple keyword/pattern matching enhanced by NLP
    if "open" in text:
        intent = "OPEN_APP"
        if "chrome" in text:
            entity = "chrome"
        elif "notepad" in text:
            entity = "notepad"
        elif "youtube" in text and "play" not in text: # distinguish from play song
            intent = "OPEN_WEBSITE"
            entity = "youtube"
        elif "github" in text:
            intent = "OPEN_WEBSITE"
            entity = "github"
    elif "search for" in text and "google" in text:
        intent = "SEARCH_GOOGLE"
        # Extract query: remove "search for" and "on google"
        entity = text.replace("search for", "").replace("on google", "").strip()
    elif "time" in text:
        intent = "GET_TIME"
    elif "tell me about" in text or "wikipedia" in text:
        intent = "WIKI_SEARCH"
        if "tell me about" in text:
            entity = text.replace("tell me about", "").replace("from wikipedia", "").strip()
    elif "shutdown" in text:
        intent = "SYSTEM_CONTROL"
        entity = "shutdown"
    elif "restart" in text:
        intent = "SYSTEM_CONTROL"
        entity = "restart"
    elif "play" in text and "youtube" in text:
        intent = "PLAY_SONG"
        entity = text.replace("play", "").replace("on youtube", "").strip()
    elif "exit" in text:
        intent = "EXIT"
    
    return intent, entity
