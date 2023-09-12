import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'professor' in command:
                command = command.replace('professor',"")
                print(command)
    
    except Exception as e:
        raise e

    return command

def run_assistant():
    command = take_command()
    print(command)

    if "play" in command:
        song = command.replace('play','')
        speak('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("current time is " + time)

    elif 'name' in command:
        speak("My name is Professor")

    elif 'joke' in command:
        speak(pyjokes.get_joke())

    elif 'wikipedia' in command:
        speak("Searching wikipedia")
        query = command.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia ")
        print(results)
        speak(results)

    elif 'close' in command:
        print("Thankyou for considering me for help I would like to help in future more. Till then good bye")
        speak("Thankyou for considering me for help I would like to help in future more. Till then good bye")
        sys.exit()

    else:
        speak("Please say the command again!")

if __name__ == "__main__":
    #take_command()
    #speak("Hey, How  are you")
    while True:
        run_assistant()