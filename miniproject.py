from __future__ import unicode_literals
import pyttsx3
import speech_recognition as speech
import datetime
import webbrowser
import os
import wikipedia
from googlesearch import search
from bs4 import BeautifulSoup
import youtube_dl
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# using the male voice to change to female voice change the value accordingly..
engine.setProperty('voices', voices[1].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12 :
        speak('Good morning ...')
    elif hour >=12 and hour <=18 :
        speak('Good afternoon ...')
    else :
        speak('Good evening ...')
# takes command from the user ...
def command() :
    a = speech.Recognizer()
    with speech.Microphone() as source :
        print('Listening......')
        a.pause_threshold = 2
        audio = a.listen(source)
        print(audio)
    try :
        print('Understannding ...')
        query = a.recognize_google(audio, language="en-in")
        print(f"user said : {query}\n")
        speak(query)
    except Exception as e:
        print("say that again please...")
        speak("say that again please...")
        return command()        
    return query
# downloading  songs from youtube (mp3/mp4)
def download () :
    video_url = j
    info = youtube_dl.YoutubeDL().extract_info(url = video_url, download = False)
    #print(info)
    #yt = YouTube(video_url)
    #file_name = yt.title
    file_name = f"{info['title']}.mp3"
    #file_name = video_url
    #print(file_name)
    specs = {
        'format' : 'bestaudio/best' ,
        'keepvideo' : False ,
        'outtmpl' : file_name ,
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio' ,
            'preferredcodec' : 'mp3' ,
            'preferredquality' : '192' ,
        }]
    }
    with youtube_dl.YoutubeDL(specs) as ydl :
        ydl.download([info['webpage_url']])

    #subprocess.call(["open", file_name])

if __name__ == "__main__":
    start()
    #speak("This is my first time meeting you , so may i know your name ....")
    #name = command()
    speak("How may i help you ...")
    
    while True :
        query = command().lower()
        if 'wikipedia' in query :
            print(query)
            #speak('Searching wikipedia .....')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query , sentences = 2)
            print(results)
            speak(results) 
        elif 'open youtube' in query :
            print(query)
            webbrowser.open('www.youtube.com')
         
        elif 'open' in query:
            query = query.replace('open',"")
            for j in search(query, tld="com", num=1, stop=1, pause=2): 
                print(j)
                webbrowser.open_new(j)

        elif 'play' in query:
            query = query.replace('play',"")
            url = ('https://www.youtube.com/results?search_query='+query)
            print(url)
            #for j in search(query, tld="com", num=2, stop=1, pause=2): 
                #print(j)
            webbrowser.open_new(url)
            #youtube_dl.YoutubeDL.urlopen(j)
                               
        elif 'transcribe' in query:
            query = query.replace('transcribe', "")
            with open("output.txt", "a") as f:
                print(query, file=f)
            
        elif 'exit' in query :
            sys.exit()
    