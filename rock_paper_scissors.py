import random
import time

def play():

    choices = ['r', 'p', 's']
    score = 0
    rounds = int(input('How many rounds?: '))
    for round in range(rounds):
        computer = random.choice(choices)
        user = input('r = rock, p = paper, s = scissors: ')
        
        if user not in choices:
            print('Invalid Option')
            break
        elif user == computer:
            print('It is a Tie')
        elif win(user, computer):
            print('You Win')
            score += 1
        else:
            print('You Lose')

    print(f'Score: {score}/{round + 1}')
    play_again()

def win(player, opponent):
    if player == 'r' and opponent == 's' or player == 'p' and opponent == 'r' or player == 's' and opponent == 'p':
        return True
    
def play_again():
    again = input('Play again? (y/n): ').lower()
    if again == 'y':
        play()
    else:
        print('Thank you, bye!')

play()


