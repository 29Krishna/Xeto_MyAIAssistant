import sys
import time
import webbrowser
import pyttsx3 #for voice agent creation
import speech_recognition as sr #for speech recognition
import datetime 
import pyautogui #for controlling the system
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
import os
import psutil
import json
import pickle
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences # type: ignore
import random
import numpy as np
import pywhatkit
# # from elevenlabs import generate, play
# from elevenlabs import text_to_speech, play
# from elevenlabs import set_api_key
# from api_key import api_key_data

# set_api_key(api_key_data)

# def  engine_talk(query):
#     audio = text_to_speech(query)
#     play(audio)
    

with open("intents.json") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl","rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl","rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)



#voice assistant
def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    #0-> male 1->female voice
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',1)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    # command from mic
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # for noises
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...", end = "", flush=True)

        # recognizer properties
        r.pause_threshold = 1
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment = 2
        r.energy_threshold = 4000
        r.phrase_time_limit  = 10
        # print(sr.Microphone.list_microphone_names())

        audio = r.listen(source)#listen to the audio from the microphone
    try:
        print("\r", end = "", flush=True)
        print("Recognizing...", end = "", flush=True)
        query = r.recognize_google(audio,language='en-in')
        print("\r", end = "", flush=True)
        print(f"Usesr said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    
    return query

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict ={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    print(day_dict[day])
    return day_dict[day]

def wishMe():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M: %p") #hours mins seconds
    day = cal_day()

    if(hour>=0 and hour<12 and 'AM' in t):
        speak(f"Good Morning! It's {t} on {day}")
    elif(hour>=12 and hour<17 and 'PM' in t):
        speak(f"Good Afternoon! It's {t} on {day}")
    else:
        speak(f"Good Evening! It's {t} on {day}")

def social_media(query):
    if("facebook" in query):
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com/")
    elif("whatsapp" in query):
        speak("Opening Whatsapp")
        webbrowser.open("https://web.whatsapp.com/")
    elif("instagram" in query):
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com/")
    elif("discord" in query):
        speak("Opening Discord")
        webbrowser.open("https://discord.com/")
    elif("twitter" in query):
        speak("Opening Twitter")
        webbrowser.open("https://twitter.com/")
    elif ("youtube" in query):
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif ("telegram" in query):
        speak("Opening Telegram")
        webbrowser.open("https://web.telegram.org/")
    else:
        speak("Sorry, I can't open that")
    return

def schedule():
    timetable = {
        "monday": [
            ("from 8:10-9:00 you have NCC/NSS/Sports"),
            ("from 9:00-9:50 you have Database Modelling and Design by Dr. Meenu Garg"),
            ("from 9:50-10:40 you have Artificial Intelligence by Dr. Tejna Khosla"),
            ("from 10:40-11:30 you have Web Development Using Mern Stack by Dr. Arushi Jain"),
            ("from 11:30-12:20 you have Programming in Python by Dr. Nidhi Sengar"),
            ("from 1:10-2:30 you have PIP LAB by Dr. Nidhi Sengar"),
            ("from 1:40-3:20 you have WD MERN LAB by Dr. Arushi Jain"),
            ("from 3:20-4:10 you have Library/Sports")
        ],
        "tuesday": [
            ("from 8:10-9:00 you have NCC/NSS/Sports"),
            ("from 9:00-10:40 you have AJP LAB by Mr. Nitesh Kr. Wadhera, PIP LAB by Dr. Nidhi Sengar"),
            ("from 10:40-11:30 you have Web Development Using Mern Stack by Dr. Arushi Jain"),
            ("from 11:30-12:20 you have Advanced Java Programming by Mr. Nitesh Wadhera"),
            ("from 1:10-2:30 you have Database Modelling and Design by Dr. Meenu Garg"),
            ("from 2:30-3:20 you have Principles of Management by Dr. Shalini Mishra"),
            ("from 3:20-4:10 you have Artificial Intelligence by Dr. Tejna Khosla")
        ],
        "wednesday": [
            ("from 8:10-9:00 you have NCC/NSS/Sports"),
            ("from 9:00-9:50 you have Programming in Python by Dr. Nidhi Sengar"),
            ("from 9:50-10:40 you have Advanced Java Programming by Mr. Nitesh Wadhera"),
            ("from 10:40-11:30 you have AJP LAB by Dr. Tejna Khosla"),
            ("from 11:30-12:20 you have WD MERN LAB by Dr. Arushi Jain"),
            ("from 12:20-1:10 you have WD MERN LAB by Dr. Arushi Jain"),
            ("from 1:10-2:30 you have Artificial Intelligence by Dr. Tejna Khosla"),
            ("from 2:30-3:20 you have Principles of Management by Dr. Shalini Mishra"),
            ("from 3:20-4:10 you have Library/Sports")
        ],
        "thursday": [
            ("from 8:10-9:00 you have NCC/NSS/Sports"),
            ("from 9:00-9:50 you have Library/Sports"),
            ("from 10:40-11:30 you have AI LAB by Dr. Shallu Bashambu"),
            ("from 11:30-12:20 you have Universal Human Values by Dr. Shalini Mishra"),
            ("from 12:20-1:10 you have Universal Human Values by Dr. Mahim Sharma"),
            ("from 1:10-2:30 you have Advanced Java Programming by Mr. Nitesh Wadhera"),
            ("from 2:30-3:20 you have Web Development Using Mern Stack by Dr. Arushi Jain")
        ],
        "friday": [
            ("from 8:10-9:00 you have NCC/NSS/Sports"),
            ("from 9:00-9:50 you have Database Modelling and Design by Dr. Meenu Garg"),
            ("from 9:50-10:40 you have Programming in Python by Dr. Nidhi Sengar"),
            ("from 10:40-11:30 you have AI LAB by Dr. Bhaskar Kapoor"),
            ("from 11:30-12:20 you have AJP LAB by Ms. Seema Kalonia"),
            ("from 12:20-1:10 you have PIP LAB by Dr. Nidhi Sengar")
        ]
    }
    day = cal_day().lower()
    print(day)
    speak(f"Opening schedule for {day}")
    schedule = timetable[day]
    for i in schedule:
        speak(f"{i[0]} - {i[1]}")
    return

def is_muted():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    return volume.GetMute()

def openApp(query):
    if "calculator" in query:
        speak("opening calculator")
        os.startfile("C:\\Windows\\System32\\calc.exe")
    elif "notepad" in query:
        speak("opening notepad")
        os.startfile("C:\\Windows\\System32\\notepad.exe")
    elif "paint" in query:
        speak("opening paint")
        os.system("start mspaint")
    elif "calendar" in query:
        speak("Opening Calendar")
        os.system("start outlookcal:")
    elif "vscode" in query:
        speak("Opening VS Code")
        os.startfile("C:\\Users\\Divya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")  
        # os.system("start code")
    elif "word" in query:
        speak("Opening Microsoft Word")
        os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    else:
        speak("Sorry, I can't open that")

#for other apps -> will have to run in admin cmd
def close_app(app_name):
    for process in psutil.process_iter():
        if process.name().lower() == app_name.lower():
            process.terminate()
            speak(f"Closed {app_name}")
            return
    speak(f"{app_name} is not running")

def closeApp(query):
    if "calculator" in query:
        speak("Closing calculator")
        os.system('wmic process where name="CalculatorApp.exe" call terminate')
    elif "notepad" in query:
        speak("Closing notepad")
        os.system('wmic process where name="Notepad.exe" call terminate')
    elif "paint" in query:
        close_app("mspaint.exe")

    elif "calendar" in query:
        close_app("ApplicationFrameHost.exe")  # Calendar runs under this

    elif "vscode" in query:
        close_app("Code.exe")

    elif "word" in query:
        close_app("WINWORD.EXE")

def browsing(query):
    speak("what do you want to search?")
    s = command()
    speak("Opening browser")
    pywhatkit.search(f"{s}")

def song(query):
    speak("which song do you want me to play?")
    s = command()
    speak(f"Playing {s} on YouTube")
    pywhatkit.playonyt(s)
    
def condition():
    usage = str(psutil.cpu_percent())
    speak(f"CPU is at {usage} percentage")
    battery = psutil.sensors_battery()
    percentage =battery.percent
    speak(f"battery is at {percentage} percentage")

    if percentage<=40:
        speak("we should connect charger!!")


# speak("Hello I am Xeto, your personal assistant. How can I help you?")
if __name__ == "__main__":
    wishMe()
    # engine_talk("Hello! I am Xeto, your AI-powered virtual assistant. I am designed to understand and respond to your queries using deep learning and natural language processing. Whether you need answers, a joke, or just someone to talk to, I'm here to help! How can I assist you today?")
    while True:
        query = command().lower()
        # query = input("enter your command->")

        #social media 
        if(('facebook' in query) or ('whatsapp' in query) or ('instagram' in query) or ('discord' in query) or ('twitter' in query) or ('youtube' in query) or ('telegram' in query)):
            social_media(query)

        # schedule
        elif (('college time table' in query) or ('schedule' in query) or ("today's time table" in query)):
            schedule()

        # volume
        elif ("volume up" in query or "increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume Increased")
        elif ("volume down" in query or "decrease volume" in query):
            if not is_muted():  # Only unmute if it's muted
                pyautogui.press("volumedown")
                speak("Volume Decreased")
            else:
                speak("Volume is muted")
            
        elif ("volume mute" in query or "mute" in query):
            if not is_muted():  # Only mute if it's not already muted
                pyautogui.press("volumemute")
                speak("Volume muted")
            else:
                speak("Volume is already muted")
        elif ("volume unmute" in query or "unmute" in query):
            if is_muted():  # Only unmute if it's muted
                pyautogui.press("volumemute")
                speak("Volume unmuted")
            else:
                speak("Volume is already unmuted")

        # opening applications
        elif(("open calculator" in query) or ("open notepad" in query) or ("open calendar" in query) or ("open paint" in query) or ("open vscode" in query) or ("open word" in query)):
            openApp(query)
        
        # closing applications
        elif(("close calculator" in query) or ("close notepad" in query) or ("close calendar" in query) or ("close paint" in query) or ("close vscode" in query) or ("close word" in query)):
            closeApp(query)

        elif any(word in query.lower() for word in ["what", "who", "how", "thanks", "hello", "bye", "joke", "time", "date", "day", "haha", "programmer", "insult", "activity", "awesome", "good", "old"]):
            padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), truncating='post', maxlen=20)
            result = model.predict(padded_sequences)
            tag = label_encoder.inverse_transform([np.argmax(result)])

            for i in data['intents']:
                if i['tag'] == tag:
                    response = np.random.choice(i['responses'])
                    print(response)
                    speak(response)

        elif("open browser" in query):
            browsing(query)

        elif("song" in query):
            song(query)

        elif ("system condition" in query) or ("condtion of the system" in query):
            speak("checking the system's condition")
            condition()

        elif "exit" in query:
            sys.exit()
        # print(query)
