#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:36:33 2019

@author: kimzoldak
"""

import re
import numpy as np
import matplotlib.pyplot as plt


## *--------------*
## USEFUL FUNCTIONS
## *--------------*

# CAPITALIZE ALL LETTERS IN EVERY WORD OF A LIST.
_upper = lambda values: [value.upper() for value in values]
# MAKE ALL LETTERS IN EACH STRING OF LIST LOWERCASE
_lower = lambda values: [value.lower() for value in values]



def _unique(values, sort=False):
    unique_values = []
    for val in values:
        if val in unique_values:
            pass
        else:
            unique_values.append(val)
    unique_values = ( sorted(unique_values) if sort else unique_values)
    return unique_values
    

keys = ['label.fontsize', 'ytick.labelright', 'axes.labelsize', 'axis.x_label', 'axis.x_label', 'axes.labelsize']
_unique(keys)
_unique(keys, sort=True)








def searching(str1, str2):
    if str1 in str2:
        out = str2
    else:
        out = 'na' # can use None here also
    return out

#searching = lambda str1, str2: [str2 if str1 in str2 else 'na']


    
    
searching('kim','kim zoldak') # returns 'kim zoldak'
searching('kim','zoldak')  # returns Nothing
searching('kim','Kim Zoldak') # returns nothing

# This runs, but returns wrong answer. 
# FUNCTION NOT MEANT TO TAKE LISTS
searching(['kim', 'derek'], ['kim zoldak','stef lane'])  
# also wont work:
searching(['kim', 'derek'], ['kim zoldak','stef lane', 'derek meyers'])  


# VECTORIZE THE FUNCTION TO ALLOW IT TO TAKES LISTS.
searching_v = np.vectorize(searching)
searching_v(['kim', 'derek'], ['kim zoldak','stef lane'])
searching_v(['kim', 'derek'], ['kim zoldak','derek meyers'])

# Vectorizing worked as desired. However, the lists must be the same length.
# won't work, throws errror:
searching_v(['kim', 'derek'], ['kim zoldak','stef lane','derek meyers'])


# USE MAP FUNCTION. It allows multiple iterators to be passed to function. 
list(map(searching, *[['kim', 'derek'], ['kim zoldak','stef lane']]))  
list(map(searching, *[['kim', 'derek'], ['kim zoldak','derek meyers']])) 
# These worked as desired.  

# Using different sized lists won't work though.
list(map(searching, *[['kim', 'derek'], ['kim zoldak','stef lane', 'derek meyers']]))
# We did not get an error, but the output was not the desired result. 


# BUILDING OUR OWN FUNCTION TO TAKE TWO LISTS AND SEARCH BOTH FOR MATCHES. 
'''
We are not specifically looking for *exact* matches. We are looking to see 
if the words within the first list of strings is found (in any form) within 
the second list of strings. 

Example:
-------
list1 = ['label', 'axis']
list2 = ['label.fontsize', 'yticks.direction', 'xticks.location', 
         'axis.xaxis', 'axis.ylabel']

From this example, we would want the 0th and 3rd, and 4th strings listed in 
list2 to be returned. This is becuase 'label' and 'axis' are within each one 
of these strings. Notice though that both 'axis' AND 'label' are found within
the 4th string in the list2 list. This means it should be returned twice, 
once for each label. However, we would like to be able to choose only the 
uniquie solutions, so we can use numpy's unique function to do this. 

Another concer we have, what if list2 is a VERY long list of strings. We may 
find that 'Axis.formatter' is within list2 and we might want that to be 
returned as well. To do this, we need a way of controlling the case sensitivity
of the function. All will be achieved within this function. 


We clearly know now that searching function above, as well as its vectorized
version, will not work for this task.

'''








def str_contains(list1, list2, unique=True, case=True):
    '''
    str_contains(list1, list2, unique=True, case=True)
    
    We want to find all the string elements within list2 that contain 
    some part of any of the strings in list1. See example below for
    clarity.
    
    PARAMETERS
    ----------
    
    
    where any of the words 
    list1 should be the list of words you would like to see if they are
    contained, in some way, within list2. 
    Lists do not need to be equal in length. 
    
    EXAMPLE:
    ----------
    list1 = ['label', 'axis', 'axes']
    list2 = ['label.size', 'yticks.direction', 'xticks.size',
            'axes.labels', 'axis.limits', 'legend.labelspacing']
    We can see that, within list2, the 0th, 3rd, 4th, and 5th are all matches.
    Each have one of the words from list1 within them. We would like the 
    mathces to be returned. However, we only need one copy of each, 
    so we use np.unique to handle copies. 
    
    '''
    hits = []
    for i in list1:
        for j in list2:
            if case:
                if i in j:
                    hits.append(j)           
            else:
                if i.lower() in j.lower():
                    hits.append(j)
    if unique:
        import numpy as np
        hits  = list(np.unique(hits))
    return hits







# SIMPLE EXAMPLES FIRST
words = ['label', 'axis', 'axes']

keys  = ['label.fontsize', 'yticks.direction', 'xticks.major.top', 
         'ytick.labelright', 'ytick.minor.visible', 'axes.labelsize', 
         'Axes.grid.which', 'axis.x_label']


'''
By eye, what would the output look like?

 FOR word = 'label'
      out:  ['label.fontsize', 'ytick.labelright', 'axes.labelsize', 'axis.x_label']
 FOR word = 'axis'
      out:  ['axis.x_label',]
 FOR word = 'axes'
      out:  ['axes.labelsize',}
    
We are treating it as if KNOW  'Axes.grid.which' will be ignored becuase 
the function is not case sensitive. 

That is a total of 6 matches. However, the default of the function is to 
use numpy's unique function, so this will get rid of duplicates. 
That leaves a total of 4:
    out:  ['label.fontsize', 'ytick.labelright', 'axes.labelsize', 'axis.x_label']

'''


# FIRST LETS USE unique = False
result = str_contains(words, keys, unique=False)
print(result)
print(len(result)) 
 
# out:  ['label.fontsize', 'ytick.labelright', 'axes.labelsize', 'axis.x_label', 'axis.x_label', 'axes.labelsize']
# out: 6




# LEAVE OFF unique = False, SINCE unique = True IS THE DEFAULT. 
result = str_contains(words, keys)
print(result)
print(len(result)) 

# out:  ['axes.labelsize' 'axis.x_label' 'label.fontsize' 'ytick.labelright'] 
# out: 4



#  WE GET THE RESULT WE EXPECTED, except numpy's unique function sorts output
#  into alphabetical order. I don't care about this, but if you do, you can
#  write and use your own unique function. 
#  
# np.unique(ar, return_index=False, return_inverse=False, return_counts=False, axis=None)
# If you don't like this, you can write you own unique function. 
# See mine at the beginning. 









## *--------------*
## TESTING CASE SENSITIVITY
## *--------------*

words = ['label', 'axis', 'axes']

keys  = ['label.fontsize', 'yticks.direction', 'xticks.major.top', 
         'ytick.labelright', 'ytick.minor.visible', 'axes.labelsize', 
         'Axes.grid.which', 'axis.x_label']


# case=True
result = str_contains(words, keys, unique=True, case=True)
print(result)
print(len(result))  

# out:  ['axes.labelsize' 'axis.x_label' 'label.fontsize' 'ytick.labelright']
# out: 4



# case=False
result = str_contains(words, keys, unique=True, case=False)
print(result)
print(len(result)) 

# out:  ['Axes.grid.which' 'axes.labelsize' 'axis.x_label' 'label.fontsize' 'ytick.labelright'] 
# out: 5




words = ['Label', 'axis', 'Axes']

keys  = ['label.fontsize', 'yticks.direction', 'xticks.major.top', 
         'ytick.labelright', 'ytick.minor.visible', 'axes.labelsize', 
         'Axes.grid.which', 'axis.x_label']

result = str_contains(words, keys, unique=True, case=False)
print(result)
print(len(result))  

# out: ['Axes.grid.which', 'axes.labelsize', 'axis.x_label', 'label.fontsize', 'ytick.labelright']
# out: 5










#   ADVANCED EXAMPLE
'''
BACKGROUND:
We want to change a matplotlib default plotting parameter, using:
    plt.rcParams['']


'''



import matplotlib.pyplot as plt

words = ['label', 'axis']
keys  = list(plt.rcParams.keys())


result = str_contains(words, keys, unique=True, case=False)
print(result)
print(len(result))  

# PRINT OUT THE rcParams KEYWORD AND ITS VALUE
for res in result:
    print( '%20s  %20s'%(res, plt.rcParams[res]) )




import numpy as np


x = np.linspace(0, 2, 100)
y = np.sin(np.pi * x)

#plt.figure(figsize=(9, 6))
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin$(\pi x)$')


plt.rcParams['axes.labelcolor'] = 'blue'
plt.rcParams['axes.labelsize'] = 26
plt.rcParams['ytick.labelright'] = True


plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin$(\pi x)$')

# RETURN RCPARAMS TO DEFAULTS:
default_params = plt.rcParamsDefault

plt.rcdefaults()

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('sin$(\pi x)$')

plt.rcParams['figure.figsize']

# plt.rcParams['figure.figsize']
# Out[48]: [6.4, 4.8]






# USE   case = False
result = str_contains(words, keys, case=False)
print(result)
print(len(result))
# as expected, 40 results returned. 



result = str_contains(words, keys, case=False)
print(result)
print(len(result))
# as expected, 40 results returned. 
















words = ['label', 'axis', 'axes']
keys  = list(plt.rcParams.keys())


result = str_contains(words, keys)
print(result)
print(len(result))  # 40



def str_contains2(list1, list2, unique=True):

    hits = [j for j in list2 for i in list1 if re.search(i, j) is not None]
    if unique:
        import numpy as np
        hits  = np.unique(hits)
    return hits



print(str_contains(words, keys))
print(len(str_contains(words, keys)))



print(str_contains2(words, keys))
print(len(str_contains2(words, keys)))


result1 = str_contains(words, keys, unique=True) 
result2 = str_contains2(words, keys, unique=True)

result1 == result2 # All True




