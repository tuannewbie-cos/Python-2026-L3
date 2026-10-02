#ex1
rad = float(input("Enter circle radius? "))
area = rad * rad * 3.14
print("Circle area = {:.1f}".format(area))

#ex2
c = float(input("Enter the temperature in Celsius?" ))
f = c*1.8 +32
print(f"{c} (C) = {f} (F)")

#ex3
num = int(input("Enter a number? "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(f"{num} is NOT a prime number")
            break

    else:
        print(f"{num} is a prime number")
else:
    print("input must be larger than 1")

#ex4
num = int(input("Enter a number? "))

#perfect number must larger than 0
if num <=0 :
    print(num,"is NOT a perfect number")
else:#num>0
    div = 0 #divisors
    for i in range(1,num):
        if num % i ==0:
            div +=i
    if div == num:
        print(num," is a perfect number")
    else:
        print(num,"is NOT a perfect number")


#ex5    
color = ["Red" ,"Blue", "Pink"]
fav = input("What is your favorite color? ")
if fav in color:
    print("Your color is at ",color.index(fav)+1,"in my list")
else:
    print("Sory, I could not find your color")

#ex6
range1 = list(range(7))
range2 = list(range(1,11,3))
range3 = list(range(5,0,-1))
range4 = list(range(6,-4,-2))
print(range1)
print(range2)
print(range3)
print(range4)

#ex7
#remove dollar sign
s = str(input("enter the price: "))
remove = "$"

for r in remove:
    s = s.replace(r, "")

print(s)

#ex8
list = list(map(int, input("Enter numbers separated by space: ").split()))
res = [num for num in list if num%2==0]
print(res)
        
#ex9
num = int(input("enter a number: "))
fac = 1
for i in range(1,num+1):
    fac = fac * i

print(fac)


#ex10
num = int(input("enter a number"))
for i in range(1,num):
    if num % i==0:
        print(i)

#ex11
import math

x1, y1 = map(float, input("Enter x1 y1: ").split())
x2, y2 = map(float, input("Enter x2 y2: ").split())

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance =", distance)

#ex12
col = int(input("cols? "))
row = int(input("row? "))
for i in range(row):
    s = ""
    for j in range(col):
        if i == 0 or i == row -1 or j == 0 or j == col - 1:
            s+= "* "
        else:
            s+="  "
    print(s)