import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#texttospeak

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Evening")
    else:
        speak("Good Evening")
    speak("I am Jarvis please tell me how can i help you")


if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("Start cmd")

        elif "open camera" in query:
             cap = cv2.VideoCapture(0)
             while True:
                 ret, frame = cap.read()

                 cv2.imshow('frame', frame)
                 if cv2.waitKey(1) & 0xFF == ord('q'):
                     break

             cap.release()
             cv2.destroyAllWindows()
                 


