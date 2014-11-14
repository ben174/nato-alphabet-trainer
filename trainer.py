#!/usr/bin/env python

import string
import random
import time

nato_dict = {}


def main():
    read_alphabet()
    flash_cards()


def read_alphabet():
    f = open('nato-alphabet.txt')
    lines = f.read().splitlines()
    global nato_dict
    nato_dict = dict(line.split('\t') for line in lines)


def flash_cards():
    deck = []
    while True:
        clear_terminal()
        if not deck:
            print 'NEW DECK'
            deck = list(string.ascii_uppercase)
            random.shuffle(deck)
        card = deck.pop()
        print card
        raw_input()
        clear_terminal()
        print nato_dict[card]
        time.sleep(0.5)


def clear_terminal():
    print chr(27) + "[2J"


if __name__ == '__main__':
    main()
