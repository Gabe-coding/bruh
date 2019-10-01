# Gabriel Duran period 4
# Rock Paper Scissors
#VARIABLES
import random

pScore = 0
cScore = 0
ties = 0
computerChoices = ["r", "p", "s"]


print("Welcome to Rock Paper Scissors")
#prompt for player name
pName = input("what is your name?")

# Game loop

# final score
def printScore():
	# write message
	print("the score is:")
	# write score
	print(pName + ":" + str(pScore))

	print("Computer:" + str(cScore))

	print("Ties: " + str(ties))

#game loop
#fovever loop
while True:
	# print current score
	printScore()
    # prompt choice for  r (rock), p(paper), s(scissors), q(quit)
pChoice = input(" Enter r (rock), p (paper), s (scissors) or q (to quit:)")
  # q
 if pChoice == "q":
    	break
  # get random choice
 cChoice = random.choice(computerChoices)

    elif pChoice == "r":
    	print(pName + "picked Rock")

    if cChoice == "r":
    	print("computer picked rock")
    	print("this is a tie")
    	ties = ties + 1

    elif cChoice == "p":
    	print("computer picked paper")
    	print("paper covers rock")
    	cScore = cScore + 1

    else:
    	print("computer picked scissors")
    	print("rock breaks scissors")
    	pScore = pScore + 1

elif pChoice == "p":
	print(pName + "picked paper")

	if cChoice == "r":
    	print("computer picked rock")
    	print("paper covers rock")
    	pScore = pScore +1

     elif cChoice == "p":
    	print("computer picked paper")
    	print("this is a tie")
    	ties = ties + 1

    else:
    	print("computer picked scissors")
    	print("scissors cuts paper")
    	cScore = cScore + 1



elif pChoice == "s":
	print(pName + "picked scissors")

	if cChoice == "r":
    	print("computer picked rock")
    	print("rock breaks scissors")
    	cScore = cScore +1

    elif cChoice == "p":
    	print("computer picked paper")
    	print("scissors cuts paper")
    	pScore = pScore + 1

     else:
    	print("computer picked scissors")
    	print("this is a tie")
    	ties = ties + 1
