from random import random
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit as tube
from time import sleep
import pyjokes

engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate",10)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("Hey Shubhanshu, I am your virtual assistant Samiksha. Please tell me how may i help you")

def takeCommand():
    #It takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Sender_Email','Passowrd')
    server.sendmail('Sender_Email',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Seaching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'music please' in query:
            n=random.randint(0,4)
            music_dir = 'C:\\Users\\Shubhanshu Rai\\Downloads\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[n]))

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak("Sir, the time is"+ strtime)
        
        elif 'open code' in query:
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak('What should i say!')
                content= takeCommand()
                to_recipient_list = ["Recipient_list"]
                sendEmail(to_recipient_list, content)
                speak("Email has beeen sent")
            except Exception as e:
                # print(e)
                speak("Sorry, I'm Not able to Send Email at this moment")

        elif 'play' in query:
            song = query.replace("play", "")
            speak('Playing' + song)
            tube.playonyt(song)

        elif 'date' in query:
            speak("Sorry, I have a Headache")
        
        elif 'are you single' in query:
            speak("Sorry, I am in a relationship with wifi")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'close' in query:
            speak('Quiting Terminal')
            break
    