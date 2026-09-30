print("for loop ko use multiple data ko print karane keliye use kiya jata hai, for loop ko l  use range ke thurogh kiya jata hai ")
val=5
for i in range(val):     # (start to end) 
    print(i)             # print (0 to 4) tak hamesa last se -1 karega 0,1,2,3,4
print()                  # blank space ke liye use kiya jata hai

for i in range(2,6):          #(start,stop,) 
    print(i)                  #yaniki print karega (2,3,4,5)
print()                       # blank space ke liye use kiya jata hai

for i in range(2,10,3):           #(start,stop,step) 
    print(i)                     #yaniki print karega (2,5,8)
print()                      # blank space ke liye use kiya jata hai

v = ('Ram','Sam','Biki','Kirish','Rahul')
for i in v:         # for loop ko use multiple data ko print karane keliye use kiya jata hai, for loop ko list/tuple me use bidaout range ke  kiya jata hai
    print(i) 
    
print(type(v))          # class ka nam pata karne ke liye use kiya jata hai

print()                 # blank space ke liye use kiya jata hai
print("for loop ko use multiple data ko print karane keliye use kiya jata hai, for loop ko list/tuple/director me use bidaout range ke  kiya jata hai ")


lists= ['Apple','Sony','Sammsung','Metrola','Intex','Gorila']
for i in (lists):
    print(i)
print(type(lists))
print()

itam= {'Mobile':'Sony','TV':'LG','Laptop':'Apple'}
for index, (key,value) in enumerate(itam.items()):# for key, value, index in mydict.items(): 
    print (index,value+': '+ key)  # print(index,value,key)