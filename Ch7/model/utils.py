#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""utils

Provide utilities for models

"""

def print_model_doc(model):
    """Print document of the given model"""
    print(model.__class__.__name__, ':', model.__doc__)
