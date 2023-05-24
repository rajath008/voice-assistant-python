import datetime

def getTime(query):
    if "the time" in query:
        strTime=datetime.datetime.now().strftime("%H:%M")
        return strTime