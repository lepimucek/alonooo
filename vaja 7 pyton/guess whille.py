#!/usr/bin/env python
# -*- coding: utf-8 -*-
secret = 22
ponovi = True

while ponovi:
    guess = int(raw_input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print "You guessed it - congratulations! It's number %s :)" %secret
        #ponovi = False
        break
    else:
        print "Sorry, your guess is not correct... Secret number is not {0} " .format(guess)
    nadaljuj = raw_input("Ponovi?(DA/NE)")
    if nadaljuj.lower() != "da":
        ponovi = False
        print "Ne bom ponovil"

