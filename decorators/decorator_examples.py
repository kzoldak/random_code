#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:01:09 2019

@author: kimzoldak
"""


import os
direc = "/Users/kimzoldak/Github/random_python_code/decorators/"
os.chdir(direc)


"""

        PYTHON DECORATORS
        
Decorators wrap a function in order to modify its behavior, without actually
changing the code within it. 

The structure should go like this:
    
    def decorator_fuction():
        def wrapper_function():
            Does something to ANOTHER function.
        return wrapper_function 
        
The inside wrapper function does something to a third function, 
and that something is returned to the decorator function. 
        

"""




def my_decorator(func):
    def wrapper():
        print('')
        print("** Something is happening before the function is called. **")
        func()
        print("** Something is happening after the function is called. **")
        print('')
        print("I don't want to change the original function, so I use a python ")
        print("decorator to wrap the outside function.")
        print('')
    return wrapper


# THE THIRD OUTSIDE FUNCTION THAT THE DECORATOR WILL BE APPLIED TO. 
def outside_function():
    print("\nThis is a function that exists somewhere in a file.\n")

    
# CALL OUTSIDE FUNCTION WITHOUT THE DECORATOR.
outside_function()
    
# APPLICATION OF DECORATOR TO THE OUTSIDE FUNCTION.
outside_function = my_decorator(outside_function)


# NOW RUN THE OUTSIDE FUNCTION AGAIN.
outside_function()



"""

`my_decorator` and `wrapper` are simply two functions that are applied to 
another function, `outside_function`. 
So when you apply the decorator to the function and then call that function, 
the order of operations are as follows:
    1. call `outside_function`, but don't run its code.
    2. this prompts a call to the ` my_decorator` function, which then returns
        the contents of the `wrapper` function.
    3. call to `wrapper` now runs its contents:
        3a) prints some things.
        3b) calls `func` with `func()` statement. This is where the contents of
            `outside_function` runs, since `func` is an alias 
            for `outside_function` once the decorator is applied to it. 
        2c) prints some things.
    3. `outside_function` terminates
    
I'd like to point one thing out. If you put a print statement within 
`my_decorator`, but above the `def wrapper()` line, that statement will NOT
print when you make a call to `outside_function`. It will ONLY print when
you assign the decorator to the function.  See below:
"""


def my_decorator(func):
    print("* my_decorator")
    def wrapper():
        print('')
        print("* wrapper before func call")
        func()
        print("* wrapper after func call")
        print('')
    return wrapper

# THE THIRD OUTSIDE FUNCTION THAT THE DECORATOR WILL BE APPLIED TO. 
def outside_function():
    print("* outside_function()")

outside_function()  # prints: * outside_function()
    
outside_function = my_decorator(outside_function) # prints: * my_decorator

outside_function()
#    prints:
#    * wrapper before func call
#    * outside_function()
#    * wrapper after func call




from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

say_whee = not_during_the_night(say_whee)

say_whee()



"""
In this form, you can manipulate a function without actually having 
acces to its code. Let's look at another example of this. 

In the code below, I have a function called `plot_data` that is 
imported from a file. This function simply performs matplotlib.plyplot's basic
`plt.plot(*args, **kwargs)`, where *args will be a list of the x and y data 
and **kwargs will be the remainder of the matplotlib.pyplot plotting arguments.
 

This basic plot command will NOT apply x- and y-axis labels, and I want those!
So, instead of looking through files to find where that function is and edit
its code, I can use a decorator to wrap the `plot_data` function and add
x- and y-axis labels. 

"""


import numpy as np
import matplotlib.pyplot as plt

# Import the plotting function from file.
from plotting import plotting_data


# Make some data.
xdata = np.linspace(-2, 2, 100)
ydata = np.sin(np.pi * xdata)

plot_data = plotting_data

# Plot the data using the function. 
plot_data(xdata, ydata)

# I should point out that this works as well:
plot_data(*[xdata, ydata])
# and setting both up as a list to pass to the function:
data = [xdata, ydata]
plot_data(*data)
# These work as long as you provided x and y in the right order, since the 
# plot_data function is set up to take the x argument first.
# Take a look at its Signature:
?plot_data





# Now, write a decorator with a wrapping function that will overlay 
# x- and y-axis labels on the plot. *args will take the list of x and y data
# values and **kwargs will take a dictionary of plotting arguments, 
# aka key-word arguments.



def my_decorator(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs) 
        plt.xlabel('x', fontsize=16)
        plt.ylabel('y', fontsize=16)
    return wrapper

# Make alias fot plotting_data so we don't change it, only its alias.
plot_data = plotting_data

# Apply the decorator function to it.
plot_data = my_decorator(plot_data) 

# Now plot again:
plot_data(*data) 
# We now have x- and y-axis labels.


# Now lets pass a dictionary of plotting argument keywords and their values.
# DICTIONARY OF PLOTTING ARGUMENTS
pltKwargs = dict(color='red', 
                 linestyle='--',
                 linewidth=3,
                 alpha=0.5)

# Now perform plot again.
plot_data(*data, **pltKwargs) 

"""
In the example above, we techinically can access the code in the plotting.py
file and change it so that it plots the x- and y-axis labels. We could do this 
becuase it is our own code and changing it will not mess anything else up. 
However, this is not true for the code within a Python package that was built
by someone else, such as `pandas`. So, for a realistic example, we will use
the `pandas` package and write a wrapper around its plotting function. 


"""

# Retrieve already cleaned data. 
# These are my PG&E energy usage and costs per bill cycle.
# Each row is a single hour of data. Thus, there are 24 rows per day.
from data import get_pge_data

pge = get_pge_data()

pge.head() # view part of dataframe

# Group dataframe by `DATE` and calculate the mean energy usage per day. 
pge.groupby('DATE').USAGE.mean()

# Using Pandas Series, plot the mean useage per day 
pge.groupby('DATE').USAGE.mean().plot()


"""
What you should notice is that pandas plotting function is not plotting the 
y-axis label. Lets fix that with a decorator!


Although I can view the pandas `pge` DataFrame and the pandas Series that 
`pge.groupby('DATE').USAGE.mean()` creates, I can't actually use any of the 
pandas functions without importing it first.

Import it using:   
import pandas as pd

Then do: 
pd.Series.plot.__call__

This is the function we are looking for! This will be our function.
"""

import pandas as pd



pge.groupby('DATE').USAGE.mean().plot()


function = pd.Series.plot.__call__


def my_decorator(func, *args, **kwargs):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs) 
        #plt.xlabel('x', fontsize=16)
        plt.ylabel('y', fontsize=16)
    return wrapper



function = pge.groupby('DATE').USAGE.mean().plot.__call__


function = my_decorator(function) 
function()



# Make alias fot plotting_data so we don't change it, only its alias.
plot_data = plotting_data

# Apply the decorator function to it.
plot_data = my_decorator(plot_data) 






print(pd.Series.plot.__doc__)
# available: line, bar, hist

print(pd.Series.plot.__dict__)
# available: line, bar, barh, hist, box, kde, density, area, pie


pge.groupby('DATE').USAGE.mean().plot()
# Default is kind='line'
pge.groupby('DATE').USAGE.mean().plot(kind='line')
pge.groupby('DATE').USAGE.mean().plot.line()

pge.groupby('DATE').USAGE.mean().plot(kind='density')
pge.groupby('DATE').USAGE.mean().plot.density()

pge.groupby('DATE').USAGE.mean().plot(kind='kde')
pge.groupby('DATE').USAGE.mean().plot.kde()

pge.groupby('DATE').USAGE.mean().plot(kind='area')
pge.groupby('DATE').USAGE.mean().plot.area()

pge.groupby('DATE').USAGE.mean().plot(kind='hist', bins=30)
pge.groupby('DATE').USAGE.mean().plot.hist(bins=30)


# TOO MANY FOR BAR, BARH, PIE
pge.groupby('DATE').USAGE.mean().plot(kind='bar')
pge.groupby('DATE').USAGE.mean().plot.bar()
pge.groupby('DATE').USAGE.mean().plot(kind='barh')
pge.groupby('DATE').USAGE.mean().plot.barh()
pge.groupby('DATE').USAGE.mean().plot(kind='pie')
pge.groupby('DATE').USAGE.mean().plot.pie()




pge.groupby('DATE').USAGE.mean().name
pge.groupby('DATE').USAGE.mean().values

plotting_function = pd.Series.plot.__call__

kwargs = pd.Series.plot.__dict__

"""
We don't want to actually call the function. 
We want to

"""



def my_decorator(*args, **kwargs):
    f = pd.Series.plot.__call__
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        s = args[0].__dict__['_data']
        if s.name:
            try:
                kind = kwargs['kind']
            except KeyError:
                kind = 'line'
            if kind == 'line' or kind == 'scatter':
                plt.ylabel(s.name)
            elif kind == 'hist':
                plt.xlabel(s.name)
        return res

kim = my_decorator(pge.groupby('DATE').USAGE.mean().plot.__call__)

pge.groupby('DATE').USAGE.mean()

kim()




pd.Series.plot.__call__ = _decorator


function = pge.groupby('DATE').USAGE.mean().plot.__call__

function = my_decorator(function) 
function()


from functools import wraps

def patch_series_plot():
    """Makes Series.plot to show series name as ylabel/xlabel according to plot kind."""
    f = pd.Series.plot.__call__
    @wraps(f)
    def _decorator(*kargs, **kwargs):
        res = f(*kargs, **kwargs)
        s = kargs[0].__dict__['_data']
        if s.name:
            try:
                kind = kwargs['kind']
            except KeyError:
                kind = 'line'
            if kind == 'line' or kind == 'scatter':
                plt.ylabel(s.name)
            elif kind == 'hist':
                plt.xlabel(s.name)
        return res
    pd.Series.plot.__call__ = _decorator
patch_series_plot()

zol = pd.Series.plot.__call__


pge.groupby('DATE').USAGE.mean().plot()









def patch_series_plot():
    """Makes Series.plot to show series name as ylabel/xlabel according to plot kind."""
    f = pd.Series.plot.__call__
    @wraps(f)
    def _decorator(*kargs, **kwargs):
        res = f(*kargs, **kwargs)
        s = kargs[0].__dict__['_data']
        if s.name:
            try:
                kind = kwargs['kind']
            except KeyError:
                kind = 'line'
            if kind == 'line' or kind == 'scatter':
                plt.ylabel(s.name)
            elif kind == 'hist':
                plt.xlabel(s.name)
        return res
    pd.Series.plot.__call__ = _decorator
patch_series_plot()





"""
Without the decorator wrapping the `outside_function`, calling 


You can apply the decorator function `my_decorator` to the function 
in two ways:
    1. To use it 
    say_whee = my_decorator(say_whee)
Another way to structure this is to use the 

"""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# THE THIRD OUTSIDE FUNCTION THAT THE DECORATOR WILL BE APPLIED TO. 
@my_decorator
def say_whee():
    print("Whee!")

# RUN THE FUNCTION.
say_whee()