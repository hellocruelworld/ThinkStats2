"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2
import chap01soln

def solution_file():
    resp = chap01soln.ReadFemResp()
    print(str(resp.head()))
    
    print(chap01soln.ValidatePregnum(resp))
    
    


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    print("Running module\n\n")
    solution_file()
    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
