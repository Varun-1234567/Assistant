import subprocess
import wolframalpha
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import pyaudio

from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
assname =("Lusi")

def search(e):
    print(e)
    g=e.lower()
    h=(g.lstrip()).strip()
    print(h)
    f=h.replace(" ","")
    f=h.replace(" ","")
    entries=list(os.listdir(r'\\192.168.0.1\d\movies'))
    for i in entries:
        if f in i.lower():
           r=i
           break
        else:
           r=1
           
    if r==1:
        speak("Sir please speak again Sir")
    else:
        print(r) 
        speak("I found it Sir")
        speak('Sir'+r+''+'is now being played')
        b=r"\\192.168.0.1\d\movies/"
        os.startfile(b+r)
        print(r)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendwhat(a,b):
    c="+91"+a
    d=str(c)
    pywhatkit.sendwhatmsg_instantly(d,b)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=3 and hour <12:
        speak('Good Morning Sir I wish you a good day Sir')
    if hour >=12 and hour <18:
        speak('Good afternoon Sir I hope that you had Lunch if not Please have the lunch soon Sir')
    if hour >=18 and hour <21:
        speak('Good Evening Sir I hope that you had snacks if not Please have the snacks soon Sir')
    if hour >=21 and hour <24:
        speak('Good night Sir and have a nice dream Sir')
    if hour >=0 and hour <3:
        speak('It is too late Sir it is time to sleep Sir so Let us take a nap Sir')
  
    assname =("Lusi")
    speak("I am your Personal Assistant")
    speak(assname)
     
def username():
    speak("welcome Sir")
    columns = shutil.get_terminal_size().columns
    uname="Aadhil" 
    print("**********".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("**********".center(columns))
     
    speak("How can i Help you, Sir")
 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio)
        print(f"User  said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('irbanaadhil@gmail.com', 'genocknxpopkwfsy')
    server.sendmail('irbanaadhil@gmail.com', to, content)
    server.quit()

def search_file():
    speak("Please tell me the file or folder name to search for, Sir.")
    query = takeCommand().lower().strip()  # Taking voice input from the user
    if query == "none":
        speak("I couldn't understand. Please try again.")
        return
    
    # Searching for the file in the system
    speak("Searching for the file or folder, Sir...")
    search_results = []
    for root, dirs, files in os.walk("C:\\"):  # Searching through the C: drive (can modify this path)
        for name in files + dirs:
            if query in name.lower():
                search_results.append(os.path.join(root, name))

    if not search_results:
        speak(f"Sir, I couldn't find an exact match for {query}. Please try again.")
    else:
        speak(f"Sir, I found the following locations for {query}:")
        for result in search_results:
            print(result)
            speak(result)

def create_file_or_folder():
    speak("Please tell me if you'd like to create a file or folder.")
    choice = takeCommand().lower().strip()
    
    if choice == 'file':
        speak("Please tell me the file name with extension.")
        file_name = takeCommand().lower().strip()
        path = os.path.join("C:\\", file_name)  # Adjust the path as per requirement
        open(path, 'w').close()  # Create an empty file
        speak(f"Sir, the file {file_name} has been created.")
    
    elif choice == 'folder':
        speak("Please tell me the folder name.")
        folder_name = takeCommand().lower().strip()
        path = os.path.join("C:\\", folder_name)  # Adjust the path as per requirement
        os.makedirs(path)
        speak(f"Sir, the folder {folder_name} has been created.")
    
    else:
        speak("I couldn't understand. Please try again.")

def delete_file_or_folder():
    speak("Please tell me if you'd like to delete a file or folder.")
    choice = takeCommand().lower().strip()
    
    if choice == 'file':
        speak("Please tell me the file name with extension.")
        file_name = takeCommand().lower().strip()
        path = os.path.join("C:\\", file_name)  # Adjust the path as per requirement
        if os.path.exists(path):
            os.remove(path)
            speak(f"Sir, the file {file_name} has been deleted.")
        else:
            speak("Sir, I couldn't find the file. Please try again.")
    
    elif choice == 'folder':
        speak("Please tell me the folder name.")
        folder_name = takeCommand().lower().strip()
        path = os.path.join("C:\\", folder_name)  # Adjust the path as per requirement
        if os.path.exists(path):
            os.rmdir(path)
            speak(f"Sir, the folder {folder_name} has been deleted.")
        else:
            speak("Sir, I couldn't find the folder. Please try again.")
    
    else:
        speak("I couldn't understand. Please try again.")

def rename_file_or_folder():
    speak("Please tell me if you'd like to rename a file or folder.")
    choice = takeCommand().lower().strip()
    
    if choice == 'file':
        speak("Please tell me the current file name with extension.")
        old_name = takeCommand().lower().strip()
        old_path = os.path.join("C:\\", old_name)
        
        if os.path.exists(old_path):
            speak("Please tell me the new file name with extension.")
            new_name = takeCommand().lower().strip()
            new_path = os.path.join("C:\\", new_name)
            os.rename(old_path, new_path)
            speak(f"Sir, the file has been renamed to {new_name}.")
        else:
            speak("Sir, I couldn't find the file. Please try again.")
    
    elif choice == 'folder':
        speak("Please tell me the current folder name.")
        old_name = takeCommand().lower().strip()
        old_path = os.path.join("C:\\", old_name)
        
        if os.path.exists(old_path):
            speak("Please tell me the new folder name.")
            new_name = takeCommand().lower().strip()
            new_path = os.path.join("C:\\", new_name)
            os.rename(old_path, new_path)
            speak(f"Sir, the folder has been renamed to {new_name}.")
        else:
            speak("Sir, I couldn't find the folder. Please try again.")
    
    else:
        speak("I couldn't understand. Please try again.")

def copy_file():
    speak("Please tell me the name of the file you'd like to copy, with the extension.")
    file_name = takeCommand().lower().strip()
    file_path = os.path.join("C:\\", file_name)  # Adjust the path as per requirement
    
    if os.path.exists(file_path):
        speak("Please tell me the destination path where you'd like to copy the file.")
        destination_path = takeCommand().lower().strip()
        shutil.copy(file_path, destination_path)
        speak(f"Sir, the file {file_name} has been copied to {destination_path}.")
    else:
        speak("Sir, I couldn't find the file. Please try again.")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
     
    while True:
         
        query = takeCommand().lower()
         
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia... Sir')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n Sir")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n Sir")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding Sir")
            webbrowser.open("stackoverflow.com")  
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music Sir")
            # music_dir = "G:\\Song"
            music_dir = "c:\\Music"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))
 
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
 
            speak(f"Sir, the time is {strTime}")
 
        elif 'open Whatsapp' in query:
            codePath = r"C:\Users\asus\Downloads\(24) WhatsApp.html"
            os.startfile(codePath)
 
        elif 'email to Dad' in query:
            try:
                speak("What should I say Sir?")
                content = takeCommand()
                to = "istafinj@karunya.edu.in"   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        elif 'whatsapp message to Friend' in query:
            try:
                speak("Sir Please say what to type Sir")
                content=takeCommand()
                sendwhat("9952714690",content)
                speak("Whatsapp message has been sent")
            except Exception as e:
                print(e)
                speak("I am not able to send this whatsapp Message")
        elif 'whatsapp message to suriya' in query:
             try:
                 speak("Sir Please say what to type Sir")
                 content=takeCommand()
                 sendwhat("7418880223",content)
                 speak("Whatsapp message has been sent")
             except Exception as e:
                 print(e)
                 speak("I am not able to send this whatsapp Message")
     
    
        elif 'send a mail' in query:
            try:                   
                
                speak("What should I say Sir?")
                content = takeCommand()
                speak(" To whom should i send Sir")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine Sir")
        
        elif 'not fine' in query or "bad" in query:
            speak("I am so sorry to disturb in this while Sir Shall i play your favourite playlist now Sir to relax you Sir")
            query1=takeCommand()
            if "okay" in query1 or "ok" in query1 or "yes" in query1 or "yeah" in query1:
                 os.startfile(r"C:\Users\RAJHAVEL\Documents\songa.xspf") 
            else:
                break
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me Sir")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            speak("Sir")
            print("My friends call me", assname, "Sir")
 
                elif 'exit' in query or "sleep"in query or "stop" in query:
            speak("Thanks for giving me your time Sir I going to sleep Sir ")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I was created by Aadhil")
             
 
        elif 'joke please' in query:
            speak(pyjokes.get_joke())
             
 
        elif "calculate" in query:
             
 
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
 
        elif 'search' in query or 'play' in query:
             
 
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
        elif "who i am" in query:
            speak("If you talk then definitely your human Sir.")
 
        elif "how you came to world" in query:
            speak("Thanks to Mr Aadhil Sir. further It's a secret")
 
        elif 'kpr presentation' in query:
            speak("opening Power Poiresentation named nt presentation")
            power = r"C:\Users\asus\Downloads\kpr.ppt"
            os.startfile(power)
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses Sir")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Mr Aadhil")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mr Aadhil ")
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully Sir")
 
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'news' in query:
             
 
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                speak("Sir i have found some news for you sir")
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
 
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device Sir")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down Sir")
                subprocess.call('shutdown / p /f')
                 
 
        elif 'clean the recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled Sir")
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Rocky from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("SIr you asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location)
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Rocky Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
 
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating Sir")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out Sir")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

                elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('Hack.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes Sir")
            file = open("Hack.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = '# url after uploading file'
            r = requests.get(url, stream = True)
             
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "Rocky" in query:
             
            wishMe()
            speak("Rocky 1 point 2005 in your service Mister")
            speak(assname)
 
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
             
        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
  
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine Sir, glad you asked about me Sir")
 
        elif "i love you" in query:
            speak("I'm glad you feel that way, but I'm an AI, and I don't have feelings in the same way humans do")
 
        elif "open movie" in query:
            e=query
            f=e.replace("open","")
            d=f.replace("movie","")
            search(d)

        elif 'search file' in query:
            search_file()
        elif 'create' in query:
            create_file_or_folder()
        elif 'delete' in query:
            delete_file_or_folder()
        elif 'rename' in query:
            rename_file_or_folder()
        elif 'copy' in query:
            copy_file()
        elif 'exit' in query:
            speak("Goodbye, Sir!")
            break
        else:
            speak("I didn't understand the command. Please try again.")
 
       
    
   
