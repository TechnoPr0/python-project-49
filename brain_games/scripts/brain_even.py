#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello


def main():
    hello()
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_correct_answer = 0
    while count_correct_answer < 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        elif random_number % 2 != 0:
            correct_answer = 'no'
        print(f"Question: {random_number}")
        user_answer = input('Your answer: ')
        if correct_answer == user_answer.lower():
            print("Correct!")
            count_correct_answer += 1
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break
    if count_correct_answer == 3:
        print(f"Congratulations, {name}!")
