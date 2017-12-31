#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CHAPTER4
"""

class Registor(object):
    """
    Registor
    """
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VolatageRegistance(Registor):
    """
    VolatageRegistance
    """
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

   
    @property
    def voltage(self):
        return self._voltage


    @voltage.setter
    def voltage(self, voltage):
        """
        Set voltage and calculate currnet.
        """
        self._voltage = voltage
        self.current = self._voltage / self.ohms

class BoundedRegistance(Registor):
    """
    BoundedRegistance
    """
    def __init__(self, ohms):
        super().__init__(ohms)
        self._ohms = self.ohms

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        """
        If ohms is equal or less than 0, ValueError occurs.
        """
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms

class ImmutableRegistance(Registor):
    """
    ImmutableRegistance
    """
    def __init__(self, ohms):
        super().__init__(ohms)
        self._ohms = self.ohms


    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        """
        This property is read only. If use this, AttributeError occurs.
        """
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't be set attribute")
        self._ohms = ohms
