print("\npython Class and Objects:- in pythan,everything is an object. A class helps us create objects.\n")
print("Creating A Class:- use the class keyword to create a class.")

# Here is the Syntax:
#	class className:
#		statement(s)

print("\nExmple here class:") 
#class Person():
#	fst_name = "dineshwar"
#	title_name = "paswan"
#	age = 35
	
print("instantiating a class:- now we can create a object from that class by instantiating a class it. To instantiate a class, add round brackets() to  its class name\n")

#obj = person() <--instantiating a class

class Person: # class name
	fst_name = "dineshwar"
	title_name = "paswan"
	age = 35
	
obj = Person() # <--instantiating a class
# access its properties
print(obj.fst_name)
print(obj.title_name)
print(obj.age)

print([obj.fst_name,obj.title_name,obj.age])
obj.fst_name = "BHARAT" # replce will be 
print("\nBHARAT Replce of dineshwar:", obj.fst_name) # BHARAT Replce of dineshwar:
print([obj.fst_name,obj.title_name,obj.age])