import time
from app import VoiceLib

time_log = (time.strftime('%H:%M:%S', time.localtime()))

f = open('logs.txt', 'w')
f.write(str(time_log) + ': ' + VoiceLib + '\n')
f.close()