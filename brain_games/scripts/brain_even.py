#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello
from brain_games.games.engine import check_answer


def even():
    hello()
    user_name = welcome_user('Answer "yes" if the number is even, otherwise answer "no".')
    count_answer = 0
    while count_answer < 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            correct_answer = 'yes'
        elif random_number % 2 != 0:
            correct_answer = 'no'
        print(f"Question: {random_number}")
        count_answer = check_answer(correct_answer, count_answer, user_name)
        if count_answer < 0:
            break
    if count_answer == 3:
        print(f"Congratulations, {user_name}!")


def main():
    even()


if __name__ == '__main__':
    main()
