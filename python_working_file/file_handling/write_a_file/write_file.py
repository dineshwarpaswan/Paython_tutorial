print("\nWrite to a File:- TO write to  a file,you can use the write() or writelines() methods:"\
	"\n.write(): Writes a string to the file."\
	"\n.writelines(): Writes a list of string.\n")


#	Syntax:-
#		 file_object = open("fileName", "mode")

# Exmple: Writing to a file (overwriting existing content).
file = open("blank.txt", "w")

file.write("\nMY COUNTRY IS LAGEST IN THE WORLD.")
file = open("blank.txt", "r")
f =file.read()
print(f)
file.close()


# Exmple: Appending to a file(add line to the end).
file_open = open("blank.txt", "a") 

file_open.write("\nand I am software engineer") # <---add ho jayega last me

file_open = open("blank.txt", "r")
f = file_open.read()
print(f)
file_open.close()

#close a file: file.close()

