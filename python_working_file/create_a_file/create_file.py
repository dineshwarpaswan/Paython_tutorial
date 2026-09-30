
# close a file
#   using with statements
with open("demo.txt", "a") as file:
	content = file.write("Mera bharat desh mahan hai our hum ye ke log bhi") # demo.txt name ke file create kar diya 
	print(content)
	
	

