# PIP
# pip install pyaudio
# pip install SpeechRecognition
# pip install googletrans
# pip install keyboard
# pip install pyttsx3

# from googletrans import Translator

import speech_recognition as sr
import requests
import os
import time
import random
import pyttsx3
import random
import webbrowser
import webview
import keyboard
from pystyle import Colors, Center, Colorate
# import log
import telebot
from alive_progress import alive_bar

#! <-- [ УСЛОВИЯ ] -->
engine = pyttsx3.init()
engine.setProperty('rate', 145)
# translator = Translator()
#! <-- ------------ -->

# <-- [ Командные функции ] -->
def cls():
    os.system("cls")

def say(text):
    engine.say(text)
    engine.runAndWait()

def KD(times):
    time.sleep(times)

def out(text):
    print(Colorate.Horizontal(Colors.purple_to_red, text))

def report():
    print("[!]: Меню жалоб")
    TOKEN = ""
    chat_id = ""
    msg = input(Colorate.Horizontal(Colors.purple_to_red, "Ваше сообщение в поддержку: "))
    message = f"Новое сообщение в поддержку от Arnold Support\n > {msg}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown"
    response = requests.get(url)
    print("Сообщение в поддержку отправлено")
    KD(2)
    cls()

def calc():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    VoiceLib = r.recognize_google(audio, language='ru-RU')
    out(f"{VoiceLib}")
    if VoiceLib == 'калькулятор':
        out("Первое число")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        n_one = r.recognize_google(audio, language='ru-RU')
        out("Второе число")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        n_two = r.recognize_google(audio, language='ru-RU')
        out("Что сделать?")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        var = r.recognize_google(audio, language='ru-RU')
        if var == "cложить":
            out(int(n_one) + int(n_two))
        if var == "вычесть":
            say(int(n_one) - int(n_two))
        if var == "умножить":
            out(int(n_one) * int(n_two))
        if var == "поделить":
            out(int(n_one) / int(n_two))


def PluginStart():
    os.system(r'p_loader.exe')

def Checker():
    with alive_bar(100) as bar:
        for i in range(100):

            if i and i % 20 == 0:
                PluginStart()
            KD(0.01)
            bar()

GreetingVar = ['Привет', 'Хай', 'Вечер в хату', 'Приветствую', 'Приветик']


AskToOpen = ['Открой', 'Запусти']
AppsName = ['Блокнот', 'блокнот', 'калькулятор']
WhatWeather = ['Какая погода', 'какая погода', 'погода', 'Погода']
HowAreYou = ["Как ты", "Как дела", "Как жизнь"]
BreakList = ["Пока", "Выключись", "Отключись", "До встречи"]
VersionAsk = ['Какая версия', 'Версия', 'Какая у тебя версия', 'Какой ты версии']
WhoYourCreator = ['Кто тебя создал', 'Где тебя создали', 'Как тебя зовут']
TimeAsk = ['Который час', 'Какой час', 'Сколько время', 'Какое время', 'Сколько часов']
GamesReact = ['Давай поиграем', 'Игра', 'Игры']
Games = ['Угадай число', 'Слова']
YoutubeOpen = ['Открой YouTube', 'Запусти YouTube', 'YouTube']
BoredHand = ['Напиши за меня', 'Пиши за меня', 'пиши за меня', 'Диктую', 'диктую', 'ручка', 'Ручка']
Google = ['Погугли', 'загугли', 'Загугли']
ReportReact = ['Репорт', 'репорт', 'Оставить репорт', 'поддержка', 'Поддержка']
update = ['Обновление', 'Обновись', 'Обновить']
calcul = ['калькулятор', 'Калькулятор']
#! <-- ---------------------------- -->

