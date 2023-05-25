from Main import speak,takeCommand
def lock():
    speak("Hello its your assistant,what's the password")
    for i in range(3):
        password =str(input("Enter the password : "))
        fp=open("password.txt","r")
        pd=fp.read()
        if(pd==password):
            return True
        else:
            speak(f"incorrect password still {3-i-1} attempts remaining")
    return False    