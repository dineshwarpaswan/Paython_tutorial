print("Extract(nikalana) First name from List")


# Extract(nikalana) First name from List 
list_data = ["DINESHWAR PASWAN", "ROHIT SHARAM", "MUNA TIWARI", "BHARAT PANDIT", "RINKI RAJPUT"]

fname = []

print("\nlist data:", list_data,"\n")

for x in list_data:
	fname.append(x.split()[0])
print("Extract First name:",fname)

print("\n" + "=" *10)

list_data1 = ["SONY LAPTOP", "ROHIT SHARAM", "RED COLOR", "NOKIA MOBILE", "SAMSUNG TV"]

fname1 = []

print("\nlist data1:", list_data1,"\n")

for x1 in list_data1:
	fname1.append(x1.split()[0])
	print(fname1)
	
print("Extract First name:", fname1)
print("\n" + "=" *10)

#ran_data = list_data1.range(0, 4)
#print(ran_data)
fname2 = []
for x2 in list_data.range(3):
	
	print(x2.split())

