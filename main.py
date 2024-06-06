import random
list=["rock","paper","scissor"]

while (True):
    
    x=(input("enter \n 1 for ROCK \n 2 for SCISSOR \n 3 for PAPER"))
    try:
        if int(x)==1:
            x="rock"
        elif int(x)==2:
            x="scissor"
        elif int(x)==3:
            x="paper"
        else:
            print("enter a valid option")
        print("player = "+ x )
    except:
        print("enter a valid option")
    
    c=random.choice(list)
    match x:
        case "rock":
            if c=="scissor":
                print("computer = " + c)
                print("you win")
            elif c=="paper":
                print("computer = " + c)
                print("You Lost :(")
            else:
                print("computer = " + c)
                print("Its a draw")
        case "paper":
            if  c=="scissor":
                print("computer = " + c)
                print("you lose")
            elif c=="rock":
                print("computer = " + c)
                print("You win :(")
            else:
                print("computer = " + c)
                print("Its a draw")
        case "scissor":
            if c=="paper":
                print("computer = " + c)
                print("you win")
            elif c=="rock":
                print("computer = " + c)
                print("You Lost :(")
            else:
                print("computer = " + c)
                print("Its a draw")
    k=input("play again?y/n")
    if k!= "y":
        break

print("bye! have a good day.")






