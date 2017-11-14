#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:52:21 2017

@author: tcs-user
"""
from Hangman import loss


def test_loss():
    assert loss(5, 7) == 'You won!'
    assert loss(7, 7) == 'You lost!'
    assert loss(9, 7) == 'You lost!'
