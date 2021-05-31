## Run this command in terminal before executing this program
## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also rasa run this in seperate terminal
## rasa run actions
import os

import requests
import speech_recognition as sr  # import the library
#import subprocess
from gtts import gTTS
from translate import Translator

# sender= input("What is your name?\n")

bot_message = ""
message = ""
translator = Translator(from_lang='en', to_lang='hi')
translation = translator.translate("hello")

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot says, ", end=' ')

for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=translator.translate(bot_message), lang='hi')
myobj.save("welcome.mp3")
print('saved')

# playing the converted file

#subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
os.system("start welcome.mp3")

while bot_message != "Bye" or bot_message != "Thanks":

    r = sr.Recognizer() # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio
        print("Speak Anything :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio)  # use recognizer to convert our audio into text
            translator = Translator(to_lang='en')
            print("You said : {}".format(translator.translate(message)))

        except:
            print("Sorry could not recognize your voice")  # in case of voice not recognized
    if len(message) == 0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": translator.translate(message)})

    print("Bot says, ", end='')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    translator = Translator(to_lang='hi')
    myobj = gTTS(text=translator.translate(bot_message))
    myobj.save("welcome.mp3")
    print('saved')

    # playing the converted file
    #subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
    os.system("start welcome.mp3")