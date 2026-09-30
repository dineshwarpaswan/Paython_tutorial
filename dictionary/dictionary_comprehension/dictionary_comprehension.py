print("\nA Dictionary comprehension allow you to create Dictionaries in a concise way.\n")



#  Syntax:
#    new_dic = {key_expression: value_expression for item in iterable if condition}


# Example: Create a dictionary with square numbers

myResult_dict = {x: x*x for x in range(1,6)}     

print("\nSquare in dictionary:",myResult_dict)  	# Output: {1,:1, 2: 4, 3: 9, 4: 16, 5: 25}
print()

myResult_dict = {x: x+x for x in range(1,11)}     

print("Additio in dictionary:",myResult_dict)  	# Output: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}
print()
myResult_dict = {x: x-x for x in range(2,10)}
print("Substracion in dictionary:",myResult_dict) #Output: {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
print()

myResult_dict = {x: x**2 for x in range(1,10)}
print("Square in dictionary:",myResult_dict)    # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
print()

myResult_dict = {x: x**3 for x in range(1,10)}
print("Square 3 in dictionary:",myResult_dict)  #Ouput: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
