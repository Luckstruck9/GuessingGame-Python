# Guessing Game
# By Lucky

import random
# Imports the object random (NECESSARY)

num = random.randint(1 , 100)								# Assigns a variable a random value
user = 0													# Sets user to equal 0
while (user!=num):											# While loop
	user = eval(input("Please guess a number 1-100: "))		# Gets the user guess

	if (user==num):											# Checks if the user guessed correctly
		print("You guessed it correctly!")
		break												# Exits the 'While' loop
	elif (user>num):										# If the guess was too large...
		print("You guessed too high!")
	elif (user<num):										# If the guess was too small...
		print("You guessed too low!")