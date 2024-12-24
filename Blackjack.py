import random

def dealcards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    c=random.choice(cards)
    return c

def calculator(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(uscore,cscore):
    if uscore == cscore:
        return "Draw"
    elif cscore == 0:
        return "Loss Oppenent Has Blackjack" 
    elif uscore == 0:
        return "Win with a Blackjack"
    elif uscore > 21:
        return "You went over,You Lose"
    elif cscore > 21:
        return "You win,Opponent went over"
    elif uscore > cscore:
        return "You win"
    else:
        return "You Lose"
    

def playthegame():
    userc=[]
    computerc=[]
    computerscore = -1
    userscore =-1
    isgameover=False

    for _ in range(2):
        userc.append(dealcards())
        computerc.append(dealcards())

    while not isgameover:

        userscore=calculator(userc)
        computerscore=calculator(computerc)

        print(f"Your card:{userc},current score:{userscore}")
        print(f"Computers first card:{computerc[0]}")

        if userscore == 0 and computerscore == 0 or userscore >21:
            isgameover = True
        else:
            userinput=input("Type 'y' to get another card,Type 'n' to pass: ")
            if userinput == "y":
                userc.append(dealcards())
                
            else:
                isgameover=True

    while computerscore != 0 and computerscore < 17:
        computerc.append(dealcards())
        computerscore=calculator(computerc)



    print(f"your final hand :{userc},final score:{userscore} ")
    print(f"Computer final hand:{computerc},final score::{computerscore}")
    print(compare(userscore,computerscore))

while input("Do you want play the game of blackjack? Type 'yes'or 'no':") == 'yes':
    playthegame()





    



             

    



