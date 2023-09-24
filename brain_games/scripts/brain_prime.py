#!/usr/bin/env python3
from random import randint
from brain_games.games.engine import check_answer, welcome_user, hello


def prime():
    hello()
    text = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    user_name = welcome_user(text)
    count_correct_answer = 0
    while count_correct_answer < 3:
        rand_num = randint(2, 100)
        correct_answer = "yes"
        for i in range(2, rand_num // 2 + 1):
            if rand_num % i == 0:
                correct_answer = 'no'
        print(f"Question: {rand_num}")
        count_correct_answer = check_answer(correct_answer,
                                            count_correct_answer,
                                            user_name)
        if count_correct_answer < 0:
            break
    if count_correct_answer == 3:
        print(f"Congratulations, {user_name}!")


def main():
    prime()


if __name__ == '__main__':
    main()
