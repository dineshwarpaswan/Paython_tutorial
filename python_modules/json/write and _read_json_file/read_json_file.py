import json


# Read JSON from file.

with open("employee.json", "r") as file:
    load_data=json.load(file)
    
print("\nData Read from employee.json:",load_data)
print(type(load_data))
print()
# Access its json values
print("YOUR NAME:",load_data["NAME"])
print("YOUR CITY NAME:",load_data["CITY"])
print("NOW YOU LANGUAGE:",load_data["LANGUAGE"])



