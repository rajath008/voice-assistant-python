import pyautogui
from Main import speak
from pynput.keyboard import Key,Controller

from time import sleep
keyboard=Controller()

def volumeup():
    for i in range(5):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumedown():
    for i in range(5):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)  


def control(query):
    if "pause" in query:
        pyautogui.press("k")
        speak("Paused")

    elif "play" in query:
        speak("Playing")
        pyautogui.press("k")

    elif "mute" in query:
        pyautogui.press("m")
        speak("Muted")

    elif "volume up" in query or "increase volume" in query:
        speak("Increasing Volume")
        volumeup()
        
    
    elif "volume down" in query or "decrease volume" in query:
        speak("Decreasing volume")
        volumedown()
