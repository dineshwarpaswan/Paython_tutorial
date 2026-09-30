print("\nSymmentric difference :-Elements in either set, but not in both. Dono sets ke woh sare elements jo common nahi hai\n")

# Characteristics of Set:
# . Unordered:- element have no define order. you can not access element by index.
# . Unique Elements:- no duplicate allow items. Each element must be distinct.
# . Mutable:- You can add or Remove element after creation.
# . Immutable Element:- Individual element inside a set cannot be modiffied


#  Symmetric difference :- Dono sets ke woh sare elements jo common nahi hai

# Method 1:  Using  Method

set1 = {1,2,3,4}
set2 = {3,4,5,6}

a = set2.symmetric_difference(set1)
print("\nTHis is a Symmetric difference(Dono sets ke woh sare elements jo common nahi hai): ",a)

# Method 2 : Using ^ oprator
no_common = set1 ^ set2
print(f"\nBoth set no common, That will be print: {no_common}") # Both set no common will be print: {1,2,5,6}
