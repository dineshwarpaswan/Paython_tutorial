
print("\nPython provide several built-in methods to use on dictionary.\n")
#Syntax:
#   dic = {"key1":"value","key2":"value2","key2":"value2",----}
#   dic.[key-name]

employee = {
			"Name": "DINESHWAR",
			"Father": "BHARAT",
			"Age":"36",
			"Dignation": "SOFTWARE ENGINEER",
			"Dep": "BANKING SECTOR",
			"Sallary": 76000,
			"City":"RANCHI",
			1: "Ratu road"
        } # Dictionary


# Returns a list containing the dictionary's keys
print("\n",employee.keys())    								 # All keys

# Returns a list of all values in the dictionary'
print("\n",employee.values())  								 # All values

# Returns a list containing a tuple for each key value pair'
print("\n",employee.items())    							# All key-value pairs

# Returns a dictionary with specifeid keys and value
print("\n",employee.fromkeys("Dep")) # argument pass krna padega nahi to erro dega

print("\nDictionary:",employee) # print will be a Dictionary

# Return value for a key( with a optional defult if key in missing).
print("\nAccess one key value:",employee.get("Name")) 
print("\nAccess one key value is missing:",employee.get("city")) # get() missing hone per erro nahi dega, balki: none dega
print("\nAccess key value is defult show:",employee.get("EMP_ID","0001")) #missing hone per defult value print karega: 0001

 

# Updates the dictionary with the specified key-value pairs
#print("\nAcces one key value update:",employee.update())

#print("\nDictionary:",employee) # print will be a Dictionary                                               
