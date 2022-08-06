'''import math
print(math.pow(2,5))
print(math.sqrt(100))
print(math.factorial(3))
print(math.gcd(12,5))
print(math.remainder(102,5))


import random as r
print(r.choice((1,20,43,42)))
print(r.random())
print(r.randint(1,10))
print(r.choices((1,2,3,4,5),k=3))'''

#let's play the lottery
def main():
    a_ = input("Are you ready to play the lottery: ")
    if a_ == "yes":
        print("Okay let's start")
    else:
        print("Okay then, Good Bye!!")
        exit()

    import random as r
    a = int(input("Choose a random number between 1 to 5: "))
    b =(r.randint(1,5))
    if a == b:
        print("Congrats you won the lottery")
        exit()
    else:
        print("Sorry the winning numeber was",b,".Better luck next time")
    
    repeat = input("Ohh don't be sad. Do you want to play one more time? Type ok for yes: ")
    if repeat == "ok":
        print("Good Luck")
        main()
    else:
        print("bye bye")
        exit()
main()
