import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 145)

def say(text):
    engine.say(text)
    engine.runAndWait()