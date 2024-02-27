# WordAnalyzer

     This file is part of WordAnalyzer.

    WordAnalyzer is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    WordAnalyzer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Foobar. If not, see <https://www.gnu.org/licenses/>. 

This program is used to automatically read books in the form of text files (files ending in .txt). Many such text files can be found through Project Gutenberg (www.gutenberg.org/).

This program uses python libraries pyttsx3 pandas and regex. 
- pyttsx3 was used for the text-to-speech functionality. 
- pandas was used for saving of reading data. 
- regex was used for delineation of sentences. 

This project started out as a way to check word frequencies in famous works (downloaded from project gutenberg), mainly as an intellectual curiousity. However, after I built that exact program, I realized it only required a few small modifications make it read the works out loud. 

To use this program, run the file 'Main.py' then follow the instructions in program.

If you download a book off project gutenberg, use the scroll functionality to change where the program starts. This is to skip the project gutenberg header from being read out.

Note, to stop the program while it is reading you have to close the terminal. Your location is saved up to the point you close the terminal.
