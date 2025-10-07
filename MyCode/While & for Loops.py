# # Loops are used to repeat instructions.
# while True:
#     print("hello")  # it will print infinetly

count = 1
while count <= 5:
    print("hello")
    count += 1

# want to print numbera 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1
print("loop ended") 

# (Q-1) Print numbers from 1 to 100 ? 
i = 1
while i <= 100:
    print(i)
    i += 1

# (Q-2) Print numbers from 100 to 1
i = 100
while i >= 1:     # Stopping condition
    print(i)
    i -= 1

# (Q-3) Print the multiplication table of a number n(4x1 = 4).
i = 1
while i <= 10:
    print(4*i)
    i += 1

# (Q-4) Print the elements of the following list using a loop ?
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])   #nums[0], nums[1], nums[2]...
    idx += 1

# (Q-5) Search for a number x in this tuple using loop:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36
i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
    i += 1


#  BREAK and CONTINUE 
i = 1    # Break
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("end of loop")

# Continue acts as SKIP (current iteration ko rok ke aage loop ki taraf badjata hai)
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

# FOR LOOP
nums = [1, 2, 3, 4, 5]
for val in nums:
    print(val)

# (Q-1) Print the elements of the following list using a loop ?
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in nums:
    print(el)

# (Q-2) Search for a number x in this tuple using a loop ?
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
    idx += 1

#   RANGE():
# return a sequence of nums, starting frm 0 & increment by 1, and stops before a specified num.
seq = range(10)  # range(stop)
for i in seq:
    print(i)

# RANGE: (start, stop, step)
for i in range(2, 10):    #range(start, stop)
    print(i)

for i in range(2, 10, 2):    #range(start, stop, step(yane 2 se increase karna))
    print(i)

# (Q-1) Print numbers from 1 to 100 ?
for i in range(1, 101):
    print(i)

# (Q-2) Print numbers from 100 to 1 ?
for i in range(100, 0, -1):
    print(i)

# (Q-3) Print the multiplication table of a number n ?
n = int(input("enter number"))
for i in range(1, 11):
    print(n * i)   # enter any table number

#  PASS STATEMENT: pass is a null stmnt that does nthng. it is used as a Placeholder for future code.
for i in range(5):
    pass
print("some useful work")

# (Q-1) Find the sum of first n numbers. (using while)
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =", sum)

# (Q-2) Find the Factorial of first n numbers. (using for)
# factorial 5 matlab  [1*2*3*4*5], final num
num = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)


