print("\nUsing Logical Operators: We can use the and or operators with conditional statement.False.\n")
print("\nThe and operator returns True, if both expression(or boolean value) are True.")
# (False and False)= False, (False and True)= False, (True and True)= True
x =10	#Type 1
y = 15
if (x == 10 and y ==15):
	print("\nType 1, If both conditional is correct")# IF  both expression is correct, print will be :True


x1 = 100	#Type 2
y2 = 1000
if (x1 == 100  and y2 == 2000):
	print("\nType 2, yes, IF  both expression is correct ")# IF conditional is correct, print will be :True
	
else:
	print("Not both correct") # oterwise,IF  both  conditional is not correct, print will be :False

if (5>4) and (6<10): #Type 3
	print("\nType 3,Yes,") # IF  both conditional is correct, print will be :True


x4 = 100
if (x4 > 10) and (50 < x4):   # Type 4
	print("Type 4, print will be True:")  # IF  both conditional is correct, print will be :True
	
a =  (4>5 and 5<6) # Type 5
print("Type 5",a)  # print will be False

a1 = (15 == 15)and (10 == 10) # Type 6
print("Type 6",a1) # print will be True

