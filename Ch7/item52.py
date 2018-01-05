#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""#52 in chapter7

How to avoide cyclic reference
"""

# module1 -> module2 -> module3, module4, module5
# module3.func3() -> module1.func1()

from module1 import func1
from module2 import func2
from module3 import func3
from module4 import func4

func1()
func2()
func3()
func4()
