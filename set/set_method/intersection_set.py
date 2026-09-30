print("\nIntersection: Includes only elements present in both set. Both two set in common result\n")

mix = {"vegeteble", "fruit", "liqiud", "greps", "apple"}

fruit = {"banana","mango","greps","apple","vegeteble", "fruit",}

intersection_set = mix.intersection(fruit)  #  both two set in common result 

print("Intersection() method use both two set in common result:",intersection_set)  #output {'greps', 'vegeteble', 'fruit', 'apple'}


#both two set in common result 

x = {40,50,60,70}
y = {40,60,70,80}
my_set = x.intersection(y) #  both two set in common result 

print("Intersection() method, use Both two set in common result",my_set)  # output: {40, 60, 70}  
