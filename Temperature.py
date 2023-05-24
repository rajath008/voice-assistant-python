# import speech_recognition
# import pyttsx3
import bs4
import requests

# def takeCommand():
#     r=speech_recognition.Recognizer()
#     with speech_recognition.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold=1
#         r.energy_threshold=300
#         audio=r.listen(source,0,4)
#     try:
#         print("Understanding....")
#         query=r.recognize_google(audio,language='en-in')
#         print(f"You said:{query}\n")
#     except Exception as e:
#         print("Say that again please")
#         return "None"
#     return query

# query=takeCommand().lower()
# engine=pyttsx3.init("sapi5")
# voices=engine.getProperty("voices")
# engine.setProperty("voice",voices[0].id)
# engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

def getTemperature(query):
    if "temperature" in query:
        search="temperature in banglore"
        url=f"https://www.google.com/search?q={search}"
        r=requests.get(url)
        data=bs4.BeautifulSoup(r.text,"html.parser")
        temp=data.find("div",class_="BNeawe").text
        return(f"current {search} is {temp}")
        # print(f"current {search} is {temp}")