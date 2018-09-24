import random
class RockPaperScissors():
	def twoplayergame(self):
		newgame = "yes"
		while newgame != "no":

			player1 = input("Player 1 please choose: rock,paper,scissors? Pick one!")
			player2 = input("Player 2 please choose: rock,paper,scissors? Pick one!")
			if player1 == "rock" and player2 == "scissors":
				print("player 1 wins!!!")
				newgame = input("Play again?")
			elif player1 == "scissors" and player2 == "paper":
				print("player 1 wins!!!")
				newgame = input("Play again?")
			elif player1 == "paper" and player2 == "rock":
				print("player 1 wins!!!")
				newgame = input("Play again?")
			elif player1 == "scissors" and player2 == "rock":
				print("player 2 wins!!!")
				newgame = input("Play again?")
			elif player1 == "paper" and player2 == "scissors":
				print("player 2 wins!!!")
				newgame = input("Play again?")
			elif player1 == "rock" and player2 == "paper":
				print("player 2 wins!!!")
				newgame = input("Play again?")
	def oneplayergame(self):

		newgame = "yes"
		gamelist = ["rock","paper","scissors"]
		computerpick = random.choice(gamelist)
		while newgame != "no":
			player1 = input("rock,paper,scissors: ")
			if computerpick == "rock" and player1 == "scissors":
				print("The computer picked " + str(computerpick) + " You lost bruh!")
				newgame = input("Play again?")
			elif computerpick == "Scissors" and player1 == "paper":
				print("The computer picked " + str(computerpick) +  " You lost bruh!")
				newgame = input("Play again?")
			elif computerpick == "paper" and player1 == "rock":
				print("The computer picked " + str(computerpick) +  " You lost bruh!")
				newgame = input("Play again?")
			elif computerpick == "rock" and player1 == "rock":
				print("The computer picked " + str(computerpick) + " You both chose the same thing. Try again.")
				newgame = input("Play again?")
			elif computerpick == "scissors" and player1 == "scissors":
				print("The computer picked " + str(computerpick) + " You both chose the same thing. Try again.")
				newgame = input("Play again?")
			elif computerpick == "paper" and player1 == "paper":
				print("The computer picked " + str(computerpick) + " You both chose the same thing. Try again.")
				newgame = input("Play again?")
			else:
				print(computerpick)
				print("You won")
				newgame = input("Play again?")
run = RexiockPaperScissors()
run.oneplayergame()






















