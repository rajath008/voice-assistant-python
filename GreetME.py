import pyttsx3
import datetime
import pyaudio

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=5 and hour<=12:
        speak("Good Morning ,Sir")
    elif hour>12 and hour<=17:
        speak("Good Afternoon ,Sir")
    elif hour>17 and hour<=19:
        speak("Good Evening ,Sir")
    else:
        speak("Good Night ,Sir")
    
    speak("Please tell me,How Can I help you?")
