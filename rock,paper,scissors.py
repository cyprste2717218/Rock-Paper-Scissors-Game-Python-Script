
import random

choices_dict = {"r":"Rock", "p":"Paper", "s":"Scissors"}
choices = ["r","p","s"]
def play_again():
	print("\n\nPlay another game?\nEnter y for Yes or n for No")
	print("\n--------------------------------")
	play_again_user_response = input("...")
	if (play_again_user_response == "y") or (play_again_user_response == "Y"):
		num_games_func()

	elif (play_again_user_response == "n") or (play_again_user_response == "N"):
		print("Are you sure you want to quit?\nEnter y to confirm")
		play_again_user_response_confirm = input("...")
		if (play_again_user_response_confirm == "y") or (play_again_user_response_confirm == "Y"):
			exit()
		else:
			play_again()

	else:
		print("Please enter y or n")
		play_again()


def result():
	# determining winner
	print("\n--------------------------------")		
	if (scores[0] > scores[1]):
		print("Player wins best out of " + str(num_games_input) + " with a score of " + str(scores[0]) + " against Computer's score of " + str(scores[1]) + "!")
	elif (scores[0] < scores[1]):
		print("Player loses best out of " + str(num_games_input) + " with a score of " + str(scores[0]) + " against Computer's score of "+ str(scores[1]))
	else:
		print("Player and Computer have drawn at a score of " + str(scores[0]) + " for the best out of " + str(num_games_input))
	play_again()

def game_run(rounds):
	if rounds > 0:
		comp_choice = random.choice(choices)
		user_input = input("...")
		if (user_input == "r"):

			if (comp_choice == "r"):
				print("Both chose " + choices_dict[comp_choice])
			
			elif (comp_choice == "p"):
				print("Computer chose " + choices_dict[comp_choice] + ", computer wins a point")
				scores[1] += 1
			
			elif (comp_choice == "s"):
				print("You scored a point! Computer chose " + choices_dict[comp_choice])
				scores[0] += 1
			

		elif (user_input == "p"):
			if (comp_choice == "r"):
				print("You scored a point! Computer chose " + choices_dict[comp_choice])
				scores[0] += 1
			
			elif (comp_choice == "p"):
				print("Both chose " + choices_dict[comp_choice])
			
			elif (comp_choice == "s"):
				print("Computer chose " + choices_dict[comp_choice] + ", computer wins a point")
				scores[1] += 1
				

		elif (user_input == "s"):
			if (comp_choice == "r"):
				print("Computer chose " + choices_dict[comp_choice] + ", computer wins a point")
				scores[1] += 1
				
			elif (comp_choice == "p"):
				print("You scored a point! Computer chose " + choices_dict[comp_choice])
				scores[0] += 1
				
			elif (comp_choice == "s"):
				print("Both chose " + choices_dict[comp_choice])
		else:
			print("Enter a valid input")
			game_run(rounds)
		
		if rounds == 1:
			result()
		rounds -= 1
		game_run(rounds)
	

def start(rounds):
	inp = rounds
	print("\n-------------------\nBest of " + str(rounds) + ":\n-------------------\nEnter:\n\nr for Rock\np for Paper\ns for Scissors")
	game_run(inp)
	
def num_games_func():
	global scores
	scores = [0,0]
	global num_games_input
	num_games_input = input("...")
	if (num_games_input.isdecimal()):
		num_games_input = int(num_games_input)
		if (num_games_input == 3):
			rounds_remaining = num_games_input
			start(num_games_input)
		elif (num_games_input == 5):
			rounds_remaining = num_games_input
			start(num_games_input)
		elif (num_games_input == 10):
			rounds_remaining = num_games_input
			start(num_games_input)
		else:
			print("Enter a valid input")
			num_games_func()
	else:
		print("Enter a valid input")
		num_games_func()

print("Welcome to Rock, Paper, Scissors:\n\nPlease choose the number of rounds from the list below:\n\n-Three (Enter 3)\n-Five (Enter 5)\n-Ten (Enter 10)")
num_games_func()




