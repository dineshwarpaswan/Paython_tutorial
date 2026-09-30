
import json


print("\nJSON file can be formatted or be prettied using the indent parameter of the json.dups() method.")


# Formatting a JSON


data = {"NAME":"DINESHWAR","DIG":"ENGINEER","AGE":35,"CITY":"BOKARO"}

print(json.dumps(data, indent = 4)) # indent = 4 whitespaces/ 4 TAB
print(type(json.dumps(data, indent = 4)))

print()

data1 = {
    "NAME":"BHARAT",
    "DIG":"ADVOCATE",
    "AGE":35,
    "CITY":"RANCHI"
    }

my_json1 = json.dumps(data1, indent = 20) # indent = 20 whitespaces
print("\nDictionary to JSON:", my_json1) 
print(type(my_json1))

print()

d = {
    "NAME":"KARAN PASWAN",
    "DIG":"MANAGER",
    "AGE":35,
    "CITY":"PATNA"
    }

my_json2 = json.dumps(d, indent = 2) # indent = 2 whitespaces
print("\nDictionary to JSON:", my_json2) 
print(type(my_json2))
