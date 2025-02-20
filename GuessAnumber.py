import random
print("Guess a Number Game v1")
print("Guess the Secret Number")

while True:
    num_guesses = 0
    secret_number = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number between 1 and 10: "))
        num_guesses += 1
        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        elif guess == secret_number:
            break
    
    print(f"You guessed it! It was {secret_number}!")
    print(f"It took {num_guesses} guesses")
    play_again = input("would you like to play again? (Y/N) ")
    if play_again == 'N':
        break


