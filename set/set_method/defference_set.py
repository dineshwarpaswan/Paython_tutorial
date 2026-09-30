print("\nDifference:Elements present in the first set but not in the second. Difference of Two Sets: TO get the difference between two sets, use the subtraction operator(-).")

# Difference:Elements present in the first set but not in the second.


x = {40, 50, 60, 70}
y = {60, 70, 80, 90}

print("\nX-Y:", x - y) # dono set ke common ko chore ke lekin jo bach gya hai jis set gataya gya hai:{40, 50}
print("\ny - x:", y - x) # Dono set ke common ko chore ke lekin jo bach gya hai jis set gataya gya hai: {80, 90}

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("\na-b:", a - b) # Dono set ke common ko chore ke lekin jo bach gya hai jis set gataya gya hai:{1, 2}
print("\nb- a:", b - a) # Dono set ke common ko chore ke lekin jo bach gya hai jis set gataya gya hai:{5, 6}


# Allternative Syntax: set_a - set_b

my_differece = a - b
print(my_differece) # ouput: {1,2}


my_differece = b - a
print(my_differece) # ouput: {5,6}
