import nltk
from nltk.corpus import words
from nltk.corpus import brown
from os.path import exists

print("CTRL+d : Restart")
print("CTRL+c enter: Quit")
while True:
    if exists('.wordlist'):
        with open('.wordlist', 'r') as f:
            w = f.read().splitlines()
    else:
        print("Generating word list... Hold on.")
        freqs = nltk.FreqDist([w.lower() for w in brown.words()])
        w = [x for x in set(words.words()) if len(x)==5 if x.lower()==x if "'" not in x]
        w = sorted(w, key=lambda x: freqs[x.lower()], reverse=True)
        w = w[0:4*len(w)//8]
        with open('.wordlist', 'w') as f:
            for i in w:
                f.write("%s\n" % i)

    while True:
        try:
            print(len(w), " possibilities!")
            guess = ""
            while len(guess)!=5:
                guess = input("guess word:\n")
                if len(guess) !=5:
                    print("Guess must be 5 letters!")
            for i, l in enumerate(guess):
                print("What color is ", l, " ?")
                c = 'x'
                while c not in "Gyg":
                    c = input("<G/y/g> Green/Yellow/gray\n")
                    if c == 'G':
                        w = [x for x in w if x[i]==l]
                    if c == 'y':
                        w = [x for x in w if l in x if x[i]!=l]
                    if c == 'g':
                        w = [x for x in w if l not in x]
            for x in range(15):
                if x < len(w):
                    print(w[x])
                else:
                    break
        except EOFError:    
            break
        except KeyboardInterrupt:
            print("Goodbye!")
            exit()
