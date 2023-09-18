#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import hello
from brain_games.games.brain_even import even


def main():
    hello()
    name = welcome_user()
    even(name)


if __name__ == '__main__':
    main()
