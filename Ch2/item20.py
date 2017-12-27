#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER2
"""

from datetime import datetime

def __log(message, when=None):
    when = datetime.now()
    print('%s: %s' %(when, message))

__log('Hi there!')
__log('Hi again!')


def __decode_json_dangerous(data, default={}):
    import json
    try:
        return json.loads(data)
    except ValueError:
        return default

FOO = __decode_json_dangerous('Invalid')
BAR = __decode_json_dangerous('Bad')

FOO['stuff'] = "Default is shared."
BAR['meep'] = "This is dangerous."

print('Foo:', FOO)
print('Bar:', BAR)

def __decode_json(data, default=None):
    import json
    if default is None:
        default = {}
    try:
        return json.loads(data)
    except ValueError:
        return default

FOO = __decode_json('Invalid')
BAR = __decode_json('Bad')

FOO['stuff'] = "Default is not shared."
BAR['meep'] = "This is safe."

print('Foo:', FOO)
print('Bar:', BAR)
