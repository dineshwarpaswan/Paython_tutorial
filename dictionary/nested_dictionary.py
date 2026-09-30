print("\nNESTED DICTIONARY: A Dictionary can contain another dictionary, to access an item in a nested Dictionary, access the key name of the dictionary.\n")

officer = {
        
		"Enginer":{"Name": "DINESHWAR PASWAN", "AGE": "35", "live": "BOKARO"},
		"Manager":{"Name": "BABLU PASI", "AGE": "45","live": "PATNA"},
		"Doctor":{"Name": "SUDHIR", "AGE": "60","live": "TATA"}
		
	} # nested Dictionary-> is dictionary ke under sub dictionary ko nested Dictionary kaha jata hai,
print("\nThis is NESTED Dictionary:",officer) # print will be a NESTED Dictionary

print("\nAccess Name: ", officer["Enginer"]["Name"]) # print will be key value
print("Access Age: ", officer["Enginer"]["AGE"]) # print will be key value
print("Access live: ", officer["Enginer"]["live"]) # print will be key value

print("\nAccess Name: ", officer["Manager"]["Name"]) # print will be key value
print("Access Age: ", officer["Manager"]["AGE"]) # print will be key value
print("Access live: ", officer["Manager"]["live"]) # print will be key value

print("\nAccess Name: ", officer["Doctor"]["Name"]) # print will be key value
print("Access Age: ", officer["Doctor"]["AGE"]) # print will be key value
print("Access live: ", officer["Doctor"]["live"]) # print will be key value



