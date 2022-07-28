#Software Company selling a pakage for $99.
#Lets give discount according to the quantity

print("UTTAM BASKET LLC")

a = 99
number = (int(input("How many package you are going to buy = ")))
if number < 10:
    print("Your total is $", (a*number))
if number >=10 and number <=19:
    print("Your total is $", (a*number),"and you got 10% discount which is $",(a*number)*0.1,"So, your total is $",(a*number)-(a*number)*0.1)

if number >=20 and number <=49:
    print("Your total is $", (a*number),"and you got 20% discount which is $",(a*number)*0.2,"So, your total is $",(a*number)-(a*number)*0.2)
    
if number >=50 and number <=99:
    print("Your total is $", (a*number),"and you got 30% discount which is $",(a*number)*0.3,"So, your total is $",(a*number)-(a*number)*0.3)

if number >= 100:
    print("Your total is $", (a*number),"and you got 40% discount which is $",(a*number)*0.4,"So, your total is $",(a*number)-(a*number)*0.4)
