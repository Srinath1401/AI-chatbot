import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import requests

    print("Enter text:")
    command = input("Enter text:")
    print(command)
    if 'sing' in command:
        song = command.replace('play','')
        talk('ok playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is: '+time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry I have a headache')
    elif 'are you single' in command:
        talk("Sorry")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'play a movie' in command:
        talk("opening a movie")
        os.startfile("D:\iot\chat bot project\@TamilMob_LinkZz_Ram_Setu_2022_HQ_HDRip_720p_HEVC_Tam_+_Tel_+_Hin.mkv")
    elif 'open eye control mode' in command:
        talk("open eye control mode")
        os.startfile("D:\iot\chat bot project\main.py")
    elif 'open funny program' in command:
        talk("openning funny program")
        os.startfile("D:\iot\chat bot project\volumn_fun.py")
    elif 'record a screen' in command:
        talk("Screen has been recording")
        os.startfile("D:\iot\chat bot project\screen recorder.py")
    elif 'given details of a phone number' in command:
        talk("enter a phone number")
        os.startfile("D:\iot\chat bot project\phone_numbers_tracker.py")
    elif 'turn on the light' in command:
        talk("turning on the light")
        val = requests.get("http://192.168.76.36/5/on")
        print(val.status_code)         
    elif 'turn off the light' in command:
        talk("turning off the light")
        val = requests.get("http://192.168.76.36/5/off")
        print(val.status_code)
    elif 'turn on the fan' in command:
        talk("turning on the fan")
        val = requests.get("http://192.168.76.36/4/on")
        print(val.status_code)
        
    elif 'turn off the fan' in command:
        talk("turning off the fan")
        val = requests.get("http://192.168.76.36/4/off")
        print(val.status_code)
    elif 'Message to srinath' in command:
        talk("Ok, Message sent to  srinath ")
        os.startfile("D:\iot\chat bot project\whatsapp.py")
    
    
   
