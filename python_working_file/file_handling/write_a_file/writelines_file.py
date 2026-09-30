print("\nWrite to a File:- TO write to  a file,you can use the write() or writelines() methods:"\
	"\n.write(): Writes a string to  the file."\
	"\n.writelines(): Writes a list of string.")


#	Syntax:-
#		 file_object = open("fileName", "mode")


# Exmple: Writing to a file 
read_file = open("blank.txt", "a") # <---open karega our last me add kardega

read_file.writelines("\nmera mahan bhat i loVe india because india is asgest countory") # <---add ho jayega last me
#read_file = open("blank.txt", "r")
#read =read_file.read()
print(read_file)
read_file.close()

