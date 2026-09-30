print("\nREMOVING AN ITEMS: TO Remove a item ,use the pop() method, Remove an item with the specified key name.")

person = {"Aplicant_name": "DINESHWAR", # firt key_name = Name, and value = DINESHWAR
         "Father_name": "BHARAT",     # second key_name= Father, and value = BHARAT
		 "Age":36  ,                  # Third key_name = Age , and value = 36
        } # Dictionary
		 
print("\nThis is Dictionary:",person) # print will be a Dictionary

person.pop("Age")     #Key atributs will be Removed in Dictionary.
person.pop("Father_name") #Key atributs will be Removed in Dictionary.

print("\n2 Key atributs will be Removed in Dictionary:", person)  # 2 Key atributs will be Removed.

print("\nANOTHER WAY TO REMOVING AN ITEMS IS TO USE THE DEL KEYWORD, use the del() method, delete an item with the specified key name.")

del person['Aplicant_name']
print("\nAll data will be Removed form Dictionary:", person)  # Dictionary WIIL BE Empty
