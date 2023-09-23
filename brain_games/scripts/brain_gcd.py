#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello
from brain_games.games.engine import check_answer

def gcd():
    hello()
    user_name = welcome_user("Find the greatest common divisor of given numbers.")
    count_answer = 0
    while count_answer < 3:
        rand_num_1 = randint(1, 100)
        rand_num_2 = randint(1, 100)
        print(f"Question: {rand_num_1} {rand_num_2}")
        if rand_num_1 < rand_num_2:
            smaller_number = rand_num_1
            larger_number = rand_num_2
        else:
            smaller_number = rand_num_2
            larger_number = rand_num_1
        for i in range(smaller_number, 0, -1):
            if smaller_number % i == 0 and larger_number % i == 0:
                correct_answer = i
                break
        count_answer = check_answer(correct_answer, count_answer, user_name)
        if count_answer < 0:
            break
    if count_answer == 3:
        print(f"Congratulations, {user_name}!")

def main():
    gcd()


if __name__ == '__main__':
    main()
