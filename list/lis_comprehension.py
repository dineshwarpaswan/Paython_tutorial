# Normal for Loop


lists = []
for x in range(10):
	if x % 2 == 0:
		lists.append(x)
print(lists) # output: [0, 2, 4, 6, 8]

lists1 = []
lists1 = [x for x in range(10) if x % 2 == 0]

print(lists1) # output: [0, 2, 4, 6, 8]

numbers = []
for x in range(5):
	numbers.append(x*2) #
print(numbers) # output: [0, 2, 4, 6, 8]

#list Comprehension	
empty = []
empty = [x * 2 for x in range(5)]
print(empty)
