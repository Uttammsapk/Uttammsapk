#let's make an lottery app 

'''import random as r
def lottery():
    ran = r.randint(1,5)   
    if a == ran:
        print("You won the lottery..")
        exit()
    else:
        print("Sorry you lost the lottery..")   
        lottery(a)
    
    b = "You will get one more chance n/Do you want to play again: "
    if b == "yes" or "Yes":
        print("Okay Good luck !!")
        lottery(a)
    else:
        exit()

a = int(input("Enter a number between 1 to 5: "))

lottery(a)'''


import random 

def lottery():
    e = [1,2,3]
    for i in e:
        a = int(input("Enter a number between 1 to 5: "))
        b = random.randint(1,5)
        if a == b:
            print("You Won The Lottery")
            exit()
        else:
            print("Sorry you lost the lottery")

        c = input("You will get one more chance \nDo you want to play again? ")
        if c == "yes" or "Yes":
            print("Okay")
        elif i <=2:
            lottery()
        else:
            print("Your reattempt chances are finished \nBetter luck next time")
            exit()
lottery()
        