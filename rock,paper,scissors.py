import random
import sys 

choices_dict = {"r":"Rock", "p":"Paper", "s":"Scissors"} #dict defined for indexing by user and computer's choices during main game loop
beats = { 'r': 'p', 's': 'r', 'p': 's' }
choices = ["r","p","s"]


def play_again(): #determining whether entire program loop to be repeated or not


    while True:
        print("\n\nPlay another game?\nEnter y for Yes or n for No")
        print("\n--------------------------------")
        play_again_user_response = input("...")
        if (play_again_user_response == "y") or (play_again_user_response == "Y"):
            num_games_func()
            break

        if (play_again_user_response == "n") or (play_again_user_response == "N"):
            print("Are you sure you want to quit?\nEnter y to confirm")
            play_again_user_response_confirm = input("...")
            if (play_again_user_response_confirm == "y") or (play_again_user_response_confirm == "Y"):
                sys.exit() #closes command prompt
            continue

        print("Error: Invalid input\nPlease enter y or n")


def result(initial_rounds_num, final_scores):


	# determining winner
	print("\n--------------------------------")		
	if (final_scores[0] > final_scores[1]):
		print("Player wins best out of " + str(initial_rounds_num) + " with a score of " + str(final_scores[0]) + " against Computer's score of " + str(final_scores[1]) + "!")
	elif (final_scores[0] < final_scores[1]):
		print("Player loses best out of " + str(initial_rounds_num) + " with a score of " + str(final_scores[0]) + " against Computer's score of "+ str(final_scores[1]))
	else:
		print("Player and Computer have drawn at a score of " + str(final_scores[0]) + " for the best out of " + str(initial_rounds_num))
	play_again()


def game_run(rounds, scores):

	initial_rounds_num = rounds
	decrease_rounds = True

	while True:
		comp_choice = random.choice(choices)
		user_input = input("...")

		if (user_input not in choices):
			print("Enter a valid input")
			decrease_rounds = False
		else:
			decrease_rounds = True
			if (comp_choice == user_input):
				print(f"Both chose {choices_dict[comp_choice]}. Tie.")

			elif comp_choice == beats[user_input]:
			    print(f"Computer scores a point with {choices_dict[comp_choice]} which beats {choices_dict[user_input]}.")
			    scores[1] += 1
			else:
			    print(f"User scores a point with {choices_dict[user_input]} which beats {choices_dict[comp_choice]}.")
			    scores[0] += 1

		if (rounds == 1 and decrease_rounds): #check to see if currently on last round of game, if so give result with result function call 
			final_scores = scores
			result(initial_rounds_num, final_scores)
		if decrease_rounds:
			rounds -= 1
	

def start(rounds, scores):
	print("""\n-------------------\nBest of " + str(rounds) + ":\n-------------------\nEnter:\n\nr for Rock\np for Paper\ns for Scissors""") #giving rules
	game_run(rounds, scores)
	

def num_games_func():
	

	scores = [0,0]

	while True:
		num_games_input = input("...")
		if (num_games_input.isdecimal()): #checking valid input
			num_games_input = int(num_games_input)
			if (num_games_input == 3):
				rounds_remaining = num_games_input
				start(num_games_input, scores)
			elif (num_games_input == 5):
				rounds_remaining = num_games_input
				start(num_games_input, scores)
			elif (num_games_input == 10):
				rounds_remaining = num_games_input
				start(num_games_input, scores)
			else:
				print("Error: Invalid input\nEnter a valid input")
		else:
			print("Error: Invalid input\nEnter a valid input")


print("""Welcome to Rock, Paper, Scissors:\n\nPlease choose the number of rounds from the list below:\n\n-Three (Enter 3)\n-Five (Enter 5)\n-Ten (Enter 10)""") #introduction
num_games_func()
