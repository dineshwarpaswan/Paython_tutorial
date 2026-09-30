print("\nRange Indexing: by using a colon (:) we can access a range of items at once. A Tuple is created round brackets() and indexing is square brackets[].\n")

num = (20,30,50,60,70,80,90)
print(num)
x=(num[1:2]) # 1st position beak kado and 2nd wale ko print kardo : 30
print("1st position beak kado and 2nd wale ko print kardo:30",x)

x1=(num[2:4]) # 2nd position beak tak kado and 3rd,4t ko print kardo: 50,60
print("2nd position beak tak kado and 3rd,4t ko print kardo:50,60",x1)

x2=(num[3:5]) # 3rd position tak beak kado and 4t,5t ko print kardo: 60,70
print("3rd position tak beak kado and 4t,5t ko print kardo:60,70",x2)

x3=(num[4:6]) # 4t position tak beak kado and 5t,six ko print kardo: 70,80
print("4t position tak beak kado and 5t,six ko print kardo:70,80",x3)

Stacnery= ("Pen","Pencil","Copy","Book","Reber")
print(Stacnery)

Stacnery1=(Stacnery[1:2])
print("\nF1st position beak kado and 2nd wale ko print kardo: Pencil",Stacnery1) #F1st position beak kado and 2nd wale ko print kardo : Pencil

Stacnery2=(Stacnery[2:3])
print("2nd position tak brea kado and 3rd wale ko print kardo: Copy",Stacnery2) # 2nd position beak tak kado and 3rd wale ko print kard: Copy

Stacnery3=(Stacnery[2:4])
print("2nd position beak tak kado and 3rd ,four ko print kard: Copy,Book",Stacnery3) # 2nd position beak tak kado and 3rd ,four ko print kard: Copy,Book

Stacnery4=(Stacnery[3:5])
print("3rd position tak beak kado and 4t,5t ko print kardo: Book,Reber:",Stacnery4) # 3rd position tak beak kado and 4t,5t ko print kardo: Book,Reber

mix = ("Dog",50,"Fruit",30.01,True)
print("\n",mix)
mix1=(mix[2:])
print("\nIndex2 to last index Fruit,30.01,True: ",mix1) # print index2 to last index: Fruit,30.01,True
mix2=(mix[:2])
print("Index2 left Dog,50: ",mix2) # print index2 left:"Dog",50,
mix3=(mix[3:])
print("Index3 to last index 30.01,True: ",mix3) # print index3 to last index: 30.01,True
mix4=(mix[:3])
print("Index3 left Dog,50,Fruit: ",mix4) # print index3 left: Dog",50,"Fruit
mix5=(mix[4:])
print("nIndex4 to last index True: ",mix5) # print index4 to last index: True


