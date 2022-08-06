def main():

    #let's start with solving the wifi error with function 
    #Program to solve WIFI Connection Error
    #We will import time so that we can start the module
    import time
    #Now we will ask the user if they are having problem with the wifi connection.
    #The program will function according to the user command
    z = input("Please enter your name: ")
    print("Hello,", z) 
    a = input("If you are having problem with wifi connection, Use YES or NO: ").upper()
    if(a=="YES"):
        print("Reboot the computer and try to connect.")
        
        b = input("Did the fix that problem, use yes or no: ").upper()
        if(b=="NO"):
            print("Reboot the router and try to connect.")
            # Giving user the advise and working accordint to the responce
            C = input("Did the fix that problem, use yes or no: ").upper()
            if(C=="NO"):
                print("Make Sure your cables between the router and modem are pluged in firmly.")
               
                d = input("Did the fix that problem, use yes or no: ").upper()
                if(d=="NO"):
                    print("Move the router to a new location and try to connect.")
                    
                    e = input("Did the fix that problem, use yes or no: ").upper()
                    if(e=="NO"):
                         print("Get a new Router, Have a nice day.")
                    else:
                        print("Thanks, Enjoy your wifi connection.")
                        #The enjoy message
                    
                else:
                    print("Thanks, Enjoy your wifi connection.")
                    

            # Using the else statement to get the different output    
            else:
                print("Thanks, Enjoy your wifi connection.")
            
        else:
            print("Thanks, Enjoy your wifi connection.")
            
    else:
        print("Thanks, Enjoy your wifi connection.")

    #Giving the option to the user if they want to restart it again
    restart = input("Do you wish to start again: ").lower()
    if restart == "yes":
        main()

    else:
        exit()
main()








    
