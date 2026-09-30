print("\nPython break and continue: The break and continue statements are commonly used in loops.\n")
print("The continue Statement : The continue  statement terminates the execution of the current iteration of the loop. And  continue the execution of loop with the next iteration.\n")

mobile = ["i phone","Metrolla","Redmi","Nathing"]

for mob in mobile: # type 1
	if mob == "Redmi":
		continue
	print("Brand: ", mob) # filter and skeep continue all data wille be print
	

tax = "DINES"  # type 2
for t in tax: 
 
	if t == "N":
		continue
	print("\nMatched and skeep character:", t) # filter matched and skeep ,print wille be: all data
	


i = 0	# type 3
while i < 4:
	i += 1
	if i == 2:
		continue
	print("\nHello friends", i)  # filter and skeep data wille be print: all