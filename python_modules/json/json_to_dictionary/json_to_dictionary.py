
print("\nJSON to Dictionary: - To convert from to json to dictionary, use the json.loads() method. This method parses a json and returns a dictionary."\
      "\nWe can access the dictionary a value.\n")
# Dictionary
data = { "NAME ":"KIRISNA",
         "AGE":30,
         "CITY":"DHANBAD",
         "DIG":"DOCTOR"
         }

print("\nDictionary:",data)
print(type(data))
print()

# JSON to Dictionary 1 
import json

x = '{"NAME": "DINESHWAR", "AGE": 35, "CITY": "BOKARO", "DIG": "ENGINEER"}'
my_json = json.loads(x) 

# Access its values just like in a dictionarY
print("YOUR NAME:", my_json["NAME"])
print("YOUR AGE:", my_json["AGE"])
print("YOUR DIGNATION:", my_json["DIG"])
print("LIVE YOU CITY:", my_json["CITY"])
print(my_json)  # python values in single qutetion
print(type(my_json))
print()

# JSON to Dictionary 2
x1 = '{"NAME": "RAMESH", "AGE": 50, "CITY": "RANCHI", "DIG": "MANAGER"}'
my_json = json.loads(x1)

# Access its values just like in a dictionary
a = my_json["NAME"]
b = my_json["AGE"]
c = my_json["CITY"]
d = my_json["DIG"]

print("YOUR NAME:", a)
print("YOUR AGE:", b)
print("YOUR DIGNATION:", d)
print("LIVE YOU CITY:", c)
print(my_json)  # python values in single qutetion
print(type(my_json))

