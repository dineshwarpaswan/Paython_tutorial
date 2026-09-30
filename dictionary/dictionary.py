print("\nDictionary:- A Dictionary is an Unordered and mutable collection of items. \n"\
	"A dictionary is a data structure in python that stores data in key-value in pairs."
	"\nDictionary items(key-value) are ordered, changeble, and do not allow duplicates. used curly brackets{}.\n")


# A dictionary is a data structure in python that stores data in key-value in pairs."
# Dictionary items(key-value) are ordered, changeble, and do not allow duplicates.
# key: Must be unique and immutable (string,number,or tuples)
# value: can be any type and does not need to be unique.

# Method 1: we cteate a dictionary using curly braces{}. Separating keys and value with a colon.
person = {
			"Name": "DINESHWAR",
			"Father": "BHARAT",
			"Grend Father": "BHAVISAN",
			"Age":"36"
        } # Dictionary
		 
print("Wich type OF class:", type(person)) # Which type of class 
print("\nThis is a Dictionary:",person) # print will be a Dictionary

print()
# Access Unique Key Value-name
print(person["Name"])
print(person["Father"])
print(person["Grend Father"])
print(person["Age"])

print()

# Access ALL Key-Name
print("Key-Name:", person.keys())

print()

# Access All Value-Name
print("Value-Name:", person.values())


print()

#Iterable Key: With Help OF FOR LOOP
for keys in person:
	print("Iterable Key key Name:",keys)

print()
#Iterable Value: With Help OF FOR LOOP
for values in person:
	print("Iterable Value Name:",person[values])

print()
#Iterable Key,Value OF Items: With Help OF FOR LOOP
for key,value in person.items():
	print("Iterable keys with values:", key, value)





















