# Lists in Python : (mutable) a built-in data type that stores set of values.
marks1 = 94.4
marks2 = 87.5
marks3 = 95.2
marks4 = 66.4
marks5 = 45.1    # ye just samajhne

marks = [94.4, 87.5, 95.2, 66.4, 45.1]     # its a list
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])

# particular a student details (multiple data in a single list)
student = ["Karan", 95.4, 17, "Delhi"]
print(student)

# Strings : immutable (jo change nahi karsakte)
# Lists :   mutable  (jo change karsakte)
student = ["Karan", 95.4, 17, "Delhi"]
print(student[0])
student[0] = "Arjun"
print(student)

# LIST  SLICING (sublist)
marks = [85, 94, 76, 63, 48]
print(marks[1:4])

# LIST  METHODS.........
# list.append
list = [2, 1, 3]
list.append(4)    # append means adds 1 element at the end.
print(list)

# list.sort():  (sorts in Ascending order [1, 2, 3]) aur ye None dega
list = [2, 1, 3]
list = ['c', 'b', 'a']
print(list.sort())
print(list)

# list.sort(reverse=True): (sorts in Descending order [3, 2, 1])
list = ["banana", "mango", "apple"]
list = ['a', 'd', 'e', 'f', 'c', 'b']
print(list.sort(reverse=True))    # 3, 2, 1
print(list)

# list.reverse() : (reverse list...poori list reverse kardeta)
list = ['a', 'd', 'e', 'f', 'c', 'b']
list.reverse()
print(list)

# list.insert(idx, el) : insert element at index
list = [2, 1, 3]
list.insert(1, 5)
print(list)

# list.remove(1) : remove first occurance of element
list = [2, 1, 3, 1]
list.remove(1)
print(list)

# list.pop(idx) :  remove elements at index
list = [2, 1, 3, 1]
list.pop(2)
print(list)




# Tuples in Python: (immutable) isko change nahi karsakte
tup = (2, 1, 3, 1)
print(type(tup))
print(tup[0])
print(tup[1])

tup = (1,)    # tup me single value ko bhi (,) se likhna zaruri hai
print(tup)
print(type(tup))

# Tuple Methods
tup = (1, 2, 3, 4)   # tup.index(el)
print(tup.index(2))

tup = (1, 2, 3, 4, 2, 2)   # tup.count(el)
print(tup.count(2))


# PRACTICE
# (Q-1) WAP to ask the user to enter names of thier 3 favorite movies & store them in a list ?
movies = []
mov1 = input("enter first movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


# (Q-2) WAP to check if a list contains a palindrome of elements.(Hint: use copy() method)
# Palindrome = means jis list me shuru se aur akhir se same dikhai dete hai ex: rac-e-car

list1 = [1, 2, 1]  # palindrome and ["m", "a", "a", "m"] also a same.
list2 = [1, 2, 3]  # non-palindrome
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")


# (Q-3) WAP to count the number of students with the "A" grade in the following tuple ?
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))


# (Q-4) Store the above values in a list & sort them from "A" to "D" ?
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
