#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:52:21 2017

@author: tcs-user
"""
import mock
from Hangman import get_input


def test_get_input():
    with mock.patch('builtins.input', side_effect='jjjj'):
        assert get_input() == 'j'
