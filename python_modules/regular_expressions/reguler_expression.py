print("\nPython Regular Expressions are patter used to match character combinations in strings. before we can work with regular Expressions,import the re module first.-\n")

print("\nThe re.search() Method :-The re.search(regex,str) method search for the given regular expression from a given string."\
	" \nIf there is match,it return the match object of the first occurence. if there is no match, returns the None.\n")
import re

regExp = "HELLO"
tax = "HELLO WORLD"
match = re.search(regExp, tax)

print("index of the start and end position",match.span()) # span() method return the indices of the star and end position of the match.
print("index of the start position",match.start()) # start() method return the start position 
print("index of the end position",match.end()) # end() method return the end position.
print()

print("\nThe re.findall() Method:- The re.findall(regEx,str) method returns a list contains the matches found.")

regEx = "javascript"
tex = "I AM studies of javascript and java and javascript is papuler language, javascript demand high"
match = re.findall(regEx, tex)
print("Matched contains in list:",match)



print()
print("\nThe re.sub() Method:- The re.sub(regular Expression, replace,string) method replace the matches found in a string. It takes 3 parameters\n")

regEx = "javascript"
tex = "I AM studies of javascript and java and javascript is papuler language, javascript demand high"
replce = re.sub("javascript", "python", tex)
print("Matched:", replce)
print()

print("\nMetacharacters: to add more information for our search we can use Metacharacters. Metacharacters dont match themselves.")

regex ="^mango"
tex = "mango is sweet"
x = re.findall(regex,tex)
if x :
	print("The string start with 'mango'")
else:
	print("The string does not sart with 'mango'")
	
print()
regex ="mango$"
tex = "I love mango"
x = re.findall(regex,tex)
if x :
	print("The string start with 'mango'")
else:
	print("The string does not sart with 'mango'")

print()
x  = re.findall("[DIN]", "DINESHWAR")

print("Found repeat DIN:",x)

print()
x1  = re.findall("D", "DINESHWAR is 35 year olD, DEEPAK IS 30.")

print("Found repeat of D:",x1) # totale repeat

print()
x1  = re.findall("d", "DINESHWAR is 35 year olD, DEEPAK IS 30.")

print("Found repeat of d:",x1) # totale repeat