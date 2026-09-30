print()

print("Multiplication,Tabale of : 2")
lists= ['oriental','sonylive','sammsung','metrola','intex  ','gorila','micromax','redmi ','relemi','jiomeet']
mul=2
ind=1
for i in lists:
    print(ind,"x",mul,"\tBrand name: ",i,"\t=" ,mul*ind)
    mul*=1
    ind+=1
    
    if mul==20:
        break
print()

print("Multiplication,Tabale of : 4")
lists= ['oriental','sonylive','sammsung','metrola','intex ','gorila','micromax','redmi ','relemi','jiomeet']
mul=4
ind=1
m=4
for i in (lists):
    print(ind,"x",mul,i,"\t=" ,mul*ind)
    mul*=1
    m+=4
    ind+=1
    if mul==40:
        break
print()

print("Multiplication,Tabale of : 3 Helpe of Range function")
index=1
index1=3
for i in range(3,33,3):          #(start,stop,step)
    print(index,'x',index1,'=',i)
    index+=1   
print()

print("Multiplication,Tabale of : 20 Helpe of Range function")

a=1
a1=20
for i in range(20,300,20):          #(start,stop,step)
    print(a,'x',a1,'=',i)
    a+=1
    if i==200 or a==11:
        break
    
    

    
