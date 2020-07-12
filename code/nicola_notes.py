#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 18:51:17 2020

@author: nicola.wong
"""
import pandas as pd

def notes_testing():
        
    d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c'],name= "series1"),
   'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'], name= "series2")}
    
    print("printing the whole dataframe\n\n")
    print(d)
    print("printing one column using dot notation\n\n")
    one = d["one"]
    print(one)
    print("printing the count\n\n")
    one.value_counts().sort_index()

if __name__ == "__main__":

# =============================================================================
#     x = "Hello World"	                             str	
#     x = 20	                                       int	
#     x = 20.5	                                    float	
#     x = 1j	                                       complex	
#     x = ["apple", "banana", "cherry"]	            list	
#     x = ("apple", "banana", "cherry")	                tuple	
#     x = range(6)	                                   range	
#     x = {"name" : "John", "age" : 36}	               dict	
#     x = {"apple", "banana", "cherry"}	              set	
#     x = frozenset({"apple", "banana", "cherry"})	frozenset	
#     x = True	                                   bool	
#     x = b"Hello"	                               bytes	
#     x = bytearray(5)	                           bytearray	
#     x = memoryview(bytes(5))	                   memoryview
# =============================================================================

# =============================================================================
# 
    #SERIES - 1 dimensional data type, similar to a dict as it has an index 
    #it can also have a name! add in as an argument 
# #index defaults to len()-1 if you dont pass in the parameter
#     
# In [3]: s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
# 
# In [4]: s
# Out[4]: 
# a    0.469112
# b   -0.282863
# c   -1.509059
# d   -1.135632
# e    1.212112
# dtype: float64
# =============================================================================
    
# =============================================================================
#   DICTS are 2 dimensional. It is just like Excel - with indexed ROWS(y) and COLUMNS (x)
    #Think in key value pairs. 
    
    
    #In [37]: d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
#    ....:      'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
#    ....: 
# 
# In [38]: df = pd.DataFrame(d)
# 
# In [39]: df
# Out[39]: 
#    one  two
# a  1.0  1.0
# b  2.0  2.0
# c  3.0  3.0
# d  NaN  4.0
# =============================================================================
    
    
    notes_testing()
    
    print("Good luck....")