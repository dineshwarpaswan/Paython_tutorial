print()
x = [1,2,3]
y = [1,2,3]

print("Result1 will be False: ",x is y) # False
print("Result2 will be True: ",x == y) # print will be: True

z = x
print("Result3 will be True: ", x is z ) # True
print()

a = [2,3,4]
b = [2,3,4]
print(a == b)#  print will be: True
print(a is b ) # print will be: False
c = b
print("Result6 will be True: ",b is c) #  print will be: True

d = [4,5,6]
e = [4,5,6]
print("Print7 Will be false: ",d is e)  # print will be: False
print("Print8 Will be True: ",d == e)  # print will be: True