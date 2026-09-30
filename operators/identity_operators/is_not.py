print()
x = [1,2,3]
y = [1,2,3]

print("Type1 will be True: ",x is not y) # print will be: True 


z = x
print("Type2 will be True: ", x is not z ) #  print will be: True 
print()

a = [2,3,4]
b = [2,3,4]

print(a is not b ) # print will be: True

c = b
print("Type3 will be False: ",b is not c) #  print will be: False

d = [4,5,6]
e = [5,6,7]
print("Type4 Will be True: ",d is not e)  # print will be: True 


