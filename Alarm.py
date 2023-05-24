import datetime
import os

def setAlarm(query):
    timehere=open("Alarmtext.txt","w")
    timehere.write(query)
    timehere.close()
    # os.startfile("setalarm.py")

def ringAlarm():
    extractedTime=open("Alarmtext.txt","r+")
    time=extractedTime.read()
    Time=str(time)
    ring(Time)

def deleteAlarm():
    deletetime=open("Alarmtext.txt","r+")
    deletetime.truncate(0)
    deletetime.close()

def ring(time):
    timeset=str(time)
    timenow=timeset.replace("jarvis","")
    timenow=timenow.replace("set an alarm at ","")
    timenow=timenow.replace(" and ",":")
    timenow=timenow.replace(" ",":")
    Alarmtime=str(timenow)
    print(Alarmtime)
    while True:
        currentTime=datetime.datetime.now().strftime("%H:%M:%S")
        if(currentTime==Alarmtime):
            os.startfile("snowfall.mp3")           
        elif currentTime+"00:00:30"==Alarmtime:
            exit()

