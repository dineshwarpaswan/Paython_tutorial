
# Dictionary comprehension :direct key-value pairs bana sakte hain.

lists = {x: x*x for x in range(4)}

print(lists)# output : {0:0,1:1,2:4,3:9}


lists1 = {x: x*x for x in range(1,6)}

print(lists1) # output : {1:1, 2:4, 3:9, 4:16, 5:25}
