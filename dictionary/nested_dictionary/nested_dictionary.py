print("\nNested Dictionary: Dictionary can contain other, which is useful for storing more complex data.\n")

# Nested dictionaries
employee = {
				"manager" : {"Name": "DINESHWAR", "Age":"36", "Dep": "BANKING","Sallary": 76000, 1: "Ratu road"},
				"engineer" : {"Name": "BHARAT RAM", "Age":"60", "Dep": "RAILWAY", "Sallary": 66000, 1: "Qowater B", "City": "PATNA"},
				"doctor" : {"Name": "SUDHER PARATAP","Age" :45, "Dep": "Daigonatics","Sallary":150000}
} # Nested Dictionaries 
print(employee) #  output: print will be Dictionary inside Dictionary

print()

# Access key value Nested Dictionaries bellow:-
#       Syntax:
#          employee["manager"]["Key_name"]
#          employee["engineer"]["Key_name"]

print(employee["manager"]["Name"])      # Output: DINESHWAR
print(employee["engineer"]["Name"])     # Output: BHARAT RAM
print(employee["doctor"]["Name"])     # Output: SUDHER PARATAP

print(employee["manager"]["Age"])       # Output: 36
print(employee["engineer"]["Age"])      # Output: 60
print(employee["doctor"]["Age"])      # Output: 45

print()

print(employee["manager"]["Dep"])       # Output: BANKING
print(employee["engineer"]["Dep"])      # Output: RAILWAY
print(employee["doctor"]["Dep"])      # Output: Daigonatics

print(employee["manager"]["Sallary"])   # Output: 76000
print(employee["engineer"]["Sallary"])  # Output: 66000
print(employee["doctor"]["Sallary"])  # Output: 150000
print()

print(employee["manager"][1])           #Output: Ratu road
print(employee["engineer"][1])          # Output: Qowater B
print(employee["engineer"]["City"])  	# Output: PATNA


