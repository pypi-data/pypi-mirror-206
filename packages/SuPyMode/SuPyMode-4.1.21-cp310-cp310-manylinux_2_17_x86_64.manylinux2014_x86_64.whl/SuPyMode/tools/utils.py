#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_valid_input(user_input, valid_inputs: list):
    if user_input not in valid_inputs:
        raise ValueError(f"user_input: {user_input} argument not valid. Valid choices are: {valid_inputs}")


# -
