number = 50
if not number % 2:
    print("Even number")
else:
    print("Odd number")

# Name legnth
name = input("enter your name : ")
print("legnth of your name is" , len(name))

# Find the occurance of $ in a string
str = "Hi, Iam the $ symbol 99.9$"
print(str.count("$"))

## CONDITIONAL STATEMENTS      IF , ELIF , ELSE
age = 21
if(age >= 18):            # to print if stmnt so if condition must be TRUE
    print("can vote & apply for license")

# Traffic lights example
light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):    # whenever we use elif we must have 1 if statement at first
    print("go")
elif(light == "yellow"):   # if any statement true then further will not print
    print("look")
   
# we can use 2 if stmnts then both will print but for elif print if must be false
num = 5
if(num > 2):
    print("greater than 2")
if(num > 3):
    print("greater than 3")
elif(num > 3):
    print("greater than 3")   

# ELSE  statement
light = "pink"
if(light == "red"):
    print("stop")
elif(light == "green"):    
    print("go")
elif(light == "yellow"):   
    print("look")
else:                     # else will print when all if and elif statements become false
    print("light is broken")

## NESTING (means if statement me ek aur if )
age = 95
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")

# Even and Odd numbers ?
num = int(input("enter number: "))
rem = num % 2
if(rem == 0):
    print("EVEN")
else:
    print("ODD")

# Find the greatest numbers entered by user ?
a = int(input("enter first number: "))
b = int(input("enter second  number: "))
c = int(input("enter third  number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third is largest", c)

# Check if a number is a multiple of 7 or not
x = int(input("enter number: "))
if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")