#!/usr/bin/env sh
if command -v termux-setup-storage
then
	yes | pkg install python
	TMP="/data/data/com.termux/files/home/tmp"
	DEST="/data/data/com.termux/files/usr"
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
rm -r wordlehelper

if command -v termux-setup-storage
then
	rm -r $TMP
fi

