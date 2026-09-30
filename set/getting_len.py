print("\cGETTING THE LENGTH OF A SET: To get the length or number of items,used len() method.\n")

# Characteristics of Set:
# . Unordered:- element have no define order. you can not access element by index.
# . Unique Elements:- no duplicate allow items. Each element must be distinct.
# . Mutable:- You can add or Remove element after creation.
# . Immutable Element:- Individual element inside a set cannot be modiffied


mix = {"vegeteble","fruit","liqiud","gegeted"}
print(f"class type:{type(mix)}")

print("Total lenth of set: ",len(mix))

print("\nThis is a set: ",mix)


for x in mix: print(x)

#print("To get the length :",lenth(mix)) # not suport while loop
