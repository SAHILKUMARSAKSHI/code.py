import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" hello SAHIL sir, I am BIRD, how may i help you ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shahil.ks011@gmail.com', 'your-password')
    server.sendmail('shahil.ks011@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:

        text = takeCommand().lower()
    # text = rec_audio()
    # speak = ""

    # Logic for executing tasks based on query
        if 'wikipedia' in text:
            speak('Searching Wikipedia...')
            text = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in text:
            webbrowser.open("youtube.com")

        elif 'open google' in text:
            webbrowser.open("google.com")

        elif 'play my music' in text:
            webbrowser.open("https://wynk.in/music")

        elif 'open stackoverflow' in text:
            webbrowser.open("stackoverflow.com")

        # elif "who are you" in text or "define yourself" in text:
        #     speak = speak + "Hello, I am an Assistant. Your Assistant. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera"

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

        elif ("who is your servant" in text or "who is your slave" in text):
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

        elif ("open whatsapp" in text):
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

        elif ("open popsql" in text):
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

        elif ("open powerpoint" in text):
            speak = speak + "Opening Microsoft PowerPoint"
            os.startfile(r"C:\...\POWERPNT.EXE")

        elif ("open outlook" in text):
            speak = speak + "Opening Microsoft Outlook"
            os.startfile(r"C:\...\OUTLOOK.EXE")

        elif ("open onenote" in text):
            speak = speak + "Opening Microsoft OneNote"
            os.startfile(r"C:\...\ONENOTE.EXE")

        elif ("Open word" in text):
            speak = speak + "Opening Microsoft Word"
            os.startfile(r"C:\...\WINWORD.EXE")

        elif ("open xbox" in text):
            speak = speak + "Opening Xbox"
            os.startfile(r"C:\...\Xbox.exe")

        elif ("open onedrive" in text):
            speak = speak + "Opening OneDrive"
            os.startfile(r"C:\Program Files\Microsoft OneDrive\OneDrive.exe")

        elif ("open skype" in text):
            speak = speak + "Opening Skype"
            os.startfile(r"C:\...\Skype.exe")

        elif ("open photos" in text):
            speak = speak + "Opening Photos"
            os.startfile(r"C:\...\Photos.exe")

        elif ("open sticky notes" in text):
            speak = speak + "Opening Sticky Notes"
            os.startfile(r"C:\...\StikyNot.exe")

        elif ("open snipping tool" in text):
            speak = speak + "Opening Snipping Tool"
            os.startfile(r"C:\...\SnippingTool.exe")

        elif ("open windows media player" in text):
            speak = speak + "Opening Windows Media Player"
            os.startfile(r"C:\...\wmplayer.exe")

        elif ("open vlc media player" in text):
            speak = speak + "Opening VLC Media Player"
            os.startfile(r"C:\...\vlc.exe")

        elif ("open adobe reader" in text):
            speak = speak + "Opening Adobe Reader"
            os.startfile(r"C:\...\AcroRd32.exe")

        elif ("open notepad++" in text):
            speak = speak + "Opening Notepad++"
            os.startfile(r"C:\...\notepad++.exe")

        elif ("open winrar" in text):
            speak = speak + "Opening WinRAR"
            os.startfile(r"C:\...\WinRAR.exe")

        elif ("open utorrent" in text):
            speak = speak + "Opening uTorrent"
            os.startfile(r"C:\...\uTorrent.exe")

        elif ("open filezilla" in text):
            speak = speak + "Opening FileZilla"
            os.startfile(r"C:\...\FileZilla.exe")

        elif ("open teamviewer" in text):
            speak = speak + "Opening TeamViewer"
            os.startfile(r"C:\...\TeamViewer.exe")

        elif ("open anydesk" in text):
            speak = speak + "Opening AnyDesk"
            os.startfile(r"C:\...\AnyDesk.exe")

        elif ("open zoom" in text):
            speak = speak + "Opening Zoom"
            os.startfile(r"C:\...\Zoom.exe")

        elif ("open discord" in text):
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




        elif 'play music' in query:
            music_dir = 'https://wynk.in/music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'email to sahil' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shahil.ks011@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sahil sir. I am not able to send this email")


