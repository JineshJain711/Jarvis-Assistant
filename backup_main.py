# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import requests
# news_api = "28e0c7698d4e4be7a92ff1971c39a511"
# recognizer = sr.Recognizer()
# engine  = pyttsx3.init()
# def speak(text) :
#     engine.say(text)
#     engine.runAndWait()
# def processCommand(c):
#     print(c)
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
#     elif "open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")
#     elif c.lower().startswith("play") :
#         song  = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)
#     elif "news" in c.lower():
#         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
    
#         if r.status_code == 200:
#             data = r.json()  # Call json() method to get the JSON object
    
#             articles = data.get('articles', [])  # Ensure articles is an empty list if 'articles' key is not found
        
#             for article in articles:  # Corrected the typo in the loop variable name
#                 speak(article['title'])
#         else:
#             print("Failed to retrieve the news")

        
    
    
# if __name__ == "__main__" :
#     speak("Initializing Jarvis....")
#     while True :
#         #Listen and wake for word Jarvis
#         #obtain audio from microphone
#         r = sr.Recognizer()
#         print("recongnize")
#         # recognize speech using Sphinx
#         try:
#             with sr.Microphone() as source:
#                 print("Listning..!")
#                 audio = r.listen(source )
#             word = r.recognize_google(audio)
#             if(word.lower() == "jarvis") :
#                 speak("Yes Boss")
#                  #listen for command
#                 with sr.Microphone() as source:
#                     print("Jarvis Listening..!")
#                     audio = r.listen(source)
#                     command =r.recognize_google(audio)
#                     processCommand(command)  
#         except sr.UnknownValueError:
#             print("Sphinx could not understand audio")
#         except sr.RequestError as e:
#             print("Sphinx error; {0}".format(e))