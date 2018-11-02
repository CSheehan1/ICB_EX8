#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 01:45:31 2018

@author: ColinSheehan
"""

def numbergame():
    nums=range(1,100)
    target=numpy.random.choice(nums)
    print("I'm thinking of a number between 1 and 100...")
    thing=raw_input("Guess my number: ")
    if thing==target:
        print("well done, persistent master of we machines.")
    while target > thing:
        print("Nahhh too low.")
        thing=raw_input("Guess my number: ")
    while target < thing:
        print("Nahhh too high.")
        thing=raw_input("Guess my number: ")
