import os
import webbrowser
import pyautogui
from time import sleep

dictApp={"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
def openApp(query):
    if ".com "in query or".co.in"in query or ".org" in query:
        query=query.replace("open","")
        query=query.replace("jarvis","")
        query=query.replace("launch","")
        query=query.replace(" ","")
        webbrowser.open(f"https://wwww.{query}")

    else:
        keys=list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictApp[app]}")



                
def closeappweb(query):
    if "one tab"in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "two tab"in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")

    elif "three tab"in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
    elif "four tab"in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")    
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
    else:
        keys=list(dictApp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictApp[app]}.exe")

