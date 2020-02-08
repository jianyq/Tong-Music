import subprocess
import time
import win32com.client as win
subprocess.Popen("beat.mp3",shell=True).wait()
speak = win.Dispatch("SAPI.SpVoice")
text = open('demo.txt', encoding='UTF8', errors='ignore').read()
text = text.split("\n")
speak.Speak("第一代说唱机器即将开始")
for lines in range(len(text)):
    speak.Speak(text[lines])
    
