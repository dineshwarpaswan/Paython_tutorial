print("\nUnion: The Combine elements from two sets, Removing duplicates.\n")

mix = {"vegeteble", "fruit", "liqiud", "greps", "apple"}

fruit = {"banana","mango","greps","apple"}

union_set = mix.union(fruit)

print("This is Union set and Combine the set:",union_set) # combine set


# Union() method:- Combine element from two sets, removing duplicates.")

x = {40,50,60,70}
y = {40,60,70,80}

union_set = x.union(y)
print("\nThis is Union set and Combine the set:",union_set) # combine set {}

# Allternative Syntax:
#       Union_set = set_a | set_b

a = {2,3,4,5,6}
b = {5,6,7,8}
 
my_unionSet = a | b   # type 2 but result same 
print("\nType2 This is Allternative and Combine the set:", my_unionSet) 

x = {40,50,60,70}
y = {40,60,70,80}
union_set = x | y   # type 2 but result same

print("\nType2 This is Allternative set and Combine the set:",union_set) # combine set {}
