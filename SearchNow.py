import pywhatkit
import wikipedia
import webbrowser



def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query=query.replace("jarvis","")
        query=query.replace("google","")
        query=query.replace("search","")

        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,1)
            print("This is what i found in google "+ result)
            return("This is what i found in google "+ result)

        except:
            print("No content found for given search")
            return("No content found for given search")


def searchYoutube(query):
    if "youtube"in query:
        query=query.replace("youtube","")
        query=query.replace("search","")
        query=query.replace("jarvis","")
        web="https://www.youtube.com/results?search_query="+query
        webbrowser.open(web)
        pywhatkit.playonyt(query)

def searchWikipedia(query):
    if "wikipedia" in query:
        query=query.replace("wikipedia","")
        query=query.replace("search","")
        query=query.replace("jarvis","")
        results=wikipedia.summary(query,sentences=2)
        return("According to Wikipedia...."+results)
