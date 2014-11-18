#!/usr/bin/env python

import string
import random
import time
import datetime
import operator


nato_dict = {}
scores = {}


def main():
    ''' A simple flaschard game to help learn nato phonetic alphabet.
    When run, a letter is displayed. If you know it's nato word, hit enter. If
    you don't know it, hit any key and enter. The answer is then displayed.
    When you've completed the deck, a score is displayed - along with any
    letters which need work.

    '''
    read_alphabet()
    flash_cards()


def read_alphabet():
    f = open('nato-alphabet.txt')
    lines = f.read().splitlines()
    global nato_dict
    nato_dict = dict(line.split('\t') for line in lines)


def flash_cards():
    deck = []
    deck = list(string.ascii_uppercase)
    random.shuffle(deck)
    game_start_time = datetime.datetime.now()

    # start game
    while deck:
        clear_terminal()
        card = deck.pop()
        print card
        start_time = datetime.datetime.now()
        result = raw_input()
        if result:
            # if user entered input, that means they didn't know the card
            # so show them the word
            clear_terminal()
            print nato_dict[card]
            time.sleep(0.5)
        else:
            # calculate time and append to scores
            scores[card] = datetime.datetime.now() - start_time
        clear_terminal()

    # game finished, calculate results
    game_time = datetime.datetime.now() - game_start_time
    bad_scores = {k: v for k, v in scores.iteritems() if v > datetime.timedelta(seconds=1)}
    good_scores = {k: v for k, v in scores.iteritems() if v < datetime.timedelta(seconds=0.75)}
    missed_letters = [l for l in list(string.ascii_uppercase) if l not in scores]

    # output results
    print 'Letters which need work:'
    for letter in missed_letters:
        print '  %s: Missed' % letter
    for score in bad_scores:
        print '  %s: %s sec' % (score, round(scores[score].total_seconds(), 2))
    print
    print 'Finished in %s seconds' % round(game_time.total_seconds(), 2)


def clear_terminal():
    print chr(27) + "[2J"


if __name__ == '__main__':
    main()
