import pyttsx3
import speech_recognition 
import requests 
import datetime
import keyboard
from bs4 import BeautifulSoup
import os
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query: 
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok mam, u can call me anytime")
                    break  

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "hello" in query:
                    speak("hello how are you?")
                elif "i am fine" in query:
                    speak("that's great")
                elif "who are you" in query:
                    speak("I am your personal assistant. tell me what can i do for you")
                elif "how r u " in query:
                    speak ("perfect ")
                elif "thank you " in query:
                    speak ("your welcome") 

                elif "pause" in query:
                  pyautogui.press("k")
                  speak("video paused")
                elif "play" in query:
                  pyautogui.press("k")             
                  speak("video played")
                elif "mute" in query:
                   pyautogui.press("m")
                   speak("video muted")

                elif "volume up" in query:
                  from keyboard import volumeup
                  speak("Turning volume up,..")
                  volumeup()
                elif "volume down" in query:
                  from keyboard import volumedown
                  speak("Turning volume down, ..")
                  volumedown()

                elif "open" in query:
                  from Dictapp import openappweb
                  openappweb(query)
                elif "close" in query:
                  from Dictapp import closeappweb
                  closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

              



                elif "temperature" in query:
                    search = "temperature in khandwa"
                    url =f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                   search = "temperature in delhi"
                   url = f"https://www.google.com/search?q={search}"
                   r  = requests.get(url)
                   data = bs4 (r.text,"html.parser")
                   temp = data.find("div", class_ = "BNeawe").text
                   speak(f"current{search} is {temp}")
                
                elif "the time" in query:
                 strTime = datetime.datetime.now().strftime("%H:%M")    
                 speak(f" the time is {strTime}")
                elif "finally sleep" in query:
                 speak("Going to sleep... ,Take care ")
                 exit()

