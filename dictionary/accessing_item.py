print("\nA ACCESSING ITEMS: TO access an item, specify the key name of an item insid suareb rackets[].")
person = {"Name": "DINESHWAR",        # firt_key = Name, and value = DINESHWAR
         "Father": "BHARAT",          # second_key = Father, and value = BHARAT
		 "Grend Father": "BHAVISAN",  # Third_key = Grend Father, and value = BHAVISAN
		 "Age":36                     # fourth_key = Age, And value = 26
        }                             # Dictionary
		 
		 
print("\nThis is Dictionary:",person) # print will be a Dictionary
per = person["Name"]              # firt_key
pe = person["Father"]             # second_key
p = person["Grend Father"]        # Third_key
p1 = person["Age"]                # fourth_key


print("Firt_key  of value:", per)  # print will be firt_key of value
print("Second_key  of value :", pe) # print will be second_key
print("Third_key  of value :", p)   # print will be Third_key
print("Fourth_key  of value :", p1) # print will be fourth_key

print("\nType2, Key name of value:",person.get("Father")) # get() method used to an access item
print("Type3, Key name of value:",person.get("soon"),"\n") #if the specified  key is not found: get() method  will only return None,
            
print("Type3 This will raise an error:", person["city"]) # This will raise an error

 