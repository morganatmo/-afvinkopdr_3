#AFVINKOPDRACHT3 - OPDRACHT 1
#Morgan Atmodimedjo BIN1a

#g staat voor getal
g = int (input("geef een getal "))

if g < 0:
    print("het getal is negatief")
elif g > 0:
    print("het getal is positief")
    if g % 2 == 0:
        print(" en even")
    else:
        print(" en oneven")
else:
    print("het getal is nul")

