print("\nLOOPING THROUGH A DICTIONARY: Basically meances accessing its items one-by-one, the for loop Returns the key name of each item, allowing us to access them one-by-one.\n")

person = {"Aplicant_name": "DINESHWAR", # firt key_name = Aplicant_name, and value = DINESHWAR
         "Father_name": "BHARAT",     # second key_name= Father_name, and value = BHARAT
		 "Age":36  ,                  # Third key_name = Age , and value = 36
        } # Dictionary
		 
print("\nThis is Dictionary:",person) # print will be a Dictionary

for key in person:        # type1
    print("\nAccess Key_name:",key) # All data access form Dictionary step-by-step key_name 
	

for key in person:        # type2 
	print("\nAccess Key_value :", person[key]) # All data access form Dictionary step-by-step Key_value
	
	