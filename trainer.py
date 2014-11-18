#!/usr/bin/env python

import string
import random
import time
import datetime
import operator


nato_dict = {}

scores = {}

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
    deck = list(string.ascii_uppercase)
    random.shuffle(deck)
    prev_card = None
    print 'Game Start'
    game_start_time = datetime.datetime.now()
    while True:
        clear_terminal()
        card = deck.pop()
        print card
        start_time = datetime.datetime.now()
        result = raw_input()
        if result:
            clear_terminal()
            print nato_dict[card]
            time.sleep(0.5)
        else:
            scores[card] = datetime.datetime.now() - start_time
        clear_terminal()
        prev_card = card
        if not deck:
            # break here, show score
            break
    game_time = datetime.datetime.now() - game_start_time
    # get scores higher than one second
    bad_scores = {k: v for k, v in scores.iteritems() if v > datetime.timedelta(seconds=1)}
    # get scores quicker than quarter second
    good_scores = {k: v for k, v in scores.iteritems() if v < datetime.timedelta(seconds=0.75)}
    missed_letters = [l for l in list(string.ascii_uppercase) if l not in scores]
    print 'Your best letters:'
    for score in good_scores:
        print '%s: %s second(s)' % (score, scores[score])
    print
    print 'Letters which need work:'
    for letter in missed_letters:
        print '%s: Missed' % letter
    for score in bad_scores:
        print '%s: %s second(s)' % (score, scores[score])
    print
    print 'Deck finished in %s seconds' % timedelta_to_seconds(game_time)
    


def timedelta_to_seconds(td):
    ''' Turn timedelta into 0.000 string.

    '''
    return '%s.%s' % (td.seconds, td.microseconds)



def clear_terminal():
    print chr(27) + "[2J"


if __name__ == '__main__':
    main()
