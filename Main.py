import pyttsx3
import speech_recognition
import os
# import pyaudio

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
# print(voices[0])
engine.setProperty("rate",240)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source,0,4)

    try:
        print("Understanding..")
        query=r.recognize_google(audio,language="en-in")
        print(f"You said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if "wake up" in query:
            from GreetME import greetMe
            greetMe()
            
            while True:
                query=takeCommand().lower()
                if "you can sign off now" in query:
                    speak("Thank you Sir,It was a pleasure to work for you")
                    exit()
                    

                elif ("hello" in query):
                    speak("Hello sir, How are you?") 

                elif"i am fine" in query:
                    speak("that's great sir")

                elif "how are you" in query:
                    speak("I am doing well sir,how about you?")

                elif "thank you"in query:
                    speak("You're welcome sir")
                

                elif "open "in query:
                    from WebsiteApps import openApp
                    speak(f"excecuting {query}")
                    openApp(query)

                elif "close" in query:
                    from WebsiteApps import closeappweb
                    closeappweb(query)
                    speak(f"{query}completed")
                
                elif "google" in query:
                    speak("Searching in google")
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                
                elif "youtube" in query:
                    speak("Searching in youtube")
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                
                elif "wikipedia" in query:
                    speak("Searching in Wikipedia")
                    from SearchNow import searchWikipedia
                    results=searchWikipedia(query)
                    speak(results)
                    print(results)
                
                elif "temperature" in query:
                    from Temperature import getTemperature
                    results=getTemperature(query)
                    speak(results)
                    print(results)

                elif "the time" in  query:
                    from Time import getTime
                    results=getTime(query)
                    print(results)
                    speak(results)

                
                elif "set alarm" in query:
                    speak("Enter the time in terms of Hours and minutes and seconds")
                    t=input("Enter the time in terms of Hours and minutes and seconds : ")
                    from Alarm import setAlarm
                    setAlarm(t)
                    from Alarm import ringAlarm
                    ringAlarm()
                    speak("Alarm set succesfully")

                elif "delete alarm" in query:
                    from Alarm import deleteAlarm
                    deleteAlarm()

                elif "play" in query or "pause" in query or "volume" in query or "mute" in "query":
                    from MediaControls import control
                    control(query)

                elif "remember that " in query:
                    from Reminder import setReminder
                    setReminder(query)
                    speak("reminder set")

                elif "what was the reminder" in query or "what do you remember":
                    from Reminder import getReminder
                    reminder=getReminder()
                    print(reminder)                
                    speak(reminder)

                elif "tired" in query:
                    speak("to relive you from strees here's your favourite song")
                    os.startfile("snowfall.mp3")

                

                
                