logo = """
                                        
                   **.                  
                  :@@-                  
         ..       :@@-       ..         
        .@@:      :@@-      .@@:        
        :@@-  ::  :@@-  ::  :@@-        
        :@@- :@@: :@@- :@@: :@@-        
    -=  :@@- :@@- :@@- :@@- :@@-  -=    
   :@@- :@@- :@@- :@@- :@@- :@@- :@@-   
   :@@- :@@- :@@- :@@- :@@- :@@- :@@-   
   :@@- :@@- :@@- :@@- :@@- :@@- :@@-   
   :@@- :@@- :@@- :@@- :@@- :@@- :@@-   
   .@@: :@@- :@@- :@@- :@@- :@@- .@@:   
        :@@- :@@- :@@- :@@- :@@-        
        :@@- .@@: :@@- .@@: :@@-        
        :@@-      :@@-      :@@-        
        .%%.      :@@-      .%%.        
                  :@@-                  
                   *#.                 
"""

Checker()
time.sleep(5)
cls()
out(logo)
KD(3)
cls()
KD(1.5)
out("Арнольд вас слушает (by TheScarecr0w)")

# <-- [ Проверка и прослушка микрофона ] -->
r = sr.Recognizer()
mic = sr.Microphone()
# <-- ---------------------------------- -->

while 1:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    VoiceLib = r.recognize_google(audio, language='ru-RU')


    
    if VoiceLib in GreetingVar:
        say(f"И тебе {VoiceLib}")
    elif VoiceLib == "Здравствуйте" and "Здравствуй":
        say(f"{VoiceLib}")

    if VoiceLib in TimeAsk:
        say(time.strftime('%H:%M', time.localtime()))
        out(time.strftime('%H:%M', time.localtime()))

    if VoiceLib in calcul:
        calc()

    if VoiceLib in WhatWeather:
        say("Скажите город")
        
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        city = r.recognize_google(audio, language='ru-RU')
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'

        weather_data = requests.get(url).json()

        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])

        out('Температура на улице в данный момент', city, str(temperature), 'градусов')
        out('Эта температура ощущается на', str(temperature_feels), 'градусов')

    if VoiceLib in YoutubeOpen:
        webview.create_window('Arnold', 'https://youtube.com')
        webview.start()
    
    if VoiceLib in ReportReact:
        report()

    if VoiceLib in update:
        webbrowser.open()

    if VoiceLib in BoredHand:
        r = sr.Recognizer()
        mic = sr.Microphone()

        say("У вас есть 10 секунд чтобы выбрать поле ввода. \n(работает на один ввод, дальше повторная команда)")
        KD(8)
        say("Можете говорить!")
        with mic as source:
            r.adjust_for_ambient_noise(source)
            
            audio = r.listen(source)

            text = r.recognize_google(audio, language='ru-RU')
            keyboard.write(text)
        say("Печать за вас остановилась")

    if VoiceLib in Google:
        say('Что загуглить?')
        with mic as sourcer:
            r.adjust_for_ambient_noise(sourcer)
            audio = r.listen(sourcer)
        GoogleAsk = r.recognize_google(audio, language='ru-RU')
        webview.create_window('Arnold', f'https://www.google.com/search?q={GoogleAsk}')
        webview.start()

    if VoiceLib in AskToOpen + AppsName:
        os.system('notepad.exe')

    if VoiceLib in VersionAsk:
        say("Версия 1.0")

    #! <-- [ Переводчик в разработке ] -->
    # if VoiceLib == "Переведи":
    #     print('Скажите слово которое нужно перевести на английский')
    #     with mic as source:
    #         r.adjust_for_ambient_noise(source)
    #         audio = r.listen(source)
    #     YourTranslateWord = r.recognize_google(audio, language='ru-RU')
    #     Translater(word=YourTranslateWord)

    if VoiceLib in WhoYourCreator:
        say("Я создан TheScarecr0w'ом")

    if VoiceLib in HowAreYou:
        random_answer = ['1', '2', '3']
        random_choose = random.choice(random_answer)
        if random_choose == "1":
            say("У меня все хорошо")
        if random_choose == "2":
            say("Все отлично")
        else:
            say("Пока работаю")
    
    if VoiceLib in BreakList:
        say("До встречи друг, я выключусь через 3 секунды.")
        KD(3)
        exit(0)
        