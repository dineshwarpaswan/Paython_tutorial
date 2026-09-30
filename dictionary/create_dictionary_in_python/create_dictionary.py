
print("\nMethod-1: We cteate a dictionary using curly braces{} and Separating keys and values with a colon.")
#Syntax:
#   dic = {"key1":"value","key2":"value2","key2":"value2",----}
person = {
			"Name": "DINESHWAR",
			"Father": "BHARAT",
			"Grend Father": "BHAVISAN",
			"Age":"36"
        } # Dictionary

print("\nThis is a Dictionary:",person) # print will be a Dictionary

print("\nWhich type of class:", type(person)) # Wich type of class 

# Empty dictionary {}
Empty_dic = {}
print("\nEmpty dictionary:",Empty_dic)

# Method-2: Using dict{} Constructor:
eployee = dict(Name = "DINESHWAR", Dignation = "SOFTWARE ENGINEER",Sallary = 56000, Dep = "IT SECTOR", City = "PUNE")
print("\nCteate a dictionary",eployee)
print("Which type of class:", type(eployee))
print()

# Method-3: Using a list of Tuples
emp = dict([("Name", "RAJESH"),("Dignation" ,"MANAGER"),("Sallary", 46000),("Dep", "BANKING SECTOR"),("City", "RANCHI")])
print(emp)
print("Which type of class:", type(emp))
