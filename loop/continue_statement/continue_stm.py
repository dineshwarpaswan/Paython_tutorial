val = [1,2,3,4,5,6,7,8,9,10]
print("PROGRAM NUMBER :1, ak value ko skip karna hi continue kahlata hai is prog me 5 ko skip kiya gya hai")
for i in val:
    if i == 5:
        continue   # jaise hi 5 milega to 5 ko Skip kar dega, baki sabhi print kar dega;
    print(i) # 5 ko chhor kar baki sabhi print kar dega
print()


print("PROGRAM NUMBER :2, ak value ko skip karna hi continue kahlata hai is prog me 3 ko skip kiya gya hai")
for i in range(6):
    if i==3:
        continue # jaise hi 3 milega to 3 ko skip kar dega, baki sahi ko print kar dega,
    print(i)
print()


print("PROGRAM NUMBER :3,ak value ko skip karna hi continue kahlata hai is prog me 18 ko skip kiya gya hai")
n=20
i=12
while i <= n:
    i +=1
    if i == 18:
        continue   # jaise hi 18 milega milega to 3 ko skip kar dega, baki sahi ko print kar dega,
    print(i)   
    
    