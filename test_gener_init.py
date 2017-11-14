#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:52:21 2017

@author: tcs-user
"""
from Hangman import gener_init, DICT


def test_gener_init():
    for i in range(4):
        letter, length, guess, attempts = gener_init(i)
        assert letter == DICT[i]
        assert length == len(letter)
        assert guess == '*' * length
        assert attempts == 0
