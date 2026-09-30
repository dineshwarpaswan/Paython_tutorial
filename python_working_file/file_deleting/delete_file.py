import os

# os.remove("blank.pdf")# <---- delet for file
# os.rmdir("all_data")   # <---- delet for folder

#Using: deletint file and folder with help of if..else

file = "blank.pdf"

if os.path.exists(file):

	os.remove(file) # <---- delet for file
else:
	print("Oops, the file does not exist!")



print()

folder = "all_data"

if os.path.exists(folder):

	os.rmdir(folder)  # <---- delet for folder

	print("Your folder was deleted!") 

else:
	print("Oops, the folder does not exists!")	
	

