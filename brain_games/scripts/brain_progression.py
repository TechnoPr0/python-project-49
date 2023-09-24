#!/usr/bin/env python3
from random import randint
from brain_games.games.engine import check_answer, welcome_user, hello

def progression():
    hello()
    user_name = welcome_user("What number is missing in the progression?")
    count_answer = 0
    while count_answer < 3:
        rand_len = randint(5, 20)
        rand_index = randint(0, rand_len)
        rand_progressive = randint(2, 100)
        rand_start = randint(1, 100)
        list_numb = []

        for i in range(0, rand_len):
            if i == 0:
                list_numb.append(str(rand_start))
                next_numb = rand_start
            else:
                next_numb += rand_progressive
                list_numb.append(str(next_numb))
        
        correct_answer = list_numb[rand_index]
        list_numb[rand_index] = '..'
        list_print = ' '.join(list_numb)
        print(f"Questions: {list_print}")
        count_answer = check_answer(correct_answer, count_answer, user_name)
        if count_answer < 0:
            break
    if count_answer == 3:
        print(f"Congratulations, {user_name}!")


def main():
    progression()


if __name__ == '__main__':
    main()
