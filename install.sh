#!/usr/bin/env sh
if command -v termux-setup-storage
then
	yes | pkg install python
	yes | pkg install git
	TMP="/data/data/com.termux/files/home/tmp"
	mkdir $TMP
	DEST="/data/data/com.termux/files/usr/bin"
else
	TMP="/tmp"
	DEST="/usr/bin"
fi

pip3 install nltk
python3 -c 'import nltk; nltk.download("brown"); nltk.download("words")'

cd $TMP
git clone --depth=1 --single-branch https://github.com/Trainraider/wordlehelper.git
cd wordlehelper

install -D wordlehelper $DEST

cd ..
yes | rm -r wordlehelper

if command -v termux-setup-storage
then
	yes | rm -r $TMP
fi

