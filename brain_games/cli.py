import prompt


def welcome_user(hint):
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(hint)
    return name
