import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime

engine = pyttsx3.init()

r = sr.Recognizer()
with sr.Microphone() as source:
    print("---***START***---")
    print("Say something...")
    engine.say("Say something...")
    engine.runAndWait()
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

def work(command):
    command.lower()
    #if there is 'play' in command it will navigate to yt and plays the name of the thing that we ask it to play
    if 'play' in command:
        key1 = 'play'
        before1, key1, after1 = command.partition(key1)
        engine.say('Playing ' + after1)
        engine.runAndWait()
        print('Playing ' + after1)
        pywhatkit.playonyt(after1)

    #if there is 'search' in command, it will navigate to the web browser and search that thing we ask it to search
    if 'search' in command:
        key = 'search'
        before, key, after = command.partition(key)
        engine.say('Searching '+after)
        engine.runAndWait()
        print("Searching "+ after)
        pywhatkit.search(after)

    #if 'time' mentioned in the command, tell time
    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(f'The time is ',time)
        engine.say('The time is '+time)
        engine.runAndWait()





text1 = text.lower()
if 'python' in text1:
    work(text)
else:
    pass

#tell time
#open applications
#pause or play yt video
#up and down the volume
#control brightness of the screen
