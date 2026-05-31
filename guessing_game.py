import random

print("GUESSING GAME")

secret_number = random.randint(0, 9)
# print(secret_number)
guess_count = 0
limit = 3
while guess_count < limit:
    while True:
        try:
            player_guess = int(input("Enter your guess (0-9): "))
            if player_guess < 0 or player_guess > 9:
                print("Enter a valid number between 0 and 9")
            else:
                break
        except ValueError:
            print("Invalid input! Enter a whole number.")

    guess_count += 1

    if player_guess == secret_number:
        print(f"Yay!! You guessed right \nYou guessed {secret_number}")
        break
    elif player_guess != secret_number:
        print(f"You failed.\nYou guessed {player_guess}")
else:
    print("You are out of tries, you lose")
