#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Functions for scripts in chapter2.
"""

def divide(dividend, divisor):
    """
    Divide dividend by divisor. If ZeroDivisionError occurs, raise ValueError.
    """
    try:
        return  dividend / divisor
    except ZeroDivisionError as ex:
        raise ValueError("Can't inout divisor as zero.") from ex


def show_quotient(dividend, divisor):
    """
    Show quotient. If ValueError occurs, print it.
    """
    try:
        print(divide(dividend, divisor))
    except ValueError as ex:
        print(ex)