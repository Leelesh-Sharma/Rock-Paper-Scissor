import random

print("\nRock Paper Scissor\n")
print("""Instructions-
    Paper beats Rock
    Scissor beats Paper
    Rock beats Scissor\n""")
print("Press 'r' for Rock, 'p' for paper, 's' for scissor\n")

def play(user):
    computer = random.choice(['r','p','s'])

    if user == computer:
        print("Tie.\n")

    elif user == 'r' < computer == 'p' or user == 'p' < computer == 's' or user == 's' < computer =='r' :
        print("Player wins.\n")

    else:
        print("Computer wins.\n")

round = int(input("How many rounds should the games consists: "))
print(f"{round} rounds\n")

for rounds in range(0,round):    
    user = input("Your move: ").lower()
    play(user)