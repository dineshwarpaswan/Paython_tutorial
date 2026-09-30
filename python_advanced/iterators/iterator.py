print("\nPython Iterators: An iterator is an object that allows you to traverse through a collection(like:- a lists,tuples, sets and even strings.\n")
 
numbers = [20,30,40,50] # list
# type 1
for num in numbers:
	print(num) # iterable/iterator<- ka matalb hai ki ak-ak kr ke nikalana ak bag se kuch object
	
print()

fruits = ("APPLE","MANGO","BANANA") # tuple
iterator = iter(fruits)
while True: # Type 2
	
	try:
		fruit = next(iterator) # advaced and fetches next item
	
		print("Result will be: ",fruit)
	
	except StopIteration:
		break # Exit loop when collection ends
		
print()		
# Type 3
pets = {"dog","cat","rabbit"} # set
pet = iter(pets)

print(next(pet))
print(next(pet))
print(next(pet))

print()		
# Type 4
text = "iterator" # string
for t in text:
	print(t)
	

	
