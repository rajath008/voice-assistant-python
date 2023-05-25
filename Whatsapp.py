from Main import speak
from bs4 import BeautifulSoup 
from time import sleep
import datetime
import pywhatkit
import timedelta

strTime=int(datetime.datetime.now().strftime("%H"))
update=int((datetime.datetime.now()).strftime("%H"))
def sendMessage():
    print("Who do you want to send the message :\n")
    speak("Who do you want to send the message ")
    print("1.Amma : 8123905369 \n")
    print("1.Me : 8660471512 ")
    a=int(input("\nEnter choice : "))
    if a==1:

        msg=str(input("What's the message :"))
        speak("What's the message")
        pywhatkit.sendwhatmsg("+918123905369",msg,time_hour=strTime,time_min=update)
    elif a==2:
        pass


