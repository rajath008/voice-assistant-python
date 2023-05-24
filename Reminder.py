def setReminder(query):
    remindermsg=query.replace("remember that","")
    remindermsg=remindermsg.replace("jarvis","")
    remind=open("reminder.txt","a")
    remind.write(remindermsg)
    remind.close()


def getReminder():
    remind=open("reminder.txt","r")
    msg=remind.read()
    remind.close()
    return(f"I remember that {msg}")
