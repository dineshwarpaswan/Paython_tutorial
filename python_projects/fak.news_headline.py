# 1. import random module
import random

# 2 .create subjucts
subjucts = [
	
	"Sharukh Khan",
	"MS Dhoni",
	"Virat Kohli",
	"Narender modi",
	"Chirag Paswan",
	"Lalu Yadav",
	"Karina kapur",
	"Rakhi Sawant",
	"Arjun Rampal Yadav",
	"Nana Patakar"

]

# 3. create actions
actions = [
	
	"Launch",
	"Danceing",
	"Eats",
	"Order a Cupe Tie",
	"Makup",
	"Celebration",
	"Smoking",
	"Mairred",
	"Quck run",
	"Excidental"
	
]
# 4. creat places_or_things
places_or_things = [
	
	" in Taj hotal",
	" in Ranchi airport",
	" at Karnat Place in Delhi",
	" inside parliament",
	" at Bitch in Gova",
	" insid Restorant",
	" in Mumbai Metro Tain",
	" at During IPL Match",
	" at India Gate",
	" in City Moll"
]

# start the headline generation lop
while True:
	subjuct = random.choice(subjucts)

	action = random.choice(actions)

	place_or_thing = random.choice(places_or_things)

	hadline = f"BREAKING NEWS: {subjuct} {action} {place_or_thing}"

	print("\n", hadline)

	user_input = input("\nDo you another Headline? (yes/no): ").strip().lower()

	if user_input == "no":

		break

# print goodbye message

print("Thank for Using the Fake News Headline Generator. Have a funy day")
