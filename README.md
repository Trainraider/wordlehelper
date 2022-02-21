# wordlehelper

A basic TUI to assist with the game wordle and its clones. Enter your guess words and the colors of each letter, and this program will tell you the top 15 most common possible words as well as how many possible words exist, so you know how narrowed down you are. These suggestions are not optimal suggestions for gathering information and only become optimal once sufficient information has already been gathered.

You'll probably have enough information to complete the wordle after guessing "crane, pivot, musky"

# Android installation:    
* Download Termux from fdroid
* pkg install python
* pip install nltk
* python
* >>> import nltk
* >>> nltk.download('brown')
* >>> nltk.download('words')
* press CTRL+d
* git clone this repository
* cd wordlehelper
* chmod +x wordle.py

Now run it with ./wordle.py
