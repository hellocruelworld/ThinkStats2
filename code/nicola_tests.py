#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 15:18:30 2020

@author: nicola.wong
"""

import numpy as np
import pandas as pd
    

def start_pandas():
#if __name__ == "__start_pandas__":
    
    x = 5
    #default index for series is len()-1 - so a numerical index 
        
   #myseries = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
    myseries = pd.Series(np.random.randn(x))
    #print("this type is " + str(type(myseries))) its not possible to use this fun
    print("finished learning this section")
 

if __name__ == "__main__":
# =============================================================================
#  commenting in a block is COMMAND + 4  
    
# =============================================================================
#     x = 9
# =============================================================================
#     for x in range (x,20):
#         print(x)
# =============================================================================
# =============================================================================
#    data = ["nicola", "lisa", "john"]
#    print("The length is " + str(len(data)))
#    index = [1,2,3]
#    print("The type is ")
#    print(type(data))
#    print(type(index))
#    s = pd.(data, index=index)
#    print(s)
#    print("looking at contents")
#    
#    for i in data:
#        print(i)
# =============================================================================

    #balloon data is a list of dicts. The content of the list can be accessed like an array. 
    balloon_data = [
        {"red": 1, "blue": 3},
        {"green":2, "blue":4},
        {"red":3, "blue":1}
        ]
    
    print("the first line of balloon data is " + str(type(balloon_data[0])))
    print("the full balloon data is " + str(type(balloon_data)))
    print(balloon_data[1])

    print("the length of balloon data is how many lines " +str(len(balloon_data)))
    
    #print("the first element of balloon data is "+ str(type(balloon_data[0].[0])))

    print("the third line red has contents " + str(balloon_data[0].get("blue")))
   # first_dataframe = pd.DataFrame(balloon_data, index=index)
    
    start_pandas()
    
    