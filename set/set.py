print("\nSET:- A set is collection of unique items in python. Set do not allow duplicate items. Use Curly brsckets{}  \n")

# Characteristics of Set:
# . Unordered:- element have no define order. you can not access element by index.
# . Unique Elements:- no duplicate allow items. Each element must be distinct.
# . Mutable:- You can add or Remove element after creation.
# . Immutable Element:- Individual element inside a set cannot be modiffied

# Use Curly brsckets{}
my_set = {1,2,3,4,5}
print(f"This is a set :{my_set}") # print will be set
print(f"type of class: {type(my_set)}") # print will be <class 'set'>

# Using the set() Constructor
my_set = set([1,2,3,4])
print(f"list convert in set: {my_set}") # list convert in set

my_set = set()
print("empty set: ",my_set)

fruit = {"banana","greps","manago","apple"}
print(type(fruit)) # print will be <class 'set'>

print("\nThis is Set: ",fruit) # print will be set

mix = {"aple",54,5.08,"ram",True}
print("\nThis is a set of mix:",mix)

A= {50,65,70,80,90,100}  
print("\nTHis is a set of digit:",A)  
