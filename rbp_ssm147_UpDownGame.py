#Autor ssm147 Varna July 2014

maximum = 1000
minimum = 1
counter = 0 

print("Think about a number from 1 to 1000! I'll guess!")

while True:
  # binary search
	guessed_number = (maximum + minimum)/2
	counter = (counter + 1)
	print("This is my number: " +str(guessed_number)+ ". Have I guessed right?")
	
  # cheater detection
	if minimum + 1 == maximum: 
		print("You shameless cheater!")
		break
		
	user_input = input("1 for up, 2 for down, 3 for yes: ")

	if user_input == 1:
		minimum = guessed_number
	
	if user_input == 2:
		maximum = guessed_number
		
	if user_input == 3:
		print("Yes! I'm a good guesser.")
		break
	
	if counter > 10:
		print("Sorry I'm tired. Maybe next time.")
		break	