import random


def play():
    print("****************************")
    print("WELCOME TO THE GUESSING GAME")
    print("****************************")

    secret_number = random.randrange(1, 101)
    maximum_of_attempts = 0
    score = 1000

    print("(1) Easy (2) Medium (3) Hard")
    difficulty_level = int(input("Choose a difficulty level: "))

    if (difficulty_level == 1):
        maximum_of_attempts = 20
    elif (difficulty_level == 2):
        maximum_of_attempts = 10
    else:
        maximum_of_attempts = 5

    for shout in range(1, maximum_of_attempts + 1):
        print("\n")
        print(
            f"# Attempt {shout} of {maximum_of_attempts}")  # equivalent print("Tentativa {} de {}".format(shout, maximum_of_attempts))

        user_attempt = int(input("Type a number between 1 and 100: "))

        if (user_attempt < 1 or user_attempt > 100):
            print("Invalid number, you must type a number between 1 and 100.")
            continue

        user_won = (user_attempt == secret_number)
        user_attempt_is_bigger = (user_attempt > secret_number)
        user_attempt_is_smaller = (user_attempt < secret_number)

        if (user_won):
            print(f"You WON! Your score: {score}.")
            break
        else:
            if (user_attempt_is_bigger):
                print("You missed! Your attempt was HIGHER than the secret number.")
            elif (user_attempt_is_smaller):
                print("You missed! Your attempt was LOWER than the secret number.")
            lost_points = abs(secret_number - user_attempt)
            score = score - lost_points

if(__name__ == "__main__"):#It enables to execute the file from the command line
    play()