import random

#Password Strength Cheacker

import random

easy_words = ["mobile","train","laptop","tiger","india"]

medium_words = ["python", "redio", "computer", "monky", "bottale"]

hard_words = ["elephant","umbrella","banana","mountain","dimond"]

print("Wellcome to the password guessing game")
print("Choice a difficulty level: easy, medium, hard")

level = input("Enter difficulty: ").lower()

if level == "easy":
	secret =random.choice(easy_words)  # use random.choice()

elif level == "medium":
	secret = random.choice(medium_words)

elif level == "hard":
	secret = random.choice(hard_words)
else:
	print("invalid choice. Default to easy level word")

	secret = random.choice(easy_words)

attempts = 0
print("Guess the secret password")

while True:
	guess = input("Enter your guess: ").lower()
	attempts += 1 

	if guess == secret:
		print(f"Congratulation! You guessed it in {attempts} attempts.")
		break
	hint = ""

	for i in range(len(secret)):
		if i < len(guess) and guess[i] ==secret[i]:
			hint += guess[i]

		else:
			hint += "_"

	print("hint:" , hint)
print("Game Over!")
    

        

   






















