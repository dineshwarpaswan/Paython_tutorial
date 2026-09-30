print("\nExteding a list:- The extend() method used to adds all items from a list to another list.\n")

hrd = ["moble", "laptop", "tv"] # list 1
print("\nList 1: ",hrd) # print will be :list1

num= [20,6.0,"Desktop"] # list 2
print("\nList2: ",num) # print will be :list 2
 
num.extend(hrd) # list 1 will be add with list 2  
print("\nlist2 and list1 Marj in one list: ",num) # All data Marj in one list

hrd.extend(num) # list 2 will be add with list 1  
print("\nlist1 and list2 Marj in one list: ",hrd) # All data Marj in one list
