print("\nWe can use pop() method for delet items  in end of list though : pop() method\n")
mix = [25.0,"Mobile",50.01,"Leptop","TV",200,True]
print("All items: ",mix)
print()
mix.pop() # type1 pop() method use for,delet will be last item in list
print("Delet will be True:",mix)
mix.pop() # pop() method use for,delet will be last item in list
print("Delet will be 200: ",mix)

mix.insert(1,"desktop") # 1 position per add ho jayega
mix.insert(2,"100") # 2 position per add ho jayega
mix.insert(5,"False") # 5 position per add ho jayega
print("New data insert with old: ",mix) # New data insert with old
print()

print("Access index 0: ",mix[0]) # access index 0 item
print("Access index 1: ",mix[1]) # access index 1 item
print("Access index 2: ",mix[2]) # access index 2 item
print("Access index 3: ", mix[3]) # access index 3 item
print("Access index 4: ",mix[4]) # access index 4 item
print("Access index 5: ",mix[5]) # access index 4 item
print("Access index 6: ",mix[6]) # access index 4 item
print("Access index 7: ",mix[7]) # access index 4 item

mix.remove("Mobile") # Type 2.remove() method use for deleting specifice item
print("Remove Mobile use for delet specificed item:",mix)

mix.remove("TV") # .remove() method use for deleting specifice item
print("Remove TV use for delet specificed item:",mix)

print("\nType 3 del method use for deleting speciefied index keyword\n") 
del mix[0] # del method use for deleting a speciefied index
del mix[2] # del method use for deleting a speciefied index
del mix[3] # del method use for deleting a speciefied index 
print("4 Items deleting in list:",mix)

