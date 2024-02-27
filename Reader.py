import pyttsx3 as speech

engine = speech.init()

def initialize(rate=200, volume=1.0, voice=0):
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[voice].id)

def readSentence(Sentence):
    
    engine.say(Sentence)
    engine.runAndWait()
        
    
    pass
