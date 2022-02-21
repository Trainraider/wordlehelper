# wordlehelper

A basic TUI to assist with the game wordle and its clones. Enter your guess words and the colors of each letter, and this program will tell you the top 15 most common possible words as well as how many possible words exist, so you know how narrowed down you are. These suggestions are not optimal suggestions for gathering information and only become optimal once sufficient information has already been gathered.

You'll probably have enough information to complete the wordle after guessing "crane, pivot, musky"

## Installation

### Android

* Install and open Termux from the fdroid app store
* run:

```
curl https://raw.githubusercontent.com/Trainraider/wordlehelper/main/install.sh | sh
```

### Linux
* Make sure you have python3, pip3, curl and git
* run:

```
curl https://raw.githubusercontent.com/Trainraider/wordlehelper/main/install.sh | sudo sh
```

## Usage

* run wordlehelper in a terminal by typing `wordlehelper`
* Guess a word in wordle
* Type that word into wordlehelper
* Tell wordlehelper the color of each letter one at a time
* The list of words are the 15 most common words that are possible answers.
* Make a new guess and repeat the above 4 steps
* Type CTRL+d to restart once you have completed the Wordle challenge or made a mistake.
* Type CTRL+c (and enter in termux) to exit wordlehelper



