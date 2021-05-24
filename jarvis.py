import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio) :
    engine.say(audio)
    engine.runAndWait()


def wishMe() : 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning Sir !!")

    elif hour>=12 and hour<18 :
        speak("Good Afternoon Sir !")
    else :
        speak("Good Evening Sir!")

speak("I am Alexa sir Please tell me how may i help you ?")



def takeCommand() :

    r = sr.Recognizer()
   # recognizer = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening.....")
        r.pause_threshhold = 45.131
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said : {query} \n")

       
    except Exception as e :
        print(e)

        print ("Say that again please....")
        return "None"
    return query
    
def sendEmail(To,content) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
    


if __name__ == "__main__" :
    wishMe()
while True :
#if 1 :     #(used to run jarvis once)
    query = takeCommand().lower()

    if 'wikipedia' in query :
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to Wikipedia...")
        print(results)
        speak(results)

    elif 'open youtube' in query :
        webbrowser.open("youtube.com")

    elif 'play' in query :
        song = query.replace('play', '')
        speak('playing'+ song)
        pywhatkit.playonyt(song)

    elif 'open google' in query :
        webbrowser.open("google.com")

    elif 'time' in query :
        strTime = datetime.datetime.now().strftime("%I : %M %p ")
        speak(f"Sir the time is{strTime}")
        print(strTime)

    elif 'hello' in query :
        speak("hello how are you sir !")

    elif 'who is your master' in query :
        speak(" Mr madhav is my creator")

    elif 'how are you' in query :
        speak("Im fine sir what about you sir ")

    elif 'good morning' in query :
        speak("Good morning sir, have a great day ahead")

    elif 'good evening ' in query :
        speak("good evening sir good to see you back again")

    elif 'what can you do' in query :
        speak("I can do all tasks which you will say to do")

    elif 'thank you' in query :
        speak("thanks a lot sir hope you enjoyed using me")

    elif 'goodbye' in query :
        speak("bye bye sir take care of yourself. And don't step out of your home")

    elif 'joke' in query :
        speak(pyjokes.get_joke())

    elif 'email to madhav' in query :
        try:
            speak("What should i say ?")
            content = takeCommand()
            to = "madhavyourEmail@gmail.com"
            sendEmail(to, content)
            speak = "Email has been sent !"
        except Exception as e :
            print(e)
            speak("sorry sir I'm unable to send this mail")

        

    
        




    


