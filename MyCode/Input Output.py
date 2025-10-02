print("Bismillah")
print("hello world")

print("Afreen is my name")
print("my age is 30")

### We can print this in same line
print("Afreen is my name.", "my age is 30.")

# We can print numbers as well
print(29)
print(30+30)

# VARIABLES: jiski value change hosakti hai.  name , age, price are variables
    # A variable is a name given to a memory location in a program. (defination)
name = "AFREEN"    # STRING type
age  = 30          # INTEGER 
price= 29.99       # FLOAT
print(type(age))

print(name)   # yaha cotes use nahi honge bcz mujhe name ki value print karani hai nake name.
print("My name is:" , name)

# RULES OF IDENTIFIERS (VARIABLES OF NAMES)
      # 1.we cant use @ , % in variable names   2.  we cant start a variable name with any digit.viable1 is valid not 1variable  3.variables can have to be simple and short.

# PRIMARY DATA TYPES:   1. String  2.Integers  3.Float  4.Boolean  5.None
name = "afreen"
age  =  30
price = 29.99
old  =  False 
a    =  None
print(type(old))

# KEYWORDS : are reserved in Python ex: True, while....   We cannot use keywords as variable names
  # Python is a case sensitive language:  A  a

# PRINT SUM
a = 5
b = 5
sum = a+b
print(sum)
diff = a-b
print(diff)

# COMMENTS IN PYTHON :  #  or  """   """(for multiple lines....ctrl /)

# TYPES OF OPERATORS :
   # Arithmatic Operator
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # reminder gives
print(a ** b) # a^b power

# Relational / Comparison Operator  ( equal to: ==     ,  not equal to  != )gives Boolean value ( T/F )
a = 50
b = 20
print(a == b) # False
print(a != b) # True
print(a >= b) # Means a > b ans True
print(a <= b) # Means a < b ans False

# Assignment Operator
num = 10
num = num + 10 # 10 + 10 = 20
num += 10      # 10 + 10 =20 (shortform)
num -= 10      # 10-10 = 0
num *= 10     #  10 * 10 = 100
num /= 10     #  10 / 10 = 1
num %= 10     #  10 % 10 = 1
num **= 10    #  10^10 = 200000

print("num :", num)

# Logical Operators : not , and , or will work on boolean values
a = 50
b = 30
print(not False)   # true
print(not True)    # false
print(not a > b)   # true

val1 = True
val2 = True
print("AND operator :" , val1 and val2)
print("OR operator :" , val1 or val2)

# Type conversion
a = 2
b = 4.25
sum = a + b  # 2.0 +  4.25 = 6.25
print(sum)

# INPUT
name = input("enter your age")
print("you entered :" , name)

first = input("4")
second = input("3")
sum = (first + second)








