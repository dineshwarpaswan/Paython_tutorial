print("\nitrerator with range helps the for loop !\n")

fruits = ("APPLE","MANGO","BANANA","ORANGE","GREPS") # tuple
iterator = iter(fruits)
for ite in iterator:
	print("Item fruits: " ,ite)

x = (len(fruits)) 
print("\nTotal lenth:",x)  # totale lenth: 5

for y in range(x):
	print("\n",y) # lenth of positin (start =0, stop =(5-1))
