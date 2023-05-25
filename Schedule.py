from Main import speak,takeCommand
from plyer import notification
from pygame import mixer

def setschedule():
    tasks=[]
    speak("Do you want to clear the old schedule or not")
    # old=str(takeCommand().lower())
    old=str(input("Yes or No"))
    if old=="yes":
        fp=open("schedule.txt","w")
        fp.write(f"")
        fp.close()
        speak("Old tasks cleared")
        speak("Enter the number of tasks")
        n=int(input("Number of tasks : "))
        # i=0
        speak("You may say the tasks now")
        i=0
        for i in range(n):
            tasks.append(takeCommand().lower())
            fp=open("schedule.txt","a")
            # fp.write(f"{i}.{tasks[i]}\n")
            fp.write(f"{tasks[i]}\n")
            i=i+1
            fp.close()
            
        speak("All tasks added to your schedule")
    
    
    elif old=="no":
        
        
        speak("Enter the number of tasks")
        n=int(input("Number of tasks : "))
        # i=0
        speak("You may say the tasks now")
        more=True
        i=0
        for i in range(n):
            tasks.append(takeCommand().lower())
            fp=open("schedule.txt","a")
            # fp.write(f"{i}.{tasks[i]}\n")
            fp.write(f"{tasks[i]}\n")
            i=i+1
            fp.close()
            
        speak("All tasks added to your schedule")


def showSchedule():
    fp=open("schedule.txt","r")
    content=fp.read()
    fp.close()
    mixer.init()
    mixer.music.load("notification.mp3")
    mixer.music.play()
    notification.notify(
        title="My schedule : ",
        message=content,
        timeout=15
    )
    speak(content)
    speak("you fucking lowlife")

