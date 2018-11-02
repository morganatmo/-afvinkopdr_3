#AFVINKOPDRACHT 3 - OPDRACHT 17
#Morgan Atmodimedjo BIN1a

no_wifi = "true"

while no_wifi == "true":
    
    print("Reboot the computer and try to connect.")
    wifi = input("Did that fix the problem? yes/no ")
    if wifi == "yes":
        no_wifi == "false"
 
    else:
        print("reboot the router and try to connect.")
        wifi = input("Did that fix the problem? yes/no ")
        if wifi == "yes":
            no_wifi == "false"
        else:
            print ("Make sure the cables between the router and modem are plugged in firmly.")
            wifi = input("Did that fix the problem? yes/no ")
            if wifi == "yes":
                no_wifi == "false"
            else:
                print ("Move the router to a new location.")
                wifi = input("Did that fix the problem? yes/no ")
                if wifi == "yes":
                    no_wifi == "false"
                else:
                    print ("Get a new router")
                    no_wifi == "false"
