print("What is JSON: stand for javascript Object Notaion. JSON contain data that are sent or recieved to and from a server."\
"\n JSON is simple a string, it follows a format similer to a python dictionary.\n")

# exampel of  basic JSON

x = '{"NAME ":"DINESHWAR","AGE":35, "CITY":"BOKARO", "DIG":"ENGINEER"}'
print("basic JSON",x) #json values in string format 
print(type(x))
print()

x1 = {"NAME ":"DINESHWAR","AGE":35, "CITY":"BOKARO", "DIG":"ENGINEER"}
print("Dictionary is python :",x1) # python value is single qutation
print(type(x1))
