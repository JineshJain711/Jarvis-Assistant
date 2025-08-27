import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


news_api = "a5ac83b280b24162ad270ebe9ca2c36a"

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    print("Command:", c)

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "open instagram" in c:
        webbrowser.open("https://instagram.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play "):
        song = c.split(" ", 1)[1]  # everything after 'play'
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, I don't have that song in my library.")

    elif "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
            if r.status_code == 200:
                data = r.json()
                print(data)
                articles = data.get('articles', [])
                if not articles:
                    speak("Sorry, I couldn't find any news right now.")
                else:
                    speak("Here are the top 5 headlines.")
                    for article in articles[:5]:
                        speak(article['title'])
            else:
                speak("Failed to fetch the news, please try again later.")
        except Exception as e:
            speak("There was an error while fetching the news.")
            print("Error:", e)

def listenCommand(timeout=5, phrase_time=7):
    """Listen and recognize speech with timeout and better accuracy"""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # reduce background noise
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time)
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Network error with speech recognition service.")
            return ""

if __name__ == "__main__":
    speak("Initializing Jarvis... Ready for your command.")
    while True:
        wakeword = listenCommand()
        if "jarvis" in wakeword.lower():
            speak("Yes Boss, what should I do?")
            command = listenCommand()
            if command:
                processCommand(command)
            else:
                speak("Sorry, I didn't catch that. Please say again.")
