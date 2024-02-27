#     This file is part of WordAnalyzer.
#
#    WordAnalyzer is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
#
#    WordAnalyzer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>. 

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
