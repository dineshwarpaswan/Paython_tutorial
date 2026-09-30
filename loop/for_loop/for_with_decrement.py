print()

print("Increment and  Decrement Program number: 1")
lists= ['apple','sonylive','sammsung','metrola','intex','gorila','micromax','redmi','relemi','jiomeet']
dec=10
ind=0
for i in (lists):
    print(dec,i, "\t=" ,ind)
    dec-=1
    ind+=1
print(type(lists))

print()
print("Increment with index and  Decrement Program Number: 2")
dec=5
val=('Laptops','Comput','Radios','TVs','Mobiles')
for index, i in enumerate(val):
    print(index, "This is an electronice device name: ",i,"\t=",dec)
    dec-=1  
print(type(val))

print()
print("Increment and  Decrement Program Number: 3")
colors=("Red", "Green", "Blue", "Purple","Black","pinck","Yellow")
se_n=0
de_n=7
for i in (colors):
    
    print(se_n, "This is a color: ",i,"=", de_n )
    se_n+=1 
    de_n -=1
print(type(colors))

