# text to speech function taken from internet
import pyttsx3


def speak(arg):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[10].id)
    engine.say(arg)
    engine.runAndWait()


speak("This is the automation of youtube ,which is created ,by Mahir.")
