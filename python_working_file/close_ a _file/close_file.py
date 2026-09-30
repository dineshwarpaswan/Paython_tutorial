
# close a file
#   using with statements
with open("demo.txt", "r") as file:
	content = file.read()
	print(content)


with open("demo.txt", "r") as file:
	content = file.readlines()
	print(content)
	
	

