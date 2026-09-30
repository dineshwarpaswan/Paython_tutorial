print()
a=(10==10) and (8==8)
print("Type1 will be True:",a) # Result will be :True

x=(20==2)and(60==60)
print("Type2 will be False:",x) # Result will be :False

print()
a = 50
a=(a>45) and (80<a)
print("Type3 will be False:",a) # Result will be :False
print()

a = 60
a1=(a>20) and (45<a)	
print("Type4:",a1) #Result will be :True
print()

a1 = 20
if (a1==20) and (a1==15):print("Type5 will be True") # Result will be :True
else:
    print("Type 5 will be False") # Result will be :False
print()

x2=100
x3 = (x2 > 20) and (30 < x2)
if (x3):print("Type6 will be True:") # Result will be :True
print()

x4=45
if (x4 > 10) and (80 < x4):
   ("Type7, Result will be True:",x4) # Result will be :False
else:
    print("Type 7 will be False") # Result will be :False
	
print()
age=int(input("Enter the value LIKE 18 : "))
edu=str(input("Enter the Education LIKE MBA : "))
print()
if (age==18 and edu=="MBA"): 
    print("Both Data match, You can allowed  for Votting ") # If both same, Result will be :True
else:
    print("Data not match, You can't allowed for votting") # If both same, Result will be :True