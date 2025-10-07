# ##  DICTIONARY and SETS :

# # Dictionaries are used to store data values in key:value pairs.
# # They are unordered, mutable(changable) & dont allow duplicate keys.

# info = {
#     "key" : "value",
#     "name" : "Afreen",
#     "learning" : "Coding",
#     "subjects" : ["python", "C", "java"],  # list
#     "topics" : ("dict", "set"),  # tuple
#     "age" : "30",
#     "is_adult" : "True",
#     "marks"  : 94.4
# }
# print(type(info))


# ## DICTIONARY IN Python :  Nested Dictionaries (Dict ke andar ek aur dict ko nested kehte hai)

# student = {
#     "nmae" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "maths" : 95
#     }
# }
# print(student)      #Nested dictioanry


# ## DICTIONARY METHODS : .........5

# #1 myDict.keys() : # will return all keys
# student = {
#     "nmae" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "maths" : 95
#     }
# }
# print(student.keys())   # return dict_keys


# #2 myDict.values() :  # will return all values
# student = {
#     "nmae" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "maths" : 95
#     }
# }
# print(student.values())   # called dict values


# #3 myDict.items() :  # return all (key, val) pairs as tuples
# student = {
#     "nmae" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "maths" : 95
#     }
# }
# print(student.items())  # will return in ()


# #4 myDict.get("key") :  # return the key according to value.
# student = {
#     "nmae" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "maths" : 95
#     }
# }
# print(student["nmae"])
# print(student.get("name"))


# #5 myDict.update( newDict ):  #inserts the specified items to the dictionary
# student = {
#     "nmae" : "rahul kumar",
#     "subjects" : {
#         "phy" : 97,
#         "chem" : 98,
#         "maths" : 95
#     }
# }
# student.update({"city" : "delhi"})
# print(student)


# ###   SETS IN PYTHON:  ********

# # -Set is the collection of the unordered items. (stores unique val)
# # -Each element in the set must be unique & immutable(unchangable)
# collection = {1, 2, 4, 3, 4, "hello", "ya", "ya" }  # will ignore same double inputs
# print(collection)
# print(type(collection))

# collection = set()  # empty set: syntax
# print(type(collection))


# ## Set Methods............6
# # Sets are mutable  but  set_elements are immutable

# #1 set.add(el) : #adds an element
# # we cannot add list in sets and Hashable values means immutable val
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)  # will set remove this 
# collection.add("check")
# collection.add((1, 2, 3))

# print(collection)

# #2 set.remove(el)  #removes the element an
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2) # will not print this duplicate value

# collection.remove(1)
# print(collection)

# #3 set.clear()    # empties the set
# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2) 
# collection.add("check")
# collection.add((1, 2, 3))

# collection.clear()       # will print 0
# print(len(collection))   # will print 4

# #4 set.pop()   # revomes a random value means will print random value
# collection = {"hello", "whats_up", "world", "coding"}

# print(collection.pop())
# print(collection.pop())

# #5 set.union( set2 )  #combines both set values & returns new
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.union(set2))  # 2 & 3 will print only once
# print(set2.union(set2))  

# #6 set.intersection( set2 )  # combines common values & returns new
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.intersection(set2))  #{2, 3}


## Practice Questions
#(Q-1) Store following word meanings in a python dictionary :

dictionary ={
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]  # here multiple val can store as list or tuple
}
print(dictionary)

#(Q-2) U are given a list of subjects for students. Assume one classroom is required for 1 subject.
   # How many classrooms are needed by all students ? (we need 5 classrooms)
subjects = {
    "python", "java", "c++", "python", "javascript", "java"
    "python", "java", "c++", "c"
}
print(subjects)
print(len(subjects))

#(Q-3) WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
  # Start with an empty dictionary & add one by one. Use subject name as key & marks as value ?
marks = {}

x = int(input("enter phy :"))
marks.update({"phy" : x})


x = int(input("enter math :"))
marks.update({"math" : x})


x = int(input("enter chem :"))
marks.update({"chem" : x})

print(marks)

#(Q-4) Figure out a way to store 9 & 9.0 as separate values in the set.
  # (You can take help of built in data types) ?
values = {9, "9.0"}     # (matlab python dono ku as 9 hi lega so take as string)
print(values)           # samajhne

values = {
    "float" : "9.0",
    "int" : "9"
}
print(values)

























