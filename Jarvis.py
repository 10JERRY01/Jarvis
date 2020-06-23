import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


#Jarvis_Speak__Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Wish_the_user_Function
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis your personal AI. How may i help u?")

#Take_input_query_from_user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query

#sendEmail function
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    f= open('C:\\Users\\KIIT\\Documents\\ppxt.txt','r')
    server.login('rd324278@gmail.com',f.read())
    server.sendmail('rd324278@gmail.com',to,content)
    server.close()





if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        #Wikipedia_Information
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        #Web_Browser
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        #Play_Music
        elif 'play music' in query:
            
            path = 'D:\\Music 2'
            files = os.listdir(path)
            d = random.choice(files)
            os.startfile(os.path.join(path,d))

        


        #Open_Pycharm
        elif 'open pycharm' in query:
            pycharmpath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.3\\bin\\pycharm64.exe"
            os.startfile(pycharmpath)

        #Open spotify
        elif 'open spotify' in query:
            spotifypath = "C:\\Users\\KIIT\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifypath)


        #Sending_Emails

        elif 'email to jerry' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "rforrahul.rd@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, my friend i am not able to send this email")

