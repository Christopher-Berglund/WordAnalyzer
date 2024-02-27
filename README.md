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

To use this program, run the file 'Main.py' then follow the instructions in program.

If you download a book off project gutenberg, use the scroll functionality to change where the program starts. This is to skip the project gutenberg header from being read out.

Note, to stop the program while it is reading you have to close the terminal. Your location is saved up to the point you close the terminal.
