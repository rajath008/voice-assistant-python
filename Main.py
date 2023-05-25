import pyttsx3
import speech_recognition
import os
import pyautogui
import speedtest

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
# print(voices[0])
engine.setProperty("rate",170)

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
    commands=open("commands-history.txt","a")
    commands.write(query + "\n")
    return query

if __name__=="__main__":
    
    from Security import lock
    # from UI import play_gif
    # play_gif()
    if lock():
        unlock=True
        while True:
            

            query=takeCommand().lower()
            if unlock:
                from GreetME import greetMe
                greetMe()

                while True:
                    query=takeCommand().lower()
                    if "you can sign off now" in query:
                        speak("Thank you Sir,It was a pleasure to work for you")
                        exit()

                    elif "change password" in query:
                        fp=open("password.txt","w")
                        speak("Tell the new password : ")
                        newpass=takeCommand().lower()
                        fp.truncate(0)
                        fp.close()
                        fp=open("password.txt","a")
                        fp.write(newpass)
                        speak("New Password has been successfully set")
                    
                    elif ("hello" in query):
                        speak("Hello sir, How are you?") 

                    elif"i am fine" in query:
                        speak("that's great sir")

                    elif "how are you" in query:
                        speak("I am doing well sir,how about you?")

                    elif "thank you"in query:
                        speak("You're welcome sir")

                    elif "open" in query and "app" in query:
                        query=query.replace("open","")
                        query=query.replace("app","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")
                    
                    
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
                    
                    
                    elif "play a game" in query or "rock paper scissors" in query:
                        print("inside")
                        from RockPaperScissor import gameplay
                        gameplay()
                    
                    
                    elif "play" in query or "pause" in query or "volume" in query or "mute" in "query":
                        from MediaControls import control
                        control(query)

                    elif "remember that" in query:
                        from Reminder import setReminder
                        setReminder(query)
                        speak("reminder set")

                    elif "what was the reminder" in query or "what do you remember"in query:
                        from Reminder import getReminder
                        reminder=getReminder()
                        print(reminder)                
                        speak(reminder)

                    elif "forget what you remember" in query :
                        from Reminder import deleteReminder
                        deleteReminder()
                        speak("Reminder has been forgotten")

                    elif "tired" in query:
                        speak("to relive you from stress here are some low beats songs")
                        os.startfile("snowfall.mp3")

                    elif "news" in query:
                        from News import latestNews
                        latestNews()

                    elif "calculate" in query:
                        from Calculator import Calc
                        Calc(query)

                    elif "whatsapp" in query:
                        from Whatsapp import sendMessage
                        sendMessage()

                    elif "shutdown" in query or "shut down" in query:
                        speak("Are you sure you want to shut down the system :")
                        sd=takeCommand().lower()
                        if sd=="yes":
                            os.system("shutdown /s /t 1")
                        else:
                            break

                    
                    elif "create my schedule" in query:
                        from Schedule import setschedule
                        setschedule()

                    elif "show my schedule" in query or "what is my schedule"in query:
                        from Schedule import showSchedule
                        showSchedule()

                    elif "internet speed" in query:
                        wifi=speedtest.Speedtest()
                        up=wifi.upload()/1048576
                        down=wifi.download()/1048576
                        print(f"Wifi Upload speed is {up},mbps")
                        speak(f"Wifi Upload speed is {up},mb per second")
                        print(f"Wifi Download speed is {down},mbps")
                        speak(f"Wifi Download speed is {down},mb per second")

                    elif "screenshot" in query:
                        im=pyautogui.screenshot()
                        im.save("Screenshot.jpg")

                    elif "click my photo" in query or "camera" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("Smile please")
                        pyautogui.press("enter")

                    elif "focus mode" in query:
                        a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                        if (a==1):
                            speak("Entering the focus mode....")
                            os.startfile("D:\Programming\Python Devlopment\Jarvis\FocusMode.py")
                            exit()


                        else:
                            pass   

                    elif "show my focus" in query:
                        from FocusGraph import focus_graph
                        focus_graph()

                    elif "translate" in query:
                        from Translator import translategl
                        query = query.replace("jarvis","")
                        query = query.replace("translate","")
                        translategl(query)

    







































    else:
        speak("All Attempts for password have been used you cannot access me anymore")

                

                
                