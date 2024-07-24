from __future__ import print_function
import speech_recognition as sr
import os
import time
from gtts import gTTS
import datetime
import pyjokes
import warnings
import webbrowser
import calendar
import pyttsx3
import random
import smtplib
import wikipedia
import playsound
import wolframalpha
import requests
import json
import winshell
import subprocess
import ctypes
from twilio.rest import Client
import pickle
import os.path

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from selenium import webdriver
from time import sleep

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return data


def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)



def call(text):
    action_call = "assistant"

    text = text.lower()

    if action_call in text:
        return True

    return False


def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."


def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello"]

    response = ["howdy", "whats good", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login("shahil.ks011@gmail.com", "godcoder#1")
    server.sendmail("shahil.ks011@gmail.com", to, content)
    server.close()


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


# def google_calendar():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists("token.json"):
#         creds = Credentials.from_authorized_user_file("token.json", SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 "credentials.json", SCOPES
#             )
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open("token.json", "w") as token:
#             token.write(creds.to_json())
#
#     try:
#         service = build("calendar", "v3", credentials=creds)
#
#     finally:
#         talk("Could not connect to the local wifi network. Please try again later.")
#         exit()
#
#
# def calendar_events(num, service):
#     talk(f'Hey there! Good Day. Hope you are doing fine. These are the events to do today')
#     # Call the Calendar API
#     now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
#     print("Getting the upcoming 10 events")
#     events_result = (
#         service.events()
#         .list(
#             calendarId="primary",
#             timeMin=now,
#             maxResults=10,
#             singleEvents=True,
#             orderBy="startTime",
#         )
#         .execute()
#     )
#     events = events_result.get("items", [])
#
#
# if not events:
#         talk('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         events_today = (event['summary'])
#         start_time = str(start.split("T")[1].split("-")[0])  # get the hour the event starts
#         if int(start_time.split(":")[0]) < 12:  # if the event is in the morning
#             start_time = start_time + "am"
#         else:
#             start_time = str(int(start_time.split(":")[0]) - 12)  # convert 24 hour time to regular
#             start_time = start_time + "pm"
#         talk(f'{events_today} at {start_time}')
#
#
# try:
#     service = google_calendar()
#     calendar_events(10, service)
# except:
#     talk("Could not connect to the local wifi network. Please try again later.")
#     exit()


# def pizza():
#     driver = webdriver.Chrome(
#         r"C:\...\chromedriver.exe"  # Location of your webdriver
#     )
#     driver.maximize_window()  # Maximizes the browser window
#
#     talk("Opening Dominos")
#     driver.get('https://www.dominos.co.in/')  # Open the site
#     sleep(2)
#
#     talk("Getting ready to order")
#     driver.find_element_by_link_text('ORDER ONLINE NOW').click()  # Click on order now button
#     sleep(2)
#
#     talk("Finding your location")
#     driver.find_element_by_class_name('srch-cnt-srch-inpt').click()  # Click on the location search
#     sleep(2)
#
#     location = ""  # Enter your location
#
#     talk("Entering your location")
#     driver.find_element_by_xpath(
#         '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(
#         location)  # Send text to location search input field
#     sleep(2)
#
#     driver.find_element_by_xpath(
#         '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]').click()  # Select the location from suggestions
#     sleep(2)
#
#     try:
#         driver.find_element_by_xpath(
#             '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]').click()  # Click on login button
#         sleep(2)
#     except:
#         talk("Your location could not be found. Please try again later.")
#         exit()
#
#     talk("Logging in")
#     phone_num = ""  # Enter your phone number here
#
#     driver.find_element_by_xpath(
#         '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
#         phone_num)  # Send text to phone number input field
#     sleep(2)
#
#     driver.find_element_by_xpath(
#         '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
#     sleep(2)
#
#     talk("What is your O T P? ")
#     sleep(3)
#
#     otp_log = rec_audio()
#
#     driver.find_element_by_xpath(
#         '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
#         otp_log)  # Paste the OTP into the text field
#     sleep(2)
#
#     driver.find_element_by_xpath(
#         '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()  # Submit OTP
#     sleep(2)
#
#     talk("Do you want me to order from your favorites?")
#     query_fav = rec_audio()
#
#     if "yes" in query_fav:
#         try:
#             driver.find_element_by_xpath(
#                 '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span').click()  # Add your favorite pizza
#             sleep(1)
#         except:
#             talk("The entered OTP is incorrect.")
#             exit()
#
#         talk("Adding your favorites to cart")
#         talk("Do you want me to add extra cheese to your pizza?")
#         ex_cheese = rec_audio()
#         if "yes" in ex_cheese:
#             talk("Extra cheese added")
#             driver.find_element_by_xpath(
#                 '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button').click()  # Add extra cheese
#         elif "no" in ex_cheese:
#             driver.find_element_by_xpath(
#                 '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
#         else:
#             talk("I dont know that")
#             driver.find_element_by_xpath(
#                 '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
#
#         driver.find_element_by_xpath(
#             '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button').click()  # Add a pepsi
#         sleep(1)
#
#         talk("Would you like to increase the qty?")
#         qty = rec_audio()
#         qty_pizza = 0
#         qty_pepsi = 0
#         if "yes" in qty:
#             talk("Would you like to increase the quantity of pizza?")
#             wh_qty = rec_audio()
#             if "yes" in wh_qty:
#                 talk("How many more pizzas would you like to add? ")
#                 try:
#                     qty_pizza = rec_audio()
#                     qty_pizza = int(qty_pizza)
#                     if qty_pizza > 0:
#                         talk_piz = f"Adding {qty_pizza} more pizzas"
#                         talk(talk_piz)
#                         for i in range(qty_pizza):
#                             driver.find_element_by_xpath(
#                                 '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]').click()
#                 except:
#                     talk("I dont know that.")
#             else:
#                 pass
#
#             talk("Would you like to increase the quantity of pepsi?")
#             pep_qty = rec_audio()
#             if "yes" in pep_qty:
#                 talk("How many more pepsis would you like to add? ")
#                 try:
#                     qty_pepsi = rec_audio()
#                     qty_pepsi = int(qty_pepsi)
#                     if qty_pepsi > 0:
#                         talk_pep = f"Adding {qty_pepsi} more pepsis"
#                         talk(talk_pep)
#                         for i in range(qty_pepsi):
#                             driver.find_element_by_xpath(
#                                 '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]').click()
#                 except:
#                     talk("I dont know that.")
#             else:
#                 pass
#
#         elif "no" in qty:
#             pass
#
#         total_pizza = qty_pizza + 1
#         total_pepsi = qty_pepsi + 1
#         tell_num = f"This is your list of order. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
#         talk(tell_num)
#         check_order = rec_audio()
#         if "yes" in check_order:
#             talk("Checking out")
#             driver.find_element_by_xpath(
#                 '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()  # Click on checkout button
#             sleep(1)
#             total = driver.find_element_by_xpath(
#                 '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[6]/span[2]/span')
#             total_price = f'total price is {total.text}'
#             talk(total_price)
#             sleep(1)
#         else:
#             exit()
#
#         talk("Placing your order")
#         driver.find_element_by_xpath(
#             '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[8]/button').click()  # Click on place order button
#         sleep(2)
#
#         talk("Saving your location")
#         driver.find_element_by_xpath(
#             '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()  # Save your location
#         sleep(2)
#
#         talk("Do you want to confirm your order?")
#         confirm = rec_audio()
#         if "yes" in confirm:
#             try:
#                 driver.find_element_by_xpath(
#                     '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
#                 sleep(2)
#             except:
#                 talk("The store is currently offline.")
#                 exit()
#
#             talk("Placing your order")
#
#             talk("Your order is places successfully. Wait for Dominos to deliver your order. Enjoy your day!")
#         else:
#             exit()
#
#     else:
#         exit()


while True:

    try:
        text = rec_audio()
        speak = ""

        if call(text):

            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today
            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)



            elif "what is the weather in" in text:
                key = "08c0e85682ca571f8704df518e9af27c"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                ind = text.split().index("in")
                location = text.split()[ind + 1:]
                location = "".join(location)
                url = weather_url + "appid=" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "404":
                    weather = js["main"]
                    temperature = weather["temp"]
                    temperature = temperature - 273.15
                    humidity = weather["humidity"]
                    desc = js["weather"][0]["description"]
                    weatherResponse = " The temperature in Celcius is " + str(temperature) + " The humidity is " + str(
                        humidity) + " and The weather description is " + str(desc)
                    speak = speak + weatherResponse
                else:
                    speak = speak + "City Not Found"

            elif "who are you" in text or "define yourself" in text:
                speak = speak + "Hello, I am an Assistant. Your Assistant. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera"

            elif "who made you" in text or "created you" in text or " kon bnaya tumko " in text or " tumhe kisne bnaya " in text:
                speak = speak + "I was created by Sahil Singh"

            elif "who is Sahil" in text or "who is sahil" in text:
                speak = speak + "Sahil is a student of Electronics and Communication Engineering at Lovely Delhi technological University. He is a passionate coder and a tech enthusiast."

            elif "who is your creator" in text or "who is your developer" in text:
                speak = speak + "My creator is Sahil Singh"

            elif "who is your father" in text or "who is your dad" in text:
                speak = speak + "My father is Sanjay kumar mukul"

            elif "who is your mother" in text or "who is your mom" in text:
                speak = speak + "My mother is Soni kumari"

            elif "who is your brother" in text or "who is your bro" in text:
                speak = speak + "My brother is Shahil Kumar Singh"

            elif "who is your sister" in text or "who is your sis" in text:
                speak = speak + "My sister is Shalini Kumari"

            elif "who is your friend" in text or "who is your buddy" in text:
                speak = speak + "My friend is Sahil Kumar Singh"

            elif "who is your enemy" in text or "who is your rival" in text:
                speak = speak + "No one, I am a friendly AI"

            elif "who is your best friend" in text or "who is your best buddy" in text:
                speak = speak + "My best friend is Sahil Kumar Singh"

            elif "who is your crush" in text or "who is your love" in text:
                speak = speak + "I am an AI, I don't have any crush"

            elif "who is your girlfriend" in text or "who is your wife" in text:
                speak = speak + "I am an AI, I don't have any girlfriend or wife"

            elif "who is your boyfriend" in text or "who is your husband" in text:
                speak = speak + "I am an AI, I don't have any boyfriend or husband"

            elif "who is your teacher" in text or "who is your mentor" in text:
                speak = speak + "My teacher is Sahil Singh"

            elif "who is your student" in text or "who is your pupil" in text:
                speak = speak + "I am an AI, I don't have any student or pupil"

            elif "who is your boss" in text or "who is your master" in text:
                speak = speak + "My boss is Sahil Singh"

            elif "who is your employee" in text or "who is your worker" in text:
                speak = speak + "I am an AI, I don't have any employee or worker"

            elif("who is your servant" in text or "who is your slave" in text):
                speak = speak + "I am an AI, I don't have any servant or slave"

            elif "who is your customer" in text or "who is your client" in text:
                speak = speak + "I am an AI, I don't have any customer or client"

            elif "who is your fan" in text or "who is your follower" in text:
                speak = speak + "I am an AI, I don't have any fan or follower"






            elif "your name" in text:
                speak = speak + "My name is Assistant"

            elif "who am I" in text:
                speak = speak + "You must probably be a human"

            elif "why do you exist" in text or "why did you come to this word" in text:
                speak = speak + "It is a secret"

            elif "how are you" in text:
                speak = speak + "I am awesome, Thank you"
                speak = speak + "\nHow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that your fine"

            elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
                talk("for how many seconds do you want me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + " seconds completed. Now you can ask me anything"

            elif "change background" in text or "change wallpaper" in text:
                img = r"Gallery\Wallpapers"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background changed successfully"

            elif "open notepad" in text:
                speak = speak + "Opening Notepad"
                os.system("notepad")

            elif "open command prompt" in text:
                speak = speak + "Opening Command Prompt"
                os.system("cmd")

            elif "open camera" in text:
                speak = speak + "Opening Camera"
                os.system("start microsoft.windows.camera:")

            elif "open calculator" in text:
                speak = speak + "Opening Calculator"
                os.system("calc")

            elif "open paint" in text:
                speak = speak + "Opening Paint"
                os.system("mspaint")

            elif "open file explorer" in text:
                speak = speak + "Opening File Explorer"
                os.system("explorer")

            elif "open settings" in text:
                speak = speak + "Opening Settings"
                os.system("start ms-settings:")

            elif "open task manager" in text:
                speak = speak + "Opening Task Manager"
                os.system("taskmgr")

            elif "open control panel" in text:
                speak = speak + "Opening Control Panel"
                os.system("control")

            elif "open device manager" in text:
                speak = speak + "Opening Device Manager"
                os.system("devmgmt.msc")

            elif "open registry editor" in text:
                speak = speak + "Opening Registry Editor"
                os.system("regedit")

            elif "open system information" in text:
                speak = speak + "Opening System Information"
                os.system("msinfo32")

            elif "open event viewer" in text:
                speak = speak + "Opening Event Viewer"
                os.system("eventvwr")

            elif "open disk management" in text:
                speak = speak + "Opening Disk Management"
                os.system("diskmgmt.msc")

            elif("open whatsapp" in text):
                speak = speak + "Opening Whatsapp"
                os.startfile(r"C:\...\WhatsApp.exe")

            elif "open zoom" in text:
                speak = speak + "Opening Zoom"
                os.startfile(r"C:\...\Zoom.exe")

            elif "open telegram" in text:
                speak = speak + "Opening Telegram"
                os.startfile(r"C:\...\Telegram.exe")

            elif "open discord" in text:
                speak = speak + "Opening Discord"
                os.startfile(r"C:\...\Discord.exe")

            elif "open microsoft teams" in text:
                speak = speak + "Opening Microsoft Teams"
                os.startfile(r"C:\...\Teams.exe")

            elif "open microsoft edge" in text:
                speak = speak + "Opening Microsoft Edge"
                os.startfile(r"C:\...\Edge.exe")

            elif "open microsoft store" in text:
                speak = speak + "Opening Microsoft Store"
                os.startfile(r"C:\...\Store.exe")

            elif("open popsql" in text):
                speak = speak + "Opening PopSQL"
                os.startfile(r"C:\Users\shahi\OneDrive\Desktop\PopSQL-Setup-1.0.128.exe")

            elif "open CST studio" in text:
                speak = speak + "Opening CST Studio"
                os.startfile(r"C:\Users\shahi\OneDrive\Desktop\1april24.cst")

            elif "open Google Play" in text:
                speak = speak + "Opening Google Play"
                os.startfile(r"C:\Users\shahi\OneDrive\Desktop\GooglePlay.exe")

            elif "open pycharm" in text:
                speak = speak + "Opening PyCharm"
                os.startfile(r"C:\Users\shahi\Downloads\pycharm-community-2023.3.4.exe")

            elif "open intellij" in text:
                speak = speak + "Opening IntelliJ IDEA"
                os.startfile(r"C:\Users\shahi\Downloads\ideaIC-2023.3.4.exe")

            elif "open android studio" in text:
                speak = speak + "Opening Android Studio"
                os.startfile(r"C:\Users\shahi\Downloads\android-studio-2023.2.1.24-windows.exe")

            elif "open My Dell" in text:
                speak = speak + "Opening My Dell"
                os.startfile(r"C:\...\DellSupportCenter.exe")

            elif("open powerpoint" in text):
                speak = speak + "Opening Microsoft PowerPoint"
                os.startfile(r"C:\...\POWERPNT.EXE")

            elif("open outlook" in text):
                speak = speak + "Opening Microsoft Outlook"
                os.startfile(r"C:\...\OUTLOOK.EXE")

            elif("open onenote" in text):
                speak = speak + "Opening Microsoft OneNote"
                os.startfile(r"C:\...\ONENOTE.EXE")

            elif("Open word" in text):
                speak = speak + "Opening Microsoft Word"
                os.startfile(r"C:\...\WINWORD.EXE")

            elif("open xbox" in text):
                speak = speak + "Opening Xbox"
                os.startfile(r"C:\...\Xbox.exe")

            elif("open onedrive" in text):
                speak = speak + "Opening OneDrive"
                os.startfile(r"C:\Program Files\Microsoft OneDrive\OneDrive.exe")

            elif("open skype" in text):
                speak = speak + "Opening Skype"
                os.startfile(r"C:\...\Skype.exe")

            elif("open photos" in text):
                speak = speak + "Opening Photos"
                os.startfile(r"C:\...\Photos.exe")

            elif("open sticky notes" in text):
                speak = speak + "Opening Sticky Notes"
                os.startfile(r"C:\...\StikyNot.exe")

            elif("open snipping tool" in text):
                speak = speak + "Opening Snipping Tool"
                os.startfile(r"C:\...\SnippingTool.exe")

            elif("open windows media player" in text):
                speak = speak + "Opening Windows Media Player"
                os.startfile(r"C:\...\wmplayer.exe")

            elif("open vlc media player" in text):
                speak = speak + "Opening VLC Media Player"
                os.startfile(r"C:\...\vlc.exe")

            elif("open adobe reader" in text):
                speak = speak + "Opening Adobe Reader"
                os.startfile(r"C:\...\AcroRd32.exe")

            elif("open notepad++" in text):
                speak = speak + "Opening Notepad++"
                os.startfile(r"C:\...\notepad++.exe")

            elif("open winrar" in text):
                speak = speak + "Opening WinRAR"
                os.startfile(r"C:\...\WinRAR.exe")

            elif("open utorrent" in text):
                speak = speak + "Opening uTorrent"
                os.startfile(r"C:\...\uTorrent.exe")

            elif("open filezilla" in text):
                speak = speak + "Opening FileZilla"
                os.startfile(r"C:\...\FileZilla.exe")

            elif("open teamviewer" in text):
                speak = speak + "Opening TeamViewer"
                os.startfile(r"C:\...\TeamViewer.exe")

            elif("open anydesk" in text):
                speak = speak + "Opening AnyDesk"
                os.startfile(r"C:\...\AnyDesk.exe")

            elif("open zoom" in text):
                speak = speak + "Opening Zoom"
                os.startfile(r"C:\...\Zoom.exe")

            elif("open discord" in text):
                speak = speak + "Opening Discord"

            elif "exit" in text or "quit" in text:
                exit()

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    os.startfile(
                        r"C:\Users\shahi\OneDrive\Desktop\SAHIL - Chrome.lnk"
                    )

                elif "word" in text.lower():
                    speak = speak + "Opening Microsoft Word"
                    os.startfile(
                        r"C:\...\WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    os.startfile(
                        r"C:\...\EXCEL.EXE"
                    )

                elif "vs code" in text.lower():
                    speak = speak + "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Users\shahi\Downloads\VSCodeUserSetup-x64-1.87.0.exe"
                    )

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "Opening Google\n"
                    webbrowser.open("https://google.com/")

                elif "stackoverflow" in text.lower():
                    speak = speak + "Opening StackOverFlow"
                    webbrowser.open("https://stackoverflow.com/")

                else:
                    speak = speak + "Application not available"

            elif "youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                speak = speak + "Opening " + str(search) + " on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"



            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"



            elif "play music" in text or "play song" in text:
                talk("Here you go with music")
                music_dir = r"...\Music"
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)

            elif "joke" in text:
                speak = speak + pyjokes.get_joke()

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"

            elif "email to computer" in text or "gmail to computer" in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    to = "Receiver email address"
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    talk("I am not able to send this email")

            elif "mail" in text or "email" in text or "gmail" in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    talk("whom should i send")
                    to = input("Enter To Address: ")
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    speak = speak + "I am not able to send this email"

            elif "make a note" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that."

            elif "news" in text:
                url = (
                    "http://newsapi.org/v2/top-headlines?"
                    "country=in&"
                    "apiKey=6480e83e97b147e384bb4130a596ae07"
                )

                try:
                    response = requests.get(url)
                except:
                    talk("Please check your connection")

                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    talk(str(new["title"]))
                    engine.runAndWait()

                    print(str(new["description"]), "\n")
                    talk(str(new["description"]))
                    engine.runAndWait()
                    time.sleep(2)

            elif "send message" in text or "send a message" in text or "send a text Message" in text or "message kro" in text or "text message" in text or "message" in text or "Message send kr do" in text:
                account_sid = ""
                auth_token = ""
                client = Client(account_sid, auth_token)

                talk("What should i send")
                message = client.messages.create(
                    body=rec_audio(), from_="", to=""
                )

                print(message.sid)
                speak = speak + "Message sent successfully"

            elif "calculate" in text or 'send a message' in text:
                app_id = ""
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "what is" in text or "who is" in text:
                app_id = ""
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("is")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + answer

            elif "order a pizza" in text or "pizza" in text:
                pizza()



            # Assistant Audio speak
            response(speak)

    except:
        talk("I don't know that")