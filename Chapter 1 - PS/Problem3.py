# Install an external module and use it to perform an operation of your interest


# Installed the module with pip install pyttsx3

# Importing module in the current script
import pyttsx3

# Code referred by pyttsx3 module page
engine = pyttsx3.init()
engine.say("Hello there! I am a python module that does Text to Speech.")
engine.runAndWait()