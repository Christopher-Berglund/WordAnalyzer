#     This file is part of WordAnalyzer.
#
#    WordAnalyzer is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free #Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#    WordAnalyzer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or #FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>. 

import regex as re
import pandas as pd
import os
import string

import Reader as rd

def selectBook():
    books = []
    while True:
        
        t = input("What is the name of the book? (type ? to view list of books) \n   exclude .txt extension: ")

        books = []
        for file in os.listdir("Books"):
            if file.endswith(".txt"):
                books.append(file[0:-4])

        if t == "?":
            for b in books:
                print(b)
            continue

        if t in books:
            break
        else:
            print("Please enter the name of a book in the Books folder")
    return t

def loadDefaultSettings():
    f = open("settings.config", "r")

    rate = int(f.readline())
    volume = float(f.readline())
    voice = int(f.readline())

    f.close()

    return rate, volume, voice


title = selectBook()

# Load Text file
A = open("Books\\" + title + ".txt", encoding="UTF-8")
data = A.read()
A.close()

data = data.replace("\n", " ")

# Load DefaultSettings
rate, volume, voice = loadDefaultSettings()

# Delineate the sentences within the book by sentence ending punctuation (.?!),
#  also removing any whitespace following said punctuation.
MySentences = pd.DataFrame(re.split(r'[.?!]+[ ]?', data))

# Load the Meta information for the library
StartingPointMeta = pd.read_csv("StartingPoints.csv", index_col=0)

# Check to ensure the book is in the StartingPointMeta
#  If it is not in there, add it.
if not (title in StartingPointMeta.index):
    
    Line = pd.DataFrame([[0, 0, rate, volume, voice]],
                        columns=["StartingPoint", "Current", "rate", "volume", "voice"],
                        index=[title])

    # add new line to StartingPoints when the title is missing.
    StartingPointMeta = pd.concat([StartingPointMeta,Line])
    StartingPointMeta.to_csv("StartingPoints.csv")

while True:
    print("What would you like to do with the book "+title +"?")
    print(" 1 - Listen to it.")
    print(" 2 - Do a word frequency analysis")
    print(" 3 - Scroll Book")
    print(" 4 - Modify Settings")
    print(" 5 - Select a Different Book")
    print(" 0 - quit")

    try:
        answer = int(input())
    except:
        answer = 999
    
    # Quit
    match(answer):
        # quit
        case 0:
            quit()

        # Read
        case 1:
            # Load default settings
            rate, volume, voice = loadDefaultSettings()

            # Deciding whether to use the default settings or not
            default = True
            yn = input ("Do you want to use the default settings? (y/n): ").lower()
            if yn == 'n':
                default = False

            # If we decide not to use the default settings,
            #  load the book specific settings and over ride the earlier stuff.
            if not default:
                rate = StartingPointMeta["rate"][title]
                volume = StartingPointMeta["volume"][title]
                voice = StartingPointMeta["voice"][title]

            # Perform the initialization required for the reading library.
            rd.initialize(rate, volume, voice)

            i = StartingPointMeta["Current"][title]
            while i<len(MySentences):
                print("{}: {}".format(i, MySentences.loc[i].item()))
                rd.readSentence(MySentences.loc[i].item())
                
                i+=1
                
                # Save the current location
                StartingPointMeta.loc[title, "Current"] = i
                StartingPointMeta.to_csv("StartingPoints.csv")

            print("Contgratulations! You've finished the book!")

            StartingPointMeta.loc[title, "Current"] = StartingPointMeta.loc[title, "StartingPoint"]
            StartingPointMeta.to_csv("StartingPoints.csv")
        
        # Word Frequency
        case 2:
            word_data = data.lower()

            # Separate out each of the words, that means removing any whitespace or punctuation
            MyWords = pd.DataFrame(re.split(r"[{} ]+".format(string.punctuation), word_data))

            # Count each how many times each word appears
            word_frequency = MyWords[0].value_counts()
            word_frequency.name="Frequency"

            totalCount = sum(word_frequency)
            word_proportion = word_frequency/totalCount
            word_proportion.name = "Proportion"
            table = pd.concat([word_frequency, word_proportion], axis=1)
            
            print(table)
            try:
                k = str(input("Would you like to save this to a .csv file? (y/n): "))
            except:
                continue
            if k.lower()=="y":
                table.to_csv(title+"_word_frequency.csv")
        
        # Scroll Book
        case 3:
            j = StartingPointMeta["Current"][title]
            n = 3
            while True:
                # Meta information about scrolling.
                print()
                print("The book starts at {}".format(StartingPointMeta["StartingPoint"][title]))
                print("Your bookmark is at {}".format(StartingPointMeta["Current"][title]))
                print("Your cursor (*) is at {}".format(j))
                
                # For displaying the contents surrounding the cursor, I am using the 'try' and 'except'
                #  This is so if you are next to an edge of the book (so j-3 < 0 ) it will try it anyways and if it fails it'll move on.

                for i in range(j - n, j + n + 1):
                    try:
                        if i != StartingPointMeta["Current"][title]:
                            print(" {}:{}".format(i, MySentences.loc[i].item()))
                        else:
                            print("*{}:{}".format(i, MySentences.loc[i].item()))
                    except:
                        pass

                print()
                print("What would you like to do?")
                print(" 1 - jump cursor")
                print(" 2 - move bookmark to cursor")
                print(" 3 - move starting point to cursor")
                print(" 0 - go back")
                try:
                    a=int(input())
                except:
                    print("Please give valid input")
                    continue

                # Go back
                if a ==0:
                    break
                
                # Jump cursor
                elif a==1:
                    try:
                        s=int(input("Where do you want to jump?: "))
                    except:
                        print("please give a valid input")

                    if s >= len(MySentences) or s<0:
                        print("Keep the cursor between 0 and {}.".format(len(MySentences)-1))
                        continue
                    else:
                        j = s
                        
                # Current <- cursor
                elif a==2:
                    StartingPointMeta.loc[title, "Current"] = j
                    StartingPointMeta.to_csv("StartingPoints.csv")
                    
                # StartingPoint <- cursor
                elif a==3:
                    StartingPointMeta.loc[title, "StartingPoint"] = j
                    if StartingPointMeta.loc[title, "Current"] < j:
                        StartingPointMeta.loc[title, "Current"] = j
                    StartingPointMeta.to_csv("StartingPoints.csv")

        # Settings
        case 4:
            while True:
                print("%rate: {}".format(StartingPointMeta["rate"][title]))
                print("volume: {}".format(StartingPointMeta["volume"][title]))
                print("voice: {}".format(StartingPointMeta["voice"][title]))
                print()
                print("What do you want to do?")
                print(" 1 - Set %rate")
                print(" 2 - Set volume")
                print(" 3 - Set voice")
                print(" 0 - Save and go back")

                try:
                    a = int(input())
                    if not a in range(4):
                        raise ValueError()
                except:
                    print("please give a valid input")
                    continue
                # Save and go back
                if a==0:
                    StartingPointMeta.to_csv("StartingPoints.csv")
                    break
                else:
                    setting = ["rate","volume","voice"][a-1]
                    print("What do you want to set {} to?".format(setting))
                    print("currently {} is: {}".format(setting, StartingPointMeta[setting][title]))
                    try:
                        s=float(input("You will set it to: "))
                        if s<0:
                            raise ValueError()
                        
                        if a == 3:
                            s = int(s)
                            if not s in [0,1]:
                                raise ValueError()
                    except:
                        print("please give a valid input")
                        continue
                    StartingPointMeta.loc[title, setting] = s

        # Select a Different Book
        case 5:
            title = selectBook()

        # Mistake
        case _:
            print()
            print("Please give one of the listed available answers.")
            continue

