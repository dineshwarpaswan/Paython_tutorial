print("\nRead From a File:-Once s a file open ,you can read from it using the followingmethods:"\
	"\n.read(): reads the entire content of the file."\
	"\n.readline(): reads one line form the file at a time."\
	"\n.readlines(): reads all lines into a list.\n")


#	Syntax:-
#		 file_object = open("fileName", "mode")


# Exmple: Reading the entire file
file = open("file_handling.txt", "r")

txt_file = file.read()

print(txt_file)
file.close()

print()

# Exmple: Reading one line at a time.
file_re = open("file_handling.txt", "r") 
line = file_re.readline()  # <---first line print karega

print("Only First line print:",line)
file_re.close()


# Exmple: Reading all lines a list.
read_file = open("file_handling.txt", "r")

files = read_file.readlines() # <--all line print: in a list 

print("\nAll line Print in a List:",files)
read_file.close()
