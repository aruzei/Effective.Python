#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER5
"""

import subprocess
from Profiles import profile_func

def _run_sleep(period):
    prop = subprocess.Popen(['sleep', str(period)])
    return prop

def _run_sleeps():
    procs = []
    for _ in range(100):
        procs.append(_run_sleep(0.01))
    for proc in procs:
        proc.communicate()

profile_func(_run_sleeps)
