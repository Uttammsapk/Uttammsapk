#Let's calculate the revenew for Dinsney University this year
# I am using the def function so that I am implement the main function
def main():
    #Asking my user to provide his/her name.
    a = input("Welcome to revenew generator, Can you please tell me your name: " )
    #Giving user a hello message
    [print("Hello,",a,)]
    #giving direction to the user to find the revenew
    print("Now let's start with finding your revenew")



    #Asking user the number of ticket that they sold and conforming the value.
    b = int(input("How many Box office tickets for (Elite Member)have you sold: "))
    print("Elite ticket is worth $200 ")
    #calulating the total for elite member 
    c = (b*200)
    print("So, the sale for Box Office is,$",c)
        

    #Asking user the number of ticket that they sold and conforming the value.
    d = int(input("How many Tier 1 ticket have you sold: "))
    print("Tier 1 ticekt is worth $50")
    #calulating the total for tier1 member 
    e = (d*50)
    print("So, the sale for Tier 1 is, $",e)


        
    #Asking user the number of ticket that they sold and conforming the value.
    f = int(input("How many Tier 2 ticket have you sold: "))
    print("Tier 2 ticekt is worth $30")
    #calulating the total for tier2 member 
    g = (f*30)
    print("So, the sale for Tier 1 is, $",g)
        

    #Asking user the number of ticket that they sold and conforming the value.
    h = int(input("How many Tier 3 ticket have you sold: "))
    print("Tier 3 ticekt is worth $20")
    #calulating the total for tier3 member 
    i = (h*20)
    print("So, the sale for Tier 1 is, $",i)
        

    
    
    #Asking the user if they want to total value and if they input "yes" providing them with the value
    j = input("Now would you like to get a total number of sale: ")
    #Calualting the total number of sale
    k = (c+e+g+i)
    print("The total number of sale generated by the selling the ticket was $", k)
    #Proving the information to the user by giving the final total value
    #Now asking the user if they want to repeat the program
    l = input("Would you like to check your sale one more time?. Press ok if you want to repeat: ")
    #Giving the user value accoring to the input 
    if l == "ok":
        print("Okay here we go")
        main()
       
    else:
        #If the user want to end, then ending the program with goobye message
        print("It was nice having you here", a, ". Have a great day. Good Bye!!")
        exit()

main()












