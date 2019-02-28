import random
import string
items = ["clock", "backpack", "book", "shirt", "glasses", "computer", "apple", "calendar", "lightning", "projector"]
word = random.choice(items)

Guesses = 8
Guessed_letters = []
individual_letters = list(word)
unknown_answer = []
Guess = ""

for item in individual_letters:
    current_index = individual_letters.index(item)
    unknown_answer.insert(current_index, "_ ")

print("".join(unknown_answer))

mistakes = 8
while mistakes > 0:
    if unknown_answer == individual_letters:
        print("You've won")
        mistakes = 0
        continue

    Guess = input("Guess a letter:")

    if Guess in string.ascii_uppercase:
        Guess = Guess.lower()

    if Guess in individual_letters and Guess not in Guessed_letters:
        Guessed_letters.append(Guess)

        for i in range(len(individual_letters)):
            if individual_letters[i] == Guess:
                unknown_answer[i] = Guess
        print("".join(unknown_answer))

    elif Guess in Guessed_letters:
        print("You've Guessed this Letter Before")

    elif Guess not in Guessed_letters and Guess not in individual_letters:
        print("Guess again")
        mistakes -= 1
        Guessed_letters.append(Guess)
        print("".join(unknown_answer))


if mistakes == 0 and unknown_answer != individual_letters:
    print("You've Lost")

