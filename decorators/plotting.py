#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:14:58 2019

@author: kimzoldak
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plotting_data(*args, **kwargs):
    """
    Can do everything plot_data_A and plot_data_B can do, and more. 
    This function also takes plotting arguments in dictionary form (**kwargs). 
    This allows the user to change the color, style, and thickness of the line, 
    as well as all other matplotlib.pylab plotting arguments for a simple plot.
    """
    return plt.plot(*args, **kwargs)

