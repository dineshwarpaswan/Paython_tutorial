
print("\nDictionary to JSON: - To convert a dictionary to a JSON, use the json.dumps() method. This method parses a Dictionary and returns a JSON in string."\
      "\nWe can access the dictionary a value.\n")


# Dictionary to JSON
import json

data = { 
			"NAME": "DINESHWAR",
			"DIG" : "ENGINEER",
			"AGE" : 35,
			"CITY" : "BOKARO"
		}

my_json = json.dumps(data)

print("\nDictionary to JSON:", my_json)


