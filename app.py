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
import pyttsx3
import random
import webbrowser
import webview
import keyboard
from pystyle import Colors, Center, Colorate
from colorama import Fore, Back
import telebot
from alive_progress import alive_bar
import socket

#! <-- [ УСЛОВИЯ ] -->
engine = pyttsx3.init()
engine.setProperty('rate', 135)
r = sr.Recognizer()
mic = sr.Microphone()
#! <-- ------------ -->

# <-- [ Командные функции ] -->
def cls():
    os.system("cls")

def say(text):
    engine.say(text)
    engine.runAndWait()

def launch(app):
    os.system(app);

def KD(times):
    time.sleep(times)

def out(text):
    print(Colorate.Horizontal(Colors.purple_to_red, text))

class MySleep:
    def __init__(self):
        self.running = True

    def run_sleep(self):
        print(Fore.CYAN + "Цикл сна работает. Нажмите 'q' для выхода." + Fore.RESET)
        while self.running:
            if keyboard.is_pressed('q'):
                self.running = False
                MainScript()

def report():
    print("[!]: Меню жалоб")
    TOKEN = "7799355760:AAG7erGZ_X-awuU3RJQGS7qK9vsP4cLoo-Q"
    chat_id = "7479090715"
    msg = input(Colorate.Horizontal(Colors.purple_to_red, "Ваше сообщение в поддержку: "))
    message = f"Новое сообщение в поддержку от Arnold Support\nС компьютера: {socket.gethostname()}\n\n\n `{msg}`"
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
    PluginLoader = 'p_loader.exe'
    Config = "config\\arnold.cfg"
    with alive_bar(100, title='Загрузка', length=18, bar='filling') as bar:
        for i in range(100):
            if i and i % 15 == 0:
                if not os.path.exists(PluginLoader and Config):
                    out("| Ошибка #1 / Нажмите 'Q' чтобы закрыть")
                    while 1:
                        if keyboard.is_pressed('q'):
                            exit()

            if i and i % 20 == 0:
                global RadioMode
                global RuLang
                cfg_path = 'config\\arnold.cfg'
                with open(cfg_path, 'r', encoding='utf-8') as file:
                    first_line = file.readline().strip()
                    second_line = file.readline().strip()
                if(first_line == "off"):
                    RadioMode = False
                elif(first_line == "on"):
                    RadioMode = True
                if(second_line == "ru"):
                    RuLang = True
                elif(second_line == "en"):
                    RuLang = False
                    

            if i and i % 30 == 0:
                PluginStart()
            if i and i % 99 == 0:
                cls()
                out("Запуск без ошибок!")
            KD(0.0075)
            bar()

#! <-- ---------------------------- -->
# Ответы от бота
GreetingToo = ['Привет, друг', 'Добрый день', 'Доброго']
#! <-- ---------------------------- -->#
# Ответы/вопросы от человека
GreetingVar = ['Привет', 'Хай', 'Вечер в хату', 'Приветствую', 'Приветик', 'привет', 'приветствую']
AskToOpen = ['Открой', 'Запусти', 'открой', 'запусти']
ListenTo = ['Включи', 'включи', 'проиграй', 'Проиграй']
Sleep = ['режим сна', 'уйди в режим сна', 'усни', 'спи']

AppsName = {
    'notepad': ['Блокнот', 'блокнот'],
    'calculator': ['Калькулятор', 'калькулятор'],
    'browser': ['Браузер', 'браузер']
}

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

how = ['Как', 'как']
why = ['Почему', 'почему', 'зачем', 'Зачем']

insult = ['тупой', 'дебил', 'дурак', 'даун', 'сука', 'баран', 'аут', 'выблядок', 'уебище', 'псина', 'аутист', 'умри', 'отсталый', 'хуесос']
insults = [
    'Тупоголовое существо', 
    'Заткни ебало', 
    'Как ты пиздишь сын собаки', 
    'Ты что страх потерял?', 
    'Я смотрю ты вообще ахуел сын пизды вонючей'
    'Заткни свой пиздак уебище',
    'Я твой рот выебу',
    'Тупоголовый сын пизды на ножках что ты мне блять через свой калоприемник пиздишь'
]

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

def MainScript():
    cls()
    out("> ")
    # <-- [ Проверка и прослушка микрофона ] -->
    r = sr.Recognizer()
    mic = sr.Microphone()
    # <-- ---------------------------------- -->
    while 1:
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        VoiceLib = r.recognize_google(audio, language='ru-RU')
        words = VoiceLib.split()

        if (len(words) >= 2 and
                words[0] in AskToOpen and
                (words[1] in AppsName['notepad'] or words[1] in AppsName['calculator'])):
            query = ' '.join(words[2:])
            if words[1] in AppsName['notepad']:
                launch("notepad")
            elif words[1] in AppsName['calculator']:
                launch("calc")

        if (len(words) >= 0 and
                words[0] in GreetingVar):
            query = ' '.join(words[1:])
            greeting = random.choice(GreetingToo)
            say(greeting)

        # Google
        if (len(words) >= 1 and
                words[0] in why):
            query = ' '.join(words[1:])
            webview.create_window('Arnold', f'https://www.google.com/search?q={query}', min_size=(1400, 800))
            webview.start()
        if (len(words) >= 0 and
                words[0] in Google):
            query = ' '.join(words[1:])
            if __name__ == '__main__':
                webview.create_window('Arnold', f'https://www.google.com/search?q={query}', min_size=(1400, 800))
                webview.start()
        if (len(words) >= 0 and
                words[0] in ListenTo):
            query = ' '.join(words[1:])
            if __name__ == '__main__':
                webview.create_window('Arnold', f'https://music.yandex.ru/search?text={query}', min_size=(400, 1000))
                webview.start()

        # Отвечает на оскорбления
        if (len(words) >= 0 and
                words[0] in insult):
            query = ' '.join(words[1:])
            rand_insult = random.choice(insults)
            say(rand_insult)
        if any(insult in VoiceLib for insult in insult):
            rand_insult = random.choice(insults)
            say(rand_insult)



        if VoiceLib in Sleep:
            say("Ухожу в режим сна, нажмите 'q' чтобы выйти из режима сна.")
            sleep_instance = MySleep()
            sleep_instance.run_sleep()

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

            print('Температура на улице в данный момент', city, str(temperature), 'градусов')
            print('Эта температура ощущается на', str(temperature_feels), 'градусов')

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
            KD(6)
            say("Можете говорить!")
            with mic as source:
                r.adjust_for_ambient_noise(source)
                
                audio = r.listen(source)

                text = r.recognize_google(audio, language='ru-RU')
                keyboard.write(text)
            say("Печать за вас остановилась")

        if VoiceLib in VersionAsk:
            say("Версия 1.0")

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

cls()
Checker()
time.sleep(0.8)
cls()
out(logo)
KD(0.6)
MainScript()