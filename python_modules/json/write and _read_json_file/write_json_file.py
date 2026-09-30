import json

# Creat amd Write JSON file

data = {

	"NAME": "DINESHWAR",
	"AGE": 35, 
	"CITY": "BOKARO",
	"LANGUAGE": ["ENGLISH","HINDI","BHOJPURI"], 
	"DIG": "ENGINEER"
}

with open("employee.json","w") as file:
    json.dump(data,file) # JSON file in string format

print("Data written to employee.json")

