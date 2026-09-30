print("\nCHECKING IF ITEM EXITES: TO check if an item exists in a set, used the in operator.\n")
mix = {"vegeteble","fruit","liqiud","gegeted"}

print("This a Set:",mix)
print("fruit" in mix) # Type1, if DATA is match, print will be: True
print("human" in mix) # Type1, if data is No match, print will be:False.

if "liqiud" in mix: # Type2, if DATA is match, print will be: Yes 
    print("\nType2 DATA is match")


if "dreass" in mix: # Type3, if DATA is NO match, print will be: No 
    print("DATA is Match")
else:
	print("\nType3 NO DATA is Match") # if DATA is NO match, print will be: No