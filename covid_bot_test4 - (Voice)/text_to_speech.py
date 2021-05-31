# import the required module for text to speech recognition
import os
import subprocess

from gtts import gTTS

# The text that you want to convert to audio
mytext = "Welcome to Covid-19 Fighting bot!"

# language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language)

# Saving the converted audio in a mp3 file named "welcome.mp3"
myobj.save("welcome.mp3")

# playing the converted file
#subprocess.call(['MPyg321', "welcome.mp3", '--play-and-exit'], shell = True)
os.system("start welcome.mp3")
