print("Hello welcome to you first calculator program ")
print(" You are about to perform some calculation")

option = int(input ("Please enter 1-5 to chose an option: "))

#print("You chose an addition")
num1 = int(input("Please enter a number "))
num2 = int(input("Please enter another number "))
   # num1, num2 = input("Please enter 2 numbers separated with comma")
if option == 1:   
    add = num1 + num2

    if add > 0:
        print ("your result is : ", add)
    else:
        print ("zsa")

if option == 2:
    #print("You chose a substraction")
   
    sub = num1 - num2

    if sub > 0:
        print ("your result is: ", sub)
    else:
        print ("zsa")

if option == 3:
    #print("You chose a division")

    div = num1 / num2

    if div > 0:
        print ( "your result is: ", div)
    else:
        print ("zsa")

if option == 4:
    #print("You chose a multiplication")
    
    mult = num1 * num2

    if mult > 0:
        print ( "your result is : ", mult)
    else:
        print ("zsa")
    
if option == 5:
    #print("Now calculate the average")
    num3 = int(input("Please enter a number "))
    num4 = int(input("Please enter another number "))
    
    avg = (num1 + num2+num3+num4) / 4

    if avg >= 0:
        print ("the average is: ", avg)
    else:
        print ("zsa")