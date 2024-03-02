# This file is part of WordAnalyzer.
# file author: Christopher-Berglund
# License: GPLv3

# This file contains the functions WordAnalyzer calls for performing text-to-speech.

import pyttsx3 as speech

engine = speech.init()

def initialize(rate=200, volume=1.0, voice=0):
    # Sets all the relevant properties of the engine, returns None
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[voice].id)

def readSentence(Sentence):
    # Takes the input string Sentence and reads it with text to speech, pausing all other execution until completion of that sentence. 
    # returns None
    engine.say(Sentence)
    engine.runAndWait()
        
    
    pass
