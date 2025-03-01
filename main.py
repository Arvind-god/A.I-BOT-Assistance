import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import microphone
import re

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="eee5b0bf8d924fed827c2a5efd61a8cb"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
    elif command.startswith("play"):
        song = command.split(" ")[1]
        link = musicLibrary.music.get(song)  
        webbrowser.open(link)
    elif"news"in command:
           r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
           if r.status_code == 200:
            
            data = r.json()
            
            
            articles = data.get('articles', [])
            
            for article in articles:
                speak(article['title'])
    

    else:
        speak("Command not recognized.")


if __name__ == "__main__":
    speak("Initializing Ayush....")
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            word = recognizer.recognize_sphinx(audio)
            if (word.lower() == "ayush"):
                speak("hi")
                with sr.Microphone() as source:
                    print("Listening for command....")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_sphinx(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")
