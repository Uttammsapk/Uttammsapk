def tiles():
    #Sale Laying Tiles
    #Let's input the function for the program 
    #Our objective of this programn is to ask the user and give them the output(value).
    #let's start getting information by user starting with asking there name.
    print("Welcome to Lowe's tiles")
    a = input("What is your name: ")
    print("Hello, ",a,"Let's find a great deal for you")
    
    #Now let's put the information for the tile value.
    #Given was, $300 for 20 sq.ft so the 1 sq.ft is 300/20 which is, 15
    #inputing the function
    t = 15
    # let's ask the user how many sq.ft they want
    tiles_wanted = int(input("How many tiles are you looking to buy: "))
    print("Okay let's find a great deal for",tiles_wanted,"tilesy")
    d = input("Are you also aware of our great deal of $300 for 20 tiles? y for yes: ")
    if d == "y":
        print("Okay that's great, you will get a great deal")
    else:
        ("okay dont worry we will give you great deal")
    #Now lets give the user the raw value of the cost
    total =  (t*tiles_wanted)
    print("The cost of your tiles for", tiles_wanted, "will be","$",total)
    #Now that we have the value for the tiles let's find out the total price with including other expenses
    def other():
        #The thing we need to inlude is state tax
        state_tax = 0.06
        tax_included = (total*state_tax)
        final_total = (tax_included+total)
        print("Your final out of the door price will be $",final_total,"with the taxes")
        print("It was great doing business with you, Good Bye!!")
        #At the final let's greet the user with thanyou message.
    
    j = input("Do you wish to repeat. Press ok for yes: ")
    if j== "ok":
        print("Okay here you go")
        tiles()
    else:
        exit()

tiles()