def main():

    #Program to solve WIFI Connection Error

    import time
    a = input("If you are having problem with wifi connection, Use YES or NO ").upper()
    if(a=="YES"):
        print("Reboot the computer and try to connect")
        time.sleep(2)
        b = input("Did the fix that problem, use yes or no: ").upper()
        if(b=="NO"):
            print("Reboot the router and try to connect")
            time.sleep(2)
            C = input("Did the fix that problem, use yes or no: ").upper()
            if(C=="NO"):
                print("Make Sure your cables between the router and modem are pluged in firmly")
                time.sleep(2)
                d = input("Did the fix that problem, use yes or no: ").upper()
                if(d=="NO"):
                    print("Move the router to a new location and try to connect")
                    time.sleep(2)
                    e = input("Did the fix that problem, use yes or no: ").upper()
                    if(e=="NO"):
                         print("Get a new Router, Have a nice day")
                    else:
                        print("Thanks, Enjoy your wifi connection")
                        
                    
                else:
                    print("Thanks, Enjoy your wifi connection")
                    

                
            else:
                print("Thanks, Enjoy your wifi connection")
            
        else:
            print("Thanks, Enjoy your wifi connection")
            
    else:
        print("Thanks, Enjoy your wifi connection")


    restart = input("Do you wish to start again: ").lower()
    if restart == "yes":
        main()

    else:
        exit()
main()








    
