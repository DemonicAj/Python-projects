
#Game of Rock Paper Scissor
#By DemonicAJ
import random
def game(z):
    compwin=0
    playwin=0
    l=[1,2,3]
    d={1:"rock",2:"paper",3:"scissor"}
    for i in range(z):
        x=int(input("Choose 1:rock 2:paper 3:scissors \n"))
        print(d[x])
        y=random.randrange(1,4,1) 
        print(d[y])
        if y not in l:
            print("Wrong Choice")
            i = i-1
        elif x==y:
            print("Tie") 
        elif (x==1 and y==3) or (x==2 and y==1) or (x==3 and y==2):
            playwin+=1
            print("Player wins",playwin,"th time") 
        else:
            compwin+=1
            print("Computer wins",compwin,"th time")
    if compwin == playwin:
        print("It is tie!")
    elif compwin > playwin:
        print("********Computer Wins!********")
    else:
        print("********Player Wins!********")

x=input("Do you want to play y/n:\n")
if x == "y":
    game(int(input("Number of times to play:\n")))
else: 
    print("Then don't play idiot!!")
