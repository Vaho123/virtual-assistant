# To be run in PyCharm

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
# Get all available voices
voices = engine.getProperty("voices")
# Get a female voice - second in the voices list
engine.setProperty("voice", voices[1].id)


def talk (statement):
    engine.say(statement)
    engine.runAndWait()

talk ("Hi there")
talk ("I'm listening")

def accept_command():
    try:
        with sr.Microphone() as source:
            print("I'm listening...")  # To tell the user they can now speak to the Virtual Assistant
            # this listens for anything coming in via the microphone (source) and assigns it to voice
            voice = listener.listen(source)
            # Use Google api to take what has been said and return the text
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alvina" in command:
                command = command.replace ("alvina", "")
    except:
        pass

    # print("returned command: " + command)
    return command

def run_assistant():
    command = accept_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("I will play " + song + "for you")
        pywhatkit.playonyt(song)
        print("playing " + song)
    elif "time" in command:
        # 24hr clock
        # time = datetime.datetime.now().strftime("%H:%M")
        # 12 hour clock
        time = datetime.datetime.now().strftime("%I:%M %p")
        print ("The time is: " + time)
        talk ("The time is" + time)
    elif "get me info on" in command:
        detail = command.replace("get me info on", "")
        # 2 = two lines of info
        info = wikipedia.summary(detail, 2)
        print(info)
        talk(info)
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        talk("I didn't hear that.  Please repeat it.")




run_assistant()
