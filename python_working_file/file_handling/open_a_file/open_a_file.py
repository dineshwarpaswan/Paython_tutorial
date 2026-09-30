print("\nOpen a file: the open() function allow  us to read, create and update files")


#	Syntax:-
#		 file_object = open("fileName", "mode")

# example:-		file = open("example.txt", "r")

# Exmple: Open a file: Opening a file for reading
file = open("example.txt", "r")

print("\n",file)
file.close()
