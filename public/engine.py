import speech_recognition as sr
import pyttsx3

def lib_import():
    import pyttsx3
    import speech_recognition as sr

# <=< === Условия === >=>
engine = pyttsx3.init()
engine.setProperty('rate', 145)
r = sr.Recognizer()
mic = sr.Microphone()
# <=< === === === === === === >=>

def say(text):
    engine.say(text)
    engine.runAndWait()

def voice():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    VoiceLib = r.recognize_google(audio, language='ru-RU')

def console(char):
    print(char)