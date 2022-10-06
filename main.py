# Declaring an empty list
list1 = []

#A list of numbers
list1=[90,95,92,97,99]
print(list1)

# Checking type

print(type(list1))

#Length of a list
print(len(list1))

# A list of strings
list2 = ["Dev", "Coding", "Classes"]
print(len(list2))
print(list2)

#Index of an element

print(list1.index(95))

print(list1[0])
print(list1[-1])


# Accessing the list element using Slice Operatror

#The slice operator(:) helps us to access the elements of the list within a range of specified index values.
print(list1[0:2])
print(list2[0:2])

#To get all the values of the list using slice operator we should specify the "stop index" one more than the length of the element.

print(list1[0:5])

#Slice Operator With Negative Index
print(list1[-5:-3])
print(list1[-4:-2])
