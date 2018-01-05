#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""#51 in chapter7

Define a root exception to insulate callers from APIs
"""

import logging

def determin_weight(volume, density):
    """Calculate weight.

    If density is not positive, raising InvalidDensityError.
    """
    if density <= 0:
        raise InvalidDensityError('Density must be positive')

    return volume * density

class Error(Exception):
    """Base class for all exceptions raised by this modules."""

class InvalidDensityError(Error):
    """There was a problem with a provided density value."""

class NegativeDensityError(InvalidDensityError):
    """A provided density value was negative."""

def _determin_weight(volume, density):
    try:
        weight = determin_weight(volume, density)
    except NegativeDensityError as ner:
        raise ValueError('Must supply non-negative density') from ner
    except InvalidDensityError:
        weight = 0
    except Error as error:
        logging.error('Bug in the calling code: %s', error)
    except Exception as ex:
        logging.error('Bug in the API code: %s', ex)
        raise
    return weight

print(_determin_weight(1, 1))
print(_determin_weight(1, 0))
print(_determin_weight(1, '0'))
