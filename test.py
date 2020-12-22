import speech_recognition as sr
from time import ctime
import time
import pyttsx3
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def respond(audioString):
    print(audioString)
    engine.say(audioString)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print("Request Failed; {0}".format(e))
    return data
def digital_assistant(data):
    if "how are you" in data:
        listening = True
        respond("I am well")
    elif "what time is it" in data:
        listening = True
        respond(ctime())
    elif 'open youtube' in data:
        listening = True
        respond("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif 'open Google' in data:
        listening = True
        respond("Here you go to Google\n")
        webbrowser.open("google.com")
    elif "stop listening" in data:
        listening = False
        print('Listening stopped')
        return listening
    else:
        listening = True
        respond("Sorry! can you repeat .. ")

    return listening
time.sleep(6)
respond("Hi Farah, what can I do for you?")
listening = True

while listening == True:
    data = listen()
    listening = digital_assistant(data)

