print("\nPython if else...Shorthand: A Shorthand if else..statement is used when you have one statement to execute.\n ")
# 	Syntax:
#		<on_true> if expression else <on_false>
print("To batter demonstrate this, lets convert an if else...statement to its shorthand version\n")

x = 100
if x == 100:			# type 1
	print("x is a 100")
else:
	print("x is not a 100")


# type 2
x1 = 200
print("\nx1 is a 200") if x1 == 200 else print("x1 is not 200")

# type 3
x2 = 400
print("x2 is a 400") if x2 == 40 else print("x2 is not 400")

# type 4
x3 = 300
str = "x3 is a 300" if x3 == 200 else "x3 is not 300"
print("\n", str)