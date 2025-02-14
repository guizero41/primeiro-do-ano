# Arrays (we'll use the numpy libray)
import numpy as np 

#Creat an array
array = np.array([1, 2, 3, 4, 5])
print("array:", array)

# Acessing elements
print("First element:", array [0])
print("First element:", array [-1])

# Slicing
print("elements from 1 to 3:", array[1:3])

#lists
my_list = [1, 2, 3, 4, 5]
print("list:", my_list)

#append an element
my_list.append(6)
print("list after append:", my_list)

# Insert an element at a specific position
my_list.insert(2, 7)
print("list after insert:", my_list)

# Remove an element
my_list. remove(4)
print("list after remove:", my_list)

# tuples
my_tuple = (1, 2, 3, 4, 5)
print("tuple:", my_tuple)

#acessing elements (same as list)
print("First element:", my_tuple[0])
print("lest element:", my_tuple[-1])

#loops
#For loops
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
i = 0
while 1 < 5:
  print(i)
  i += 1

# looping over a list white indices 
my_list = [1, 2, 3, 4, 5]
for i, element in enumerate(my_list):
    print(f"index {i}: {element}")