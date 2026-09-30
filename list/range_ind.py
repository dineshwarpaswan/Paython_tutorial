print("\nRange Indexes by using a colon(:), We can acces a range  of items at one in list, using square brackets(object[1:3]).\n")

fruits = ["banana","orange","apple","mango","greps"] # in this Example :- using square brackets(object[-1]).
print(fruits) # print will be :list
print()
print("This fruit:",fruits[1:3])
print("This fruit:",fruits[2:4])
print("This fruit: ",fruits[3:5])
print("First se four tak print will be fruits: ",fruits[:4]) # First se four tak print will be
print("Skeep of banana,orange Fruits: ",fruits[2:]) # skeep of banana,orange,all will be: apple,mango,greps
a= fruits[1:5]
print(a)

print()

mix = ["dog",108, True,8.0,False] # Type 2 mix indexing list
print(mix) # print will be :list
print()
a1= mix[1:] #  Skeep of dog  all will be print: 108, True,8.0,False
print("Skeep of dog",a1)
a1= mix[3:]
print("Skeep of dog,108,True will be: ",a1)