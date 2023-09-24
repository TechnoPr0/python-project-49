#!/usr/bin/env python3
from random import randint
from brain_games.games.engine import check_answer, welcome_user, hello


def check_numb(num_1, num_2):
    if num_1 < num_2:
        smaller_number = num_1
        larger_number = num_2
    else:
        smaller_number = num_2
        larger_number = num_1
    return smaller_number, larger_number


def gcd():
    hello()
    text = "Find the greatest common divisor of given numbers."
    user_name = welcome_user(text)
    count_answer = 0
    while count_answer < 3:
        rand_num_1 = randint(1, 100)
        rand_num_2 = randint(1, 100)
        print(f"Question: {rand_num_1} {rand_num_2}")
        smaller_number, larger_number = check_numb(rand_num_1, rand_num_2)
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
