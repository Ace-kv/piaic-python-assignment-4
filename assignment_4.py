# Instructions: Implement Python programs to accomplish the following task

# Task : High Low

# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to 
# have you develop a game! The game is called High-Low and the way it's played goes as follows:

# 1. Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be 
# your opponent. You can see your number, but not the computer's!

# 2. You make a guess, saying your number is either higher than or lower than the computer's number

# 3. If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than 
# the computer's), you get a point!

# 4. These steps make up one round of the game. The game is over after all rounds have been played.

from random import randint
from typing import Literal

print("Welcome to the High-Low Game!\n_____________________________")

round_num: int = 1
score: int = 0

GUESS_VAL = Literal['higher', 'lower']

while round_num <= 5:

    my_num: int = randint(1, 100)
    comp_num: int = randint(1, 100)

    print(f'Round {round_num}\n')
    print(f'Your number is {my_num}')

    guess: GUESS_VAL = input("Do you think your number is 'higher' or 'lower' than the computer's?: ").lower()

    if guess not in ['higher', 'lower']:
        print("\nInvalid Input. Only type 'higher' or 'lower' to play the game\n")
        continue

    if (guess == 'higher' and my_num > comp_num) or (guess == 'lower' and my_num < comp_num):
        print(f"You were right! The computer's number was {comp_num}")

        score += 1

    else:
        print(f"That's incorrect. The computer's number was {comp_num}")

    round_num += 1
    print(f"\nYour score is now {score}\n")


rounds_played = round_num -1
print(f'Rounds Played: {rounds_played}, Total Score: {score}\n')

if score == 5:
    print('Amazing! You played perfectly!')

elif score >= (rounds_played // 2):
    print('Good job, you played really well!')
            
else:
    print('Better luck next time!')
