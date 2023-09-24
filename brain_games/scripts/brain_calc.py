#!/usr/bin/env python3
from random import randint, choice
from brain_games.games.engine import check_answer, welcome_user, hello


def brain_calc():
    hello()
    user_name = welcome_user("What is the result of the expression?")
    signs = ['+', '-', '*']
    count_answer = 0
    while count_answer < 3:
        first_num, second_num = randint(1, 100), randint(1, 100)
        rand_sign = choice(signs)
        print(f"Question: {first_num} {rand_sign} {second_num}")
        match rand_sign:
            case '+':
                correct_answer = first_num + second_num
            case '-':
                correct_answer = first_num - second_num
            case '*':
                correct_answer = first_num * second_num
        count_answer = check_answer(correct_answer, count_answer, user_name)
        if count_answer < 0:
            break
    if count_answer == 3:
        print(f"Congratulations, {user_name}!")


def main():
    brain_calc()


if __name__ == '__main__':
    main()
