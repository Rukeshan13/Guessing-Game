import  random
attempts = 5

def rules_list():
    print("Welcome to Guessing Game!\n")
    print("Computer selected a number btw 1 to 150.")
    print("You have 5 attempts to guess.\n")

def play_game(number, attempt=1):
    if attempt > attempts:
        print("Game Over.")
        print("The correct number was:", number)
        return

    guess = input(f"Attempt {attempt}/5 - Enter your guess:")

    try :
        guess = int(guess)
    except ValueError:
        print("Plz Enter a valid Number.\n")
        return play_game(number, attempt)

    if guess < 1 or guess > 150:
        print("Plz Enter a Number between 1 to 150.\n")
        return play_game(number, attempt)

    check_guess = lambda x, y : "correct" if x == y else(
        "low" if x < y else "high"
    )
    result = check_guess(guess, number)

    if result == "correct":
        print("\nCongrats! You Guessed it right!")
        print("You guesed it in", attempt, "attempt(s).")
        return
    if result == "low":
        print("Too Low.. Try a higer number.\n")
    else:
        print("Too High.. Try a smaller Number.\n")

    play_game(number, attempt + 1)

rules_list()
random_number = random.randint(1, 150)
play_game(random_number)