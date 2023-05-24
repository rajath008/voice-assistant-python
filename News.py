import json
import requests
from Main import speak
# dde53a9d9d8a4010b67b56a1b8a45912
def latestNews():
    api_dict={
        "buisness":"https://newsapi.org/v2/top-headlines?country=in&category=buisness&apiKey=dde53a9d9d8a4010b67b56a1b8a45912",
        "entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=dde53a9d9d8a4010b67b56a1b8a45912",
        "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=dde53a9d9d8a4010b67b56a1b8a45912",
        "science":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=dde53a9d9d8a4010b67b56a1b8a45912",
        "technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=dde53a9d9d8a4010b67b56a1b8a45912"
    }

    content=None
    url=None
    field=input("Field of interest for news : ")
    for key,value in api_dict.items():
        if key.lower()in field.lower():
            url=value
            print(url)
            print("url was found")
            break
        else:
            url=True
            if url is True:
                print("url not found")

    news=requests.get(url).text
    news=json.loads(news)
    speak("First News about in the field of "+{field})

    arts=news["articles"]
    for articles in arts:
        article=articles["title"]
        print(article)
        speak(article)
        news_url=article["url"]
        print(f"For more information visit {news_url}")

        a=input("Press 1 to continue or Press 2 to stop")
        if(str(a)==1):
            pass
        elif(str(a)==2):
            break
        
        speak("that's all")

