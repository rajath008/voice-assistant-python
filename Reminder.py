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

def deleteReminder():
    remind=open("reminder.txt","w")
    remind.truncate(0)
    remind.close()
