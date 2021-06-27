#A simple game of Hangman
#By DemonicAj

import random as r
from words import words 

def game(word):
    global gc
    global gw
    l=word.upper()
    s=len(l)-1
    k=list(l)
    i=1
    j=[]
    flag=0
    for i in range(4):
        x=r.randrange(0,s,1)
        if x not in j:
            j.append(x)
            k[x]="_"
        else:
            i=i-1

    j.sort()
    c=" ".join(k)
    print(c)

    print("You have 3 chances")
    print("Guess and enter the missing alphabets: \n")
    #print(len(j))
    
    for o in range(1,4):
        t=k
        for z in range(len(j)):
            i=j[z]
            t[i]=input().upper()
            g=t[i]
            #t="".join(t)
            #print(t)
            if g==l[i]:
                flag+=1
                print("Correct alphabet!!")
        t="".join(t)
        print(t)
        if flag==len(j):
            print(f"Your guess is correct : {t} !!")
            print("You have won !!!")
            gc+=1
            break
        else:
            ch=3-o
            flag=0
            
            if ch==0:
                gw+=1
                print(f"You have lost !!! \nThe correct word is {l}")
            else:
                print(f"Wrong guess!! You have {ch} more chance, try once more from starting")

global gc
global gw
n=int(input("How many words do u want to guess :\n"))
gc=0
gw=0
l=[]
for i in range(0,n):
    x=r.choice(words)
    x.upper()
    if x not in l:
        l.append(x)
        game(x)
    else:
        i=i-1
    
if gc==n:
    print("You have guessed all {n} words correctly!!")
elif gc>0:
    print("You only guessed {gc} words correctly!! And You failed to guess {gw} words!!")
else:
    print("You failed to guess all the words!!")