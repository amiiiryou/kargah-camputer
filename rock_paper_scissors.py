import random

user_score = 0
computer_score = 0

while True:

    print("\nRock Paper Scissors")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    user = int(input("Enter your choice: "))

    computer = random.randint(1, 3)

    if user == 1:
        user_choice = "Rock"
    elif user == 2:
        user_choice = "Paper"
    elif user == 3:
        user_choice = "Scissors"
    else:
        print("Invalid choice!")
        continue

    if computer == 1:
        computer_choice = "Rock"
    elif computer == 2:
        computer_choice = "Paper"
    else:
        computer_choice = "Scissors"

    print("Your choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user == computer:
        print("Draw!")

    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):

        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Score:", user_score, "-", computer_score)

    again = input("Do you want to play again? (yes/no): ")

    if again.lower() == "no":
        break

print("\nFinal Score:", user_score, "-", computer_score)

if user_score > computer_score:
    print("You win the game!")
elif computer_score > user_score:
    print("Computer wins the game!")
else:
    print("The game is a draw!")
