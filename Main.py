#Author: Vineet Raj Parashar
###THIS PROGRAM NEEDS INTERNET CONNECTION
# importing module for converting speech into text
import speech_recognition as sr
# importing module for converting text into speech
import pyttsx3
# importing module for YouTube search eg:-Song
import pywhatkit as pkt
# importing module for extracting system date
import datetime
# importing module for wikipedia search
import wikipedia as wk
# importing module for generating random jokes(just for fun)
import pyjokes
# importing modules for specifies a set of strings that matches it
import re
# importing module for web search
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# we pass a string as an argument into this function and it will speak up the input string
def talk(text):
    engine.say(text)
    engine.runAndWait()

# This function will take input command from your system's microphone or it will recognise the voice
# This assistant will only repond when you say "Hey dude" before saying any task to do.
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey dude' in command:
                command = command.replace('hey dude', '')
                print(command)
    except:
        pass
    return command

# This function contains all kinds of commands which this model can perform.
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pkt.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wk.summary(person,1)
        print(info)
        talk(info)
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)',command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass
    '''elif 'current weather in' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            talk('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))
    '''
    elif 'what is' in command:
        obj = command.replace('what is','')
        info = wk.summary(obj,1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('No, I am in relationship with wi-fi')
    elif 'how old' in command:
        talk('I was created in 2020,so I am still fairly young')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')

print("**Hello there!! I am your virtual assistance**")
print("->If you want anything just say 'Hey Dude' and ask your question")
while True:
    run_alexa()
