import os
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console
just_fix_windows_console()

slash = "папка\имя.exe: "

plugin_name = input(slash)
writeplugin = open("loader.cfg", 'w')
writeplugin.write(plugin_name + '\n')

print("Плагин прописан")

input()