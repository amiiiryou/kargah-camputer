import random

words = ["apple", "book", "computer", "school", "python"]

word = random.choice(words)

guessed = []
wrong = 0

print("Hangman")
print("Guess the word!")

while wrong < 6:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", display)

    if "_" not in display:
        print("You win!")
        break

    guess = input("Enter a letter: ")

    if guess in guessed:
        print("You already guessed this letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong += 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong)

if wrong == 6:
    print("\nYou lose!")
    print("The word was:", word)
