print()
print("for loop ko use multiple data ko print karane keliye use kiya jata hai, for loop ko list/tuple/director me use bidaout range ke  kiya jata hai ")
print("program number: 1")
lists= ['apple','sony','sammsung','metrola','intex','gorila','micromax','redmi','relemi','jio']
ind=0
for i in lists:
    print(ind,i)
    ind+=1
print("This type of: ",type(lists))

print()
print("Program Number: 2")
val=('Laptops','Computers','Radios','TVs','Mobiles')
for index, i in enumerate(val):
    print(index, "This is an electronice device name: ",i)  
print("This type of:",type(val))

print()
print("Program Number: 3")
data= {'Mobile':'Sony','TV':'LG','Laptop':'Apple'} 
for index, (key, value) in enumerate(data.items()):
    print(index , key +': Brand Name of: '+value)
print("This type of:",type(data))
print()

print("Program Number: 4")
data= {'Mobile':'Sony','TV':'LG','Laptop':'Apple'} 
for key, value in data.items():
    print(key,"\tBrand Name of: ",value)
print()

print("Program Number: 5")
data= {'Mobile':'Sony','TV':'LG','Laptop':'Apple'} 
for value in data.values():
    print("Dictionary of value : ",value)
print()

print("Program Number: 6")
data= {'Mobile':'Sony','TV':'LG','Laptop':'Apple'} 
for key in data.keys():
    print("Dictionary of key: ",key)
print()

print("Program Number: 7")
data= {'Mobile':'Sony','TV':'LG','Laptop':'Apple'} 
for i in data.items():
    print("This result in tuple: ",i)
print()

print("Program Number: 8")
itam= {'Mobile':'Sony','TV':'Metrola','TabletS':'Gorila','headphon':'Sammsung'}
for index, (key, value) in enumerate(itam.items()):
    print (index, key+': brand name of: '+value)
print()

print("Program Number: 9")
colors = ["red", "green", "blue", "purple"]
for b in range(len(colors)):
    print(colors[b])