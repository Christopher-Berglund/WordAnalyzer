# WordAnalyzer

Contributors: Christopher-Berglund

Tags: reading, data

Donate link: N/A

Requires at least: Python 3.0, pandas, pyttsx3, regex

License: GPLv3

License URL: https://www.gnu.org/licenses/gpl-3.0.txt

This program is used to automatically read books in the form of text files (files ending in .txt). Many such text files can be found through Project Gutenberg (www.gutenberg.org/).

This program uses python libraries pyttsx3 pandas and regex. 
- pyttsx3 was used for the text-to-speech functionality. 
- pandas was used for saving of reading data. 
- regex was used for delineation of sentences. 

This project started out as a way to check word frequencies in famous works (downloaded from project gutenberg), mainly as an intellectual curiousity. However, after I built that exact program, I realized it only required a few small modifications make it read the works out loud. 

To begin listening to the book, 
 - Make sure there are files ending in .txt in the folder Books
 - Run the file 'Main.py'
 - Type the name of one of the files ending in .txt in the folder Books, to bring up a list of files ending in .txt, type '?'
 - type '1' to begin listening.
 - to stop the reading, close the program.

You can use the scroll functionality to change the book's starting point. If you download a book off project gutenberg, you can use this to move the starting point past the table of contents.
To use the scroll functionality to change your starting point in the book,
 - In the menu, type '3' to scroll book.
 - Type '1' to jump the cursor
 - Enter an estimation for where in the book you wish to start.
 - Read the surrounding sentences on that part and decide if you guessed correctly. If not, type '1' again to move the cursor again. Make sure the sentence with the * next to it is where you wish to start listening.
 - type '3' to move the starting point to the cursor location.
 - type '2' to move the bookmark (where you currently are in the book) to the cursor location.
 - type '0' to go back to the main menu.

The word frequency analysis feature allows you to find how often particular words get used in the book in question.
To use the word frequency analysis feature,
 - In the menu, type '2' to do a word frequency analysis. This will generate a dataframe
 - type 'y' to save the result to a .csv file.
 - type in the name for the file.
 - Check the folder containing Main.py to find the .csv file.

Here are the files used and what they do.
 - Main.py	- This is the file that should be run for using WordAnalyzer
 - Reader.py - This file contains the functions WordAnalyzer calls for performing text-to-speech.
 - StartingPoints.csv - Contains the data on starting points, as well as current locations for all the books used by the program in the past, along with the book specific user settings.
 - settings.config - Used to store the default settings.







