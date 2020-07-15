#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:48:37 2020

@author: nicola.wong
"""

# =============================================================================
# Which summary statistics would you use if you wanted to get a story on the evening news? 
# 
# Which ones would you use if you wanted to reassure an anxious patient?
# =============================================================================

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2
import chap01soln
import thinkplot


def make_histogram(preg):
    live = preg[preg.outcome == 1]
    print(live.head())
    print("Now creating histogram")
    hist = thinkstats2.Hist(live.birthwgt_lb, label='birthwgt_lb')
    thinkplot.Hist(hist)
    thinkplot.Show(xlabel='pounds', ylabel='frequency')


def main():
    preg = nsfg.ReadFemPreg()
    make_histogram(preg)
    

if __name__ == '__main__':

    main()