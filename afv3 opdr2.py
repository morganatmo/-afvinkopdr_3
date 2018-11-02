#AFVINKOPDRACHT 3 - OPDRACHT 2
#Morgan Atmodimedjo BIN1a

r = 1  #teller
area_big = 0  #grootste oppervlakte
greater = 0  # naam van grootste oppervlakte

while r <= 2:
    print("rectangle ", r)
    length = int(input("what's the rectangle's length? "))
    width = int(input("what's the rectangle's width? "))
    area = length * width
    if area > area_big:
        greater = r
        area_big = area
        print ("rectangle", greater, "has the greater area")
    else:
        if area == area_big:
            print("both rectangle's have the same area") 
    r += 1

print ("rectangle", greater, "has the greater area")
