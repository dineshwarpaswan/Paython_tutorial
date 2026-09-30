print("\nPython break and continue: The break and continue statements are commonly used in loops.\n")
print("The break Statement : The break statement stoop the execution of the current loop.\n")

mobile = ["i phone","Metrolla","Redmi","Nathing"]

for mob in mobile: # type 1
	print("Brand name:", mob) 
	if mob == "Redmi":
		break  #  all print karega
print()

mob = ["i phone","Metrolla","Redmi","Nathing"]
for mo in mob: # type 2
	if mo == "Metrolla":
		break
	print("\nData filter and matched wille be stoped:", mo) # step by step data filter and matched wille be stoped.

print()

	
for a in range(6):  # type 3
	if a == 4:
		break
	print("Hello", a) # filter and matched wille be stoped, print wille be : 0 - 3
	
print()

i = 0	# type 4
while i <= 6:
	if i == 4:
		break
	print("Hello friends", i)
	i += 1