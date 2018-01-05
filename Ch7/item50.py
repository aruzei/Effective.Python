#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""#50 in chapter7

Use package for module configuration and provide stable API.

"""

from model.glm import GLM
from model.gmm import GMM
import model.utils
from model.utils import print_model_doc as printm

from utils import print_model_doc


GLM = GLM()
GMM = GMM()

print_model_doc(GMM)
model.utils.print_model_doc(GMM)
printm(GLM)
