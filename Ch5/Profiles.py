#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER5
"""

from cProfile import Profile
from pstats import Stats

def profile_func(function):
    """
    Profile execution of a function
    """
    profile = Profile()
    profile.runcall(function)

    stat = Stats(profile)
    stat.strip_dirs()
    stat.sort_stats('cumulative')
    stat.print_stats()
