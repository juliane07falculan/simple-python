import random

print('Number Guessing')
#function to play
def play():
    #enter lower and upper boundaries
    min_value = int(input('Enter a minimum value: '))
    max_value = int(input('Enter a maximum value: '))
    #generate random number
    random_number = random.randint(min_value, max_value)
    guess = int(input(f'Enter your guess between {min_value} and {max_value}: '))
    attempts = 0

    while guess != random_number:
        if guess < min_value or guess > max_value:
            guess = int(input(f'Invalid Option. Guess again between {min_value} and {max_value}: '))
            attempts -= 1  
        elif guess < random_number:
            min_value = guess
            guess = int(input(f'Too low. Guess again between {min_value + 1} and {max_value}: '))
        elif guess > random_number:
            max_value = guess
            guess = int(input(f'Too high. Guess again between {min_value} and {max_value - 1}: '))
        attempts += 1
    else:
        print(f'Congratulations! You have guessed the {random_number} correctly. \n{attempts} attempt/s')
        guess_again()

#function to guess again
def guess_again():

    response = input('Guess again? (y/n): ').lower()

    if response == 'y':
        play()
    else:
        print('Thank you, bye!')


play()

