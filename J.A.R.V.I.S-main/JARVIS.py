#Jarvis--by team KTMS
import datetime
import json
import os
import sys
import time
import webbrowser
import isort
import numpy as np
import psutil
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import speedtest
import wikipedia
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtCore import QDate, Qt, QTime, QTimer
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pytube import YouTube
from requests import get

from JarvisUi import Ui_JarvisUI

isort.file("JARVIS.py")#to sort Import libraries


VOICES = {
    'en':  'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
    'fr': 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0'
}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',VOICES) 

#Main classs where all the functiona are present
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        self.Intro()
    
    #function that will take the commands  to convert voice into text
    def take_Command(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:

                print('Listening....')
                listener.pause_threshold = 1
                voice = listener.listen(source,timeout=4,phrase_time_limit=7)
                print("Recognizing...")
                command1 = listener.recognize_google(voice,language='en-in') or (listener.recognize_google(voice,language='fr-in'))
                
                command1 = command1.lower()  
                if 'jarvis' in command1: 
                    command1 = command1.replace('jarvis','')
                
            return command1
        except:
            return 'None'
        
    #Jarvis commands controller 
    def run_jarvis(self):
        self.wish()
        self.talk('Hello I am jarvis your assistant. please tell me how can i help you')
        while True:
            self.command = self.take_Command() #Every time taking command after a task is done
            print(self.command)
            if ('play a song' in self.command) or ('youtube' in self.command) or ("download a song" in self.command) or ("download song" in self.command) : 
                #commands for opening youtube, playing a song in youtube, and download a song in youtube
                self.yt(self.command) #function is from line 555
            #Interaction commands with JARVIS
            elif ('your age' in self.command) or ('are you there' in self.command) or ('tell me something' in self.command) or ('thank you' in self.command) or ('in your free time' in self.command) or ('can you hear me' in self.command) or ('do you ever get tired' in self.command):
                self.Fun(self.command)
            elif 'time' in self.command : 
                self.Clock_time(self.command)
            elif (('hi' in self.command) and len(self.command)==2) or ((('heyah' in self.command) or ('hey' in self.command)) and len(self.command)==3) or (('hello' in self.command) and len(self.command)==5):
                self.comum(self.command)
            elif ('what can you do' in self.command) or ('your name' in self.command) or ('my name' in self.command) or ('university name' in self.command):
                self.Fun(self.command)
            elif ('joke'in self.command):
                self.Fun(self.command)
            #It will tell the day Eg : Today is wednesday
            elif ("today" in self.command) or ('date' in self.command):
                day = self.Cal_day()
                self.talk("Today is "+day)
            #command if you don't want the JARVIS to spack until for a certain time
            #Note: I can be silent for max of 10mins
            # Eg: JARVIS keep quiet for 5 minutes 
            elif ('silence' in self.command) or ('silent' in self.command) or ('keep quiet' in self.command) or ('wait for' in self.command) :
                self.silenceTime(self.command)
            #command to search for something in wikipedia
            #Eg: what is meant by python in wikipedia (or) search for "_something_" in wikipedia
            elif ('wikipedia' in self.command) or ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command):
                self.B_S(self.command)
            elif ('open github'in self.command):
                self.open_source(self.command)
            #Command to open desktop applications
            #It can open : caliculator, notepad,paint, teams(aka online classes), discord, spotify, ltspice,vscode(aka editor), steam, VLC media player
            elif ('open calculator'in self.command) or ('open notepad'in self.command) or ('open paint'in self.command) or ('open discord'in self.command):
                self.OpenApp(self.command)
            #Command to close desktop applications
            #It can close : caliculator, notepad,paint, discord, spotify, ltspice,vscode(aka editor), steam, VLC media player
            elif ('close calculator'in self.command) or ('close notepad'in self.command) or ('close paint'in self.command) or ('close discord'in self.command):
                self.CloseApp(self.command)
            #command for opening shopping websites 
            #NOTE: you can add as many websites
            #command for asking your current location
            elif ('where am i' in self.command) or ('where we are' in self.command):
                self.locaiton()
            #command for opening command prompt 
            #Eg: jarvis open command prompt
            elif ('command prompt'in self.command) :
                self.talk('Opening command prompt')
                os.system('start cmd')
            #Command for opening taking screenshot
            #Eg: jarvis take a screenshot
            elif ('take screenshot' in self.command)or ('screenshot' in self.command) or("take a screenshot" in self.command):
                self.scshot()
            #command for increaing the volume in the system
            #Eg: jarvis increase volume
            elif ("volume up" in self.command) or ("increase volume" in self.command):
                pyautogui.press("volumeup")
                self.talk('volume increased')
            #command for decreaseing the volume in the system
            #Eg: jarvis decrease volume
            elif ("volume down" in self.command) or ("decrease volume" in self.command):
                pyautogui.press("volumedown")
                self.talk('volume decreased')
            #Command to mute the system sound
            #Eg: jarvis mute the sound
            elif ("volume mute" in self.command) or ("mute the sound" in self.command) :
                pyautogui.press("volumemute")
                self.talk('volume muted')
            #command for knowing your system IP address
            #Eg: jarvis check my ip address
            elif 'ip address' in self.command:
                ip = get('https://api.ipify.org').text
                print(f"your IP address is {ip}")
                self.talk(f"your IP address is {ip}")
            #command for checking the temperature in surroundings
            #jarvis check the surroundings temperature
            elif ("temperature" in self.command)or("weather" in self.command):
                self.temperature()
            #command for checking internet speed
            #Eg: jarvis check my internet speed
            elif "internet speed" in self.command:
                self.InternetSpeed()
            #command to make the jarvis sleep
            #Eg: jarvis you can sleep now
            elif ("you can sleep" in self.command) or ("sleep now" in self.command):
                self.talk("Okay, I am going to sleep")
                break
            elif("est ce que tu dors" in self.command) :
                self.talk("qui")
            #command for waking the jarvis from sleep
            #jarvis wake up
            elif ("wake up" in self.command) or ("get up" in self.command):
                self.talk("Bruh I am not sleeping i am an AI, what can I do for u")
            elif ("salut" in self.command):
                self.talk("je suis un robot, je ne dors pas")
            #command for exiting jarvis from the program
            #Eg: jarvis goodbye
            elif ("goodbye" in self.command) or ("get lost" in self.command)or("bye bye jarvis" in self.command):
                self.talk("Thanks have a good day")
                sys.exit()
            #command for knowing about your system condition
            #Eg: jarvis what is the system condition
            elif ('system condition' in self.command) or ('condition of the system' in self.command):
                self.talk("checking the system condition")
                self.condition()
            #command for knowing the latest news
            #Eg: jarvis tell me the news
            elif ('tell me news' in self.command) or ("the news" in self.command) or ("todays news" in self.command) or ("News" in self.command):
                self.talk("Please wait,i featching the latest news")
                self.news()
            #command for shutting down the system
            #Eg: jarvis shutdown the system
            elif ('shutdown the system' in self.command) or ('down the system' in self.command):
                self.talk("shutting down the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /s /t 5")
            #command for restarting the system
            #Eg: jarvis restart the system
            elif 'restart the system' in self.command:
                self.talk("restarting the system in 10 seconds")
                time.sleep(10)
                os.system("shutdown /r /t 5")
            #command for make the system sleep
            #Eg: jarvis sleep the system
            elif 'sleep the system' in self.command:
                self.talk("The system is going to sleep")
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")
            
    #Intro msg
    def Intro(self):
        while True:
            self.permission = self.take_Command()
            print(self.permission)
            if ("wake up" in self.permission) or ("get up" in self.permission)or("salut" in self.permission):
                self.run_jarvis()
            elif ("goodbye" in self.permission) or ("get lost" in self.permission):
                self.talk("Thanks for using me, have a good day")
                sys.exit()
                
    #Talk 
    def talk(self,text):
        engine.say(text)
        engine.runAndWait()

    #Wish
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        t = time.strftime("%I:%M %p")
        day = self.Cal_day()
        print(t)
        if (hour>=0) and (hour <=12) and ('AM' in t):
            self.talk(f'Good morning, its {day} and the time is {t}')
        elif (hour >= 12) and (hour <= 16) and ('PM' in t):
            self.talk(f"good afternoon, its {day} and the time is {t}")
        else:
            self.talk(f"good evening, its {day} and the time is {t}")

    #Weather forecast
    def temperature(self):
        IP_Address = get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
        geo_reqeust = get(url)
        geo_data = geo_reqeust.json()
        city = geo_data['city']
        search = f"temperature in {city}"
        url_1 = f"https://www.google.com/search?q={search}"
        r = get(url_1)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        self.talk(f"current {search} is {temp}")
    
  
    #Internet speed
    def InternetSpeed(self):
        self.talk("Wait a few seconds, checking your internet speed")
        st = speedtest.Speedtest()
        dl = st.download()
        dl = dl/(1000000) #converting bytes to megabytes
        up = st.upload()
        up = up/(1000000)
        print(dl,up)
        self.talk(f"we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

    #Communication commands
    def comum(self,command):
        print(command)
        if ('hi'in command) or('heya'in command) or ('hey'in command) or ('hello' in command) :
            self.talk("Hello what can I help for u")
        else :
            self.No_result_found()

    #Fun commands to interact with jarvis
    def Fun(self,command):
        print(command)
        if 'your name' in command:
            self.talk("My name is jarvis")
        elif 'your age' in command:
            self.talk("you did not program me to have a age system")
        elif 'date' in command:
            self.talk('Sorry not intreseted, I am having headache, we will catch up some other time')
        elif 'joke' in command:
            self.talk(pyjokes.get_joke())
        elif 'are you there' in command:
            self.talk('Nah you are speaking with yourself')
        elif 'thank you' in command:
            self.talk('I am here to help you..., your welcome')
        elif 'do you ever get tired' in command:
            self.talk('Yes now stop annoying me')
        else :
            self.No_result_found()

    #Social media accounts commands
    def social(self,command):
        print(command)
        if 'discord' in command:
            self.talk('opening your discord')
            webbrowser.open('https://discord.com/channels/@me')
        else :
            self.No_result_found()
        
    #clock commands
    def Clock_time(self,command):
        print(command)
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        self.talk("Current time is "+time)
    
    #calender day
    def Cal_day(self):
        day = datetime.datetime.today().weekday() + 1
         
        # Data to be written to JSON
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',4: 'Thursday', 5: 'Friday', 6: 'Saturday',7: 'Sunday'}
        
        # Serializing json
        json_object = json.dumps(Day_dict, indent=4)
        

        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            return day_of_the_week
            # Writing to days.json
        
        with open("days.json", "w") as outfile:
	        outfile.write(json_object)
    
        

        
        
     
    
    #Brower Search commands
def B_S(self,command):
        print(command)
        try:
            # ('what is meant by' in self.command) or ('tell me about' in self.command) or ('who the heck is' in self.command)
            if ('wikipedia' in command):
                target1 = command.replace('search for','')
                target1 = target1.replace('in wikipedia','')
            elif('what is meant by' in command):
                target1 = command.replace("what is meant by"," ")
            elif('tell me about' in command):
                target1 = command.replace("tell me about"," ")
            elif('who the heck is' in command):
                target1 = command.replace("who the hell is"," ")
            print("searching....")
            info = wikipedia.summary(target1,5)
            print(info)
            self.talk("According to wikipedia .. "+info)
        except :
            self.No_result_found()
        
    #Browser
def brows(self,command):
        print(command)
        if 'Google' in command:
            self.talk("what should I search on google..")
            S = self.take_Command()#taking command for what to search in google
            
            webbrowser.open(f"{S}")
        elif 'Edge' in command:
            self.talk('opening your Miscrosoft edge')
            os.startfile(r'C:\Users\tgunn\AppData\Local\Microsoft\Edge\Profile')#path for your edge browser application
        else :
            self.No_result_found()
    #youtube
def yt(self,command):
        print(command)
        if 'play' in command:
            self.talk("Yo what's popping what song do you want to hear")
            song = self.take_Command()
            if "play" in song:
                song = song.replace("play","")
            self.talk('playing '+song)
            print(f'playing {song}')
            pywhatkit.playonyt(song)
            print('playing')
        elif "download" in command:
            self.talk("Enter the link first")
            link = input("Enter the YOUTUBE video link: ")
            yt=YouTube(link)
            yt.streams.get_highest_resolution().download()
            self.talk(f"I have downloaded {yt.title} from the link you given")
        elif 'youtube' in command:
            self.talk('opening your youtube')
            webbrowser.open('https://www.youtube.com/')
        else :
            self.No_result_found()
        
    #Github account
def open_source(self,command):
        print(command)
        if 'github' in command:
            self.talk('opening your github')
            webbrowser.open('https://github.com/tushilkumar')
        else :
            self.No_result_found()
    #PC allications
    #note for team  choose correct path//met en path kot zot app eter
def OpenApp(self,command):
        print(command)
        if ('calculator'in command) :
            self.talk('Opening calculator')
            os.startfile('C:\\Windows\\System32\\calc.exe')
        elif ('paint'in command) :
            self.talk('Opening msPaint')
            os.startfile('c:\\Windows\\System32\\mspaint.exe')
        elif ('discord'in command) :
            self.talk('Opening discord')
            os.startfile('c:\\Windows\\System32\\Discord.exe')
        elif ('editor'in command) :
            self.talk('Opening your Visual studio code')
            os.startfile('c\\Windows\\System32\\Code.exe')
        elif ('spotify'in command) :
            self.talk('Opening spotify')
            os.startfile('c.\\Windows\\System32\\Spotify.exe')
        else :
            self.No_result_found()
            
    #closeapplications function
def CloseApp(self,command):
        print(command)
        if (' close calculator'in command) :
            self.talk("okay, closeing caliculator")
            os.system("taskkill /f /im calc.exe")
        elif ('close paint'in command) :
            self.talk("okay, closeing mspaint")
            os.system("taskkill /f /im mspaint.exe")
        elif ('close notepad'in command) :
            self.talk("okay boss, closeing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif ('discord'in command) :
            self.talk("okay, closeing discord")
            os.system("taskkill /f /im Discord.exe")
        elif ('editor'in command) :
            self.talk("okay, closeing vs code")
            os.system("taskkill /f /im Code.exe")
        elif ('spotify'in command) :
            self.talk("okay, closeing spotify")
            os.system("taskkill /f /im Spotify.exe")
        else :
            self.No_result_found()

   
    #Time caliculating algorithm
def silenceTime(self,command):
        print(command)
        x=0
        #caliculating the given time to seconds from the speech commnd string
        if ('10' in command) or ('ten' in command):x=600
        elif '1' in command or ('one' in command):x=60
        elif '2' in command or ('two' in command):x=120
        elif '3' in command or ('three' in command):x=180
        elif '4' in command or ('four' in command):x=240
        elif '5' in command or ('five' in command):x=300
        elif '6' in command or ('six' in command):x=360
        elif '7' in command or ('seven' in command):x=420
        elif '8' in command or ('eight' in command):x=480
        elif '9' in command or ('nine' in command):x=540
        self.silence(x)
        
    #Silence
def silence(self,k):
        t = k
        s = "Ok I will be silent for "+str(t/60)+" minutes"
        self.talk(s)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        self.talk("The "+str(k/60)+" minutes over")

    #location
def locaiton(self):
        self.talk("Wait , let me check")
        try:
            IP_Address = get('https://api.ipify.org').text
            print(IP_Address)
            url = 'https://get.geojs.io/v1/ip/geo/'+IP_Address+'.json'
            print(url)
            geo_reqeust = get(url)
            geo_data = geo_reqeust.json()
            city = geo_data['city']
            state = geo_data['region']
            country = geo_data['country']
            tZ = geo_data['timezone']
            longitude = geo_data['longitude']
            latidute = geo_data['latitude']
            org = geo_data['organization_name']
            print(city+" "+state+" "+country+" "+tZ+" "+longitude+" "+latidute+" "+org)
            self.talk(f"i am not sure, but i think we are in {city} city of {state} state of {country} country")
            self.talk(f"we are in {tZ} timezone the latitude os our location is {latidute}, and the longitude of our location is {longitude}, and we are using {org}\'s network ")
        except Exception as e:
            self.talk("Sorry, due to network issue i am not able to find where we are.")
            pass

    #ScreenShot
def scshot(self):
        self.talk("please tell me the name for this screenshot file")
        name = self.take_Command()
        self.talk("Please hold the screen for few seconds, I am taking screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        self.talk("I am done, the screenshot is saved in the folder.")

    #News
def news(self):
        MAIN_URL_= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=991fc257532d42c7abd896a737dbdac5"
        MAIN_PAGE_ = get(MAIN_URL_).json()
        articles = MAIN_PAGE_["articles"]
        headings=[]
        seq = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth'] #If you need more than ten you can extend it in the list
        for ar in articles:
            headings.append(ar['title'])
        for i in range(len(seq)):
            print(f"todays {seq[i]} news is: {headings[i]}")
            self.talk(f"todays {seq[i]} news is: {headings[i]}")
        self.talk("I have read you the latest news bye now")

    #System condition
def condition(self):
        usage = str(psutil.cpu_percent())
        self.talk("CPU is at"+usage+" percentage")
        battray = psutil.sensors_battery()
        percentage = battray.percent
        self.talk(f"our system have {percentage} percentage Battery")
        if percentage >=75:
            self.talk(f"we could have enough charging to continue our work")
        elif percentage >=40 and percentage <=75:
            self.talk(f"we should connect out system to charging point to charge our battery")
        elif percentage >=15 and percentage <=30:
            self.talk(f"we don't have enough power to work, please connect to charging")
        else:
            self.talk(f"we have very low power, please connect to charging otherwise the system will shutdown very soon")
        
    #no result found
def No_result_found(self):
        self.talk('I couldn\'t understand, could you please say it again.')        

startExecution = MainThread()
class Main(QMainWindow):
    cpath =""
    
    def __init__(self,path):
        self.cpath = path
        super().__init__()
        self.ui = Ui_JarvisUI(path=current_path)
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.startTask)
        self.ui.pushButton_3.clicked.connect(self.close)
       
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\gif.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()        
        self.ui.movie = QtGui.QMovie(rf"{self.cpath}\UI\lines1.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

current_path = os.getcwd()
app = QApplication(sys.argv)
jarvis = Main(path=current_path)
jarvis.show()
exit(app.exec_())