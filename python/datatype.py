# We are learning python variables and data types
a = 12
b = 1.5
c = 2j
d = "Hello"
e = [1, 2, 3, 4, 5] 

# we can use the type() function to check the data type of a variable
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
#list is a collection of items which is ordered and changeable. It allows duplicate members. List is defined by using square brackets [].
# l1 = [1, 2, 3, 4, 5]    # index start from left to right ( 0, 1, 2, 3, 4) # index from right to left (-5 -4 -3 -2 -1)
# l2 = [2,3.5,'kumar', 3.5]
# print(l1[0:3])  # this will print the first element of the list
# print(l1[2:])   # this will print the elements from index 2 to the end of the list
# print(l1[-2])

# l3 = [10,20,40,60,90]
# l3.append(100)   # this will add the element 100 at the end of the list
# print(l3)
# l3.insert(2,30)  # this will add the element 30 at index 2 of the list
# print(l3)
# l3.remove(40)   # this will remove the element 40 from the list
# print(l3)
# l3.pop(2)    # this will remove the element at index 2 from the list
# print(l3)
# l3.pop()     # this will remove the last element from the list
# print(l3)
# del l3

# import numpy as np

# arr1 = np.array([
#     [0,1,2],
#     [3,4,5],
#     [6,7,8]
#     ])
# print(arr1)
# import array
# arr2 = array.array('i', [1, 2, 3, 4, 5])  # 'i' is the type code for integers
# print(arr2[0])  # this will print the first element of the array
# arr2.append(6)  # this will add the element 6 at the end of the array
# print(arr2)

t1 = (1, 2, 3, 4, 5)  # tuple is a collection of items which is ordered and unchangeable. It allows duplicate members. Tuple is defined by using parentheses ().
print(t1[0])  # this will print the first element of the tuple
t2 = (0.5, 0.6, 0.7)
s1 = {"apple", "banana", "cherry"}  # set is a collection of items which is unordered and unindexed. It does not allow duplicate members. Set is defined by using curly braces {}.
print(s1)
# print(s1[0])  # this will give an error because set is unordered and unindexed

l5 = [1, 2, 3, 4, 5,1,2,3,4]
print(l5)
s2 = set(l5)  
print(s2)  # this will print the unique elements of the list l5
l5 = list(s2)  # this will convert the set s2 back to a list
print(l5)  # this will print the list l5 with unique elements only


d1 = {"name": "John", "age": 30, "city": "New York"}  # dictionary is a collection of items which is unordered, changeable and indexed. It does not allow duplicate members. Dictionary is defined by using curly braces {}.
print(d1.items())
print(d1.keys())
print(d1.values())
d1["address"] = "123 Main St"  # this will add a new key-value pair to the dictionary
print(d1)

d2 = {
"Student1": {"name": "Alice", "age": 20, "grade": "A"},
"Student2": {"name": "Bob", "age": 22, "grade": "B"},
"Student3": {"name": "Charlie", "age": 21, "grade": "A"}
}
print(d2["Student1"]["name"])  # this will print the name of Student1

# Structuredb -> textdb -> graphdb(movie) or vectordb 
# dictionary - > json - > yaml 