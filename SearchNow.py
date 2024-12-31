import speech_recognition as sr
import pyttsx3
import webbrowser


# Initialize text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(audio):
    """Function to convert text to speech."""
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    """Function to capture voice input and return it as text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4, phrase_time_limit=4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please say it again.")
        return "None"
    except sr.RequestError:
        print("Unable to connect to the speech recognition service.")
        return "None"
    return query.lower()


def searchGoogle(query):
    """Function to open Google and search for the query."""
    speak("Searching on Google...")
    query = query.replace("google", "").replace("search for", "").replace("open", "").strip()
    web = f"https://www.google.com/search?q={query}"
    webbrowser.open(web)
    speak(f"Here are the search results for {query}")


def searchYoutube(query):
    """Function to open YouTube and search for the query."""
    speak("Searching on YouTube...")
    query = query.replace("youtube", "").replace("search for", "").replace("open", "").strip()
    web = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(web)
    speak(f"Here are the search results for {query}")


# Main Program
if __name__ == "__main__":
    while True:
        query = takeCommand()
        if query == "none":
            continue
        elif "google" in query:
            searchGoogle(query)
        elif "youtube" in query:
            searchYoutube(query)
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to handle that. Please try again.")
