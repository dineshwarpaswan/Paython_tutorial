print("\nCombine Two Set: TO Combine two sets, We can use the update() method and union()Method.\n")

mix = {"vegeteble","fruit","liqiud",}

fruit = {"banana","mango","greps","apple"}

mix.update(fruit)

print("Type1 is combine  Set:",mix) # combine set


x = {40,50,60,70}
y = {40,60,70,80}
x.update(y)
print("\nType2 combine  Set:",x) # combine set {}

print("1. Union() method:- Combine element from two sets, removing duplicates.")

my_set= x.union(y)    
print(my_set)  # output: 40,50,60,70,80 

print("Intersection() method:- Combine element from two sets, removing duplicates.")
x = {40,50,60,70}
y = {40,60,70,80}
my_set = x.intersection(y)
print(my_set)  # output: {40,60,70}
