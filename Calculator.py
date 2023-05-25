import wolframalpha
import pyttsx3
from Main import speak

def WolframAlpha(query):
    api="VQRRYV-WJ8UL76UQL"
    requester=wolframalpha.Client(api)
    requested=requester.query(query)

    try:
        answer=next(requested.results).text
        return answer 
    except:
        speak("The value is not answerable")

def Calc(query):
    term=str(query)
    term=term.replace("jarvis","")
    term=term.replace("multiply","*")
    term=term.replace("add","+")
    term=term.replace("plus","+")
    term=term.replace("substract","-")
    term=term.replace("minus","-")
    term=term.replace("divide","/")

    Final=str(term)

    try:
        result=WolframAlpha(Final)
        print(f"{result}")
        speak(result)

    except:
        print("Math error")
        speak("The value is not answerable")


