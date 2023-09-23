import prompt


def welcome_user(hint):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(hint)
    return name


def hello():
    print("Welcome to the Brain Games!")


def check_answer(correct_answer, count_correct_answer, user_name):
    user_answer = input('Your answer: ').lower()
    if str(correct_answer) == user_answer:
        print("Correct!")
        count_correct_answer += 1
    else:
        print(
            f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {user_name}!")
        count_correct_answer = -1
    return count_correct_answer
