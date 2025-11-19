# Determine the user's life stage based on their age
def generate_profile(age):
	if current_age >= 20: 
		return "Adult"
	elif current_age >= 13: 
		return "Teenager"
	else: 
		return "Child"

current_year = 2025

# Input user info
user_name = input("Enter your full name: ") 					# current user's name
birth_year_str = input("Enter your birth year: ")			# string of the user's birth year
birth_year = int(birth_year_str)											# convert birth_year_str to integer
current_age = current_year - birth_year								# current user's age

hobbies = []																					# list of user's hobbies
# Loop to input hobbies until the user types 'stop'
while True:
	hobbie = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
	if hobbie.lower() == "stop": break
	hobbies.append(hobbie)

# Create the user profile dictionary with keys: name, age, stage, hobbies
life_stage = generate_profile(current_age)
user_profile = {"name" : user_name,
								"age" : current_age,
								"stage" : life_stage,
								"hobbies" : hobbies
								}

#Display information about user
print("---")
print("Profile Summary:")
print(f"Name: {user_profile["name"]}")
print(f"Age: {user_profile["age"]}")
print(f"Life Stage: {user_profile["stage"]}")
# Print the list of hobbies if they exist
if len(user_profile["hobbies"]) == 0: 
	print("You didn't mention any hobbies.") 
else:
	print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
	for hobbie in user_profile["hobbies"]:
		print(f"- {hobbie}")

print("---")