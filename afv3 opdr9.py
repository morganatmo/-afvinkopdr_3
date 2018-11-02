#AFVINKOPDRACHT 3 - OPDRACHT 9
#Morgan Atmodimedjo BIN1a

p = int (input("What is your pocket number? (0-36) "))

#p stands for pocket
p_11 = range(1, 11)
p_19 = range(11, 19)
p_29 = range(19, 29)
p_37 = range(29, 37)

if p in range(0, 37):
    if p in p_11:
        if p % 2 == 0:
            print("your pocket is black")
        else:   
            print("your pocket is red")

    elif p in p_19:
        if p % 2 == 0:
            print("your pocket is red")
        else:
            print("your pocket is black")
            
    elif p in p_29:
        if p % 2 == 0:
            print("your pocket is black")
        else:
            print("your pocket is red")

    elif p in p_37:
        if p % 2 == 0:
            print("your pocket is red")
        else:
            print("your pocket is black")
            
    else:
        if p == 0:
            print("your pocket is green")


else:
    print ("ERROR. please fill in a number from 0-36")
