import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5') #for getting voice
voices=engine.getProperty('voices')
#print(voices[1].id) #for frmale voice
engine.setProperty('voice', voices[1].id ) #setting voice here mail(0) or female(1)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, This is Zira. How may i help you?")

def takecommand():
    """
    takes microphone input from the user and returns string output 
    """
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold=1 # seconds of non-speaking audio before a phrase is considered complete
        audio=r.listen(source)

    try:
        print("Recognizng........")
        query=r.recognize_google(audio, Language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please!")
        return "None"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    if 1:
        query=takecommand().lower() #lower string
        #logic for executiong task based on query
        if 'wikipedia' in query:
            speak("searching wikipedia.......")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:  #impoerting webbrowser for opening utube
            webbrowser.open("youtube.com")

        elif 'open google' in query:  
            webbrowser.open("google.com")

        elif 'paly music' in query:
            music_dir= 'C:\\song'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\Users\Nikki\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        #For sending emails
        elif 'email to neli' in query:
            try:
                speak("What should i say?")
                content=takecommand()
                to="neliyourEmail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, didn't find the mail!")
        """elif 'quit' in query:
            takecommand.exit()  #add more functionality RUN THIS IN ANOTHER SYSTEM"""


            
