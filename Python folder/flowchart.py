a = 10
b = 20
c = 30

avg = (a+b+c)/3

print("avg = ", avg)

if avg > a and avg >b and avg > c:
    print("avg is higher than a, b, c ")

if avg > a and avg > b :
    print ("avg is higher than a, b")

if avg > a and avg > c:
    print("avg is higher than a, c")

if avg > b and avg > c:
    print ("avg is higher than b, c")

if avg > b:
    print("avg is just higher than b")

if avg > c:
    print("avg is just higher than c")

if avg > a:
    print ("avg is just higher than a")