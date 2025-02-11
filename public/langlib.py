import time
import speech_recognition as sr
import pyttsx3
import colorama

# <== Условия ==>
engine = pyttsx3.init()
engine.setProperty('rate', 145)
# <== === === ==>

def func(f_name, do):
    f_name(do)

def say(text):
    engine.say(text)
    engine.runAndWait()

def log(text):
    print(text)

def ent(out):
    input(out)

def sob(__class):
    if __class:
        func()