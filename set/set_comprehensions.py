print("\nSet Comprehension:- Set Comprehension allow concise and readable creation of sets. Similler to list comprehensions but for sets.Use Curly brsckets{}  \n")

# Characteristics of Set:
# . Unordered:- element have no define order. you can not access element by index.
# . Unique Elements:- no duplicate allow items. Each element must be distinct.
# . Mutable:- You can add or Remove element after creation.
# . Immutable Element:- Individual element inside a set cannot be modiffied


# Syntax:
# my_set = {expresssion for item in iterable if condition}
        # Squares = {x**2 for x in range(1,6)}


# exmple
    

Squares = {x**2 for x in range(1,6)}

print("\nThis is a Set Comprehension X**2: ", Squares) # output: {1, 4, 9, 16, 25}  

Squares1 = {x**3 for x in range(1,6)}

print("This is a Set Comprehension  x**3:",Squares1)

nums = [1, 2, 2, 3, 4, 4]

Unique_squares = {x**2 for x in nums}

print(Unique_squares)