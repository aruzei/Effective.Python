#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""platform"""

import sys

class _WindowsDB(object):
    def __repr__(self):
        return "Database for Windows platform"
class _LinuxDB(object):
    def __repr__(self):
        return "Database for Linux platform"

if sys.platform.startswith('win'):
    DB = _WindowsDB
else:
    DB = _LinuxDB
