#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:52:21 2017

@author: tcs-user
"""
from Hangman import gener_random


def test_gener_random():
    c = gener_random()
    assert c >= 0 and c <= 4
