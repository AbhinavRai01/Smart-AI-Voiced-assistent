import os
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def recongnising():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening...")
        speak("listening")
        r.pause_threshold = 1
        audio = r.record(source, duration=4)
    try:
        print("recongnizing...")
        speak("Recongnizing")
        query = r.recognize_google(audio, language='en-in')
        return query
    except:
        print("Unable to recongnize")


def waitbtwn():
    s = sr.Recognizer()
    with sr.Microphone() as source:
        audio = s.record(source, duration=2)
    try:
        a = s.recognize_google(audio, language='en-in')
        return a
    except:
        return ""


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email,password)
    server.sendmail(email, to, content)
    server.close()


speak("Hello there this is an AI agent created by abhinav How can I serve you")
while True:
    query = recongnising()

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    print(query)
    try:
        query = query.lower()
    except:
        speak("sorry unable to recongnise")
        continue

    if 'wikipedia' in query:
        search = query.replace("wikipedia", "")
        speak("Gathering search results . please wait")
        search_results = wikipedia.search(search)

        Req_page = wikipedia.page(search_results[0])

        content = wikipedia.summary(Req_page)
        print(content)
        speak(content[0:200])

    elif 'open youtube' in query:

        speak("Opening youtube")
        webbrowser.get(chrome_path).open("youtube.com")

    elif 'open swiggy partner' in query:
        speak("Opening swiggy partner")
        webbrowser.get(chrome_path).open("https://partner.swiggy.com/")

    elif 'open google' in query:
        speak("Opening google")
        webbrowser.get(chrome_path).open("google.com")

    elif 'google search' in query:

        search = query.replace("google search", "")
        speak(f"searching about{search}")
        driver = webdriver.Chrome('F:\chromedriver')
        driver.get('http://www.google.com/')

        search_box = driver.find_element_by_name('q')
        search_box.send_keys(search)
        search_box.submit()

    elif 'play the song' in query:

        search = (query.replace("play the song ", "")) + "song"
        speak(f"playing the song{search} from youtube.please wait")
        driver = webdriver.Chrome('F:\chromedriver')

        a = search.replace(" ", "+")
        driver.get(f'https://www.youtube.com/results?search_query={a}')

        song = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        song.click()

    elif 'search on youtube' in query:

        driver = webdriver.Chrome('F:\chromedriver')
        search = query.replace("search on youtube ", "")
        speak(f"searching on youtube about{search}")
        a = search.replace(" ", "+")
        driver.get(f'https://www.youtube.com/results?search_query={a}')

    elif 'open vs code' in query:
        speak("opening vs code")
        os.startfile("F:\Microsoft VS Code\Code")

    elif 'open pycharm' in query:
        speak("opening pycharm")
        os.startfile("C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.3\bin\pycharm64.exe")

    elif 'open calculator' in query:
        speak("opening calculator")
        os.startfile("C:\\Windows\\System32\\calc.exe")

    elif 'open notepad' in query:
        speak("opening notepad")
        os.startfile("C:\\Windows\\System32\\notepad.exe")

    elif 'open wordpad' in query:
        speak("opening wordpad")
        os.startfile("C:\\Windows\\System32\\write.exe")

    elif 'open chrome' in query:
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    elif 'send email' in query:
        try:
            speak("What should I say?")
            content = recongnising()

            speak("Whom shall i send this")
            email = recongnising()

            emailac = email.lower()
            emailacc = email.replace(" ", "") + "@gmail.com"

            print(emailacc)
            sendEmail(emailacc, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Email has not been send. Sorry for the inconvinience")

    elif 'exit' in query:

        speak("exiting the program Thank you")
        exit()

    elif '+' in query:
        try:
            string = query.replace(" + "," ")
            var_list = string.split()
            result = int(var_list[0]) + int(var_list[1])

            print(f"{var_list[0]} + {var_list[1]} = {result}")
            speak(f"{query} equals {result}")
        except:
            print(("Invalid value ! Please try again."))
            speak("invalid value please try again")

    elif '-' in query:
        try:
            string = query.replace(" - "," ")
            var_list = string.split()
            result = int(var_list[0]) - int(var_list[1])

            print(f"{var_list[0]} - {var_list[1]} = {result}")
            speak(f"{query} equals {result}")
        except:
            print(("Invalid value ! Please try again."))
            speak("invalid value please try again")


    elif 'into' in query:
        try:
            string = query.replace(" into "," ")
            var_list = string.split()
            result = int(var_list[0]) * int(var_list[1])

            print(f"{var_list[0]} * {var_list[1]} = {result}")
            speak(f"{query} equals {result}")
        except:
            print(("Invalid value ! Please try again."))
            speak("invalid value please try again")


    elif 'divided by' in query:
        try:
            string = query.replace(" divided by "," ")
            var_list = string.split()
            result = int(var_list[0]) / int(var_list[1])

            print(f"{var_list[0]} / {var_list[1]} = {result}")
            speak(f"{query} equals {result}")
        except:
            print(("Invalid value ! Please try again."))
            speak("invalid value please try again")

    else:
        speak("sorry.Unable to recongnize")

    q = input()
