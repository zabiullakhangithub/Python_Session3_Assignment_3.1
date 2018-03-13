# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 11:25:09 2018

@author: zabiulla.khan

Write a function to compute 5/0 and use try/except to catch the exceptions

"""
# Define a function which accepts two arguments
def Exceptions(a,b):
    try:
        # Perform division operation
        a/b
    except ZeroDivisionError:
        # Handle ZeroDivisionError
        print("Division by zero!")
        #Handle all other exceptions
    except Exception:
        print('Caught an exception')
        #Define finally block
    finally:
        print('In finally block for garbage collection and releasing resources')
        
Exceptions(5,0)
Exceptions(5,'a')