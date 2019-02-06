#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

In this file, I will keep useful python functions that I have written. 
These are not specific for math or science computations, but more for
object-oriented programming. These can be used as class attributes that are 
frequently needed by the user.

I will format them as traditional functions, but will provide the shortened
lambda function, or list comprehension, with the same functionality. 
Lambda functions do not allow for docstrings, which is extremely useful 
sometimes. 


"""


def print_docstring_shortcut(ntabs=1, case=None):
    '''
    print_docstring_shortcut(ntabs=1, case=None)
    
    Prints the docstring headers in a format that will keep all your 
    docstrings clean and consistent. 
    
    
    PARAMETERS:
    -----------
    nTabs: int, number of tabs to use when indenting the docstring text.
            Default ntabs=1, since most functions are indented by 1 tab, or
            4 spaces. This can be changed to 0, or any other integer number.
    
    case: 0, 1, or None. Tells function whether you want to use all 
            lowercase (case=0) letters or all uppercase (case=1) for the 
            docstring headers. Default is case=None. If left as None, the 
            first letter of every header is upper case and the rest are 
            lowercase. 
        
    NOTES:
    ------
    Headers are:
    ['Parameters', 'Returns', 'Raises', 'Notes', 'References', 
    'See Also', 'Examples']
    
    
    EXAMPLES
    --------
    print_docstring_shortcut(ntabs=0, case=None)
    print_docstring_shortcut(ntabs=1, case=1)
    print_docstring_shortcut(ntabs=2, case=0)
    
    '''
    
    heads = ['Parameters', 'Returns', 'Raises', 'Notes', 
             'References', 'See Also', 'Examples']
    
    if case is not None:
        if case == 0:
            heads = [head.lower() for head in heads]
        elif case == 1:
            heads = [head.upper() for head in heads]
    else:
        pass
            
    ntabs = ntabs
    tab = '\t'
    out = []
    for head in heads:
        out.append('\n\n'+tab*ntabs+head+'\n'+tab*ntabs+'-'*len(head))     
    print(''.join(out))   





#
#def _upper(values):
#    '''
#    _upper(values)
#    
#    Has same functionality of 'word'.upper(), but can take lists of strings.
#    Capitalizes all letters in each string within a list of strings. 
#
#     
#    PARAMETERS
#    ----------
#    values: list of strings. 
#            If values is a single string, it will be 
#            separated into a list of individual letters and all will be
#            capitalized.
#            
#    
#    NOTES
#    -----
#    LIST COMPREHENSION VERSION:
#        _upper = lambda values: [value.upper() for value in values]
#        _upper(words)
#    
#    
#    EXAMPLES
#    --------
#    words = ['label', 'axis', 'axes']
#    _upper(values)
#    _upper('kim')
#    
#    '''
#    return [value.upper() for value in values]
#
#
#
#def _lower(values):
#    '''
#    _lower(values)
#    
#    Has same functionality of 'Word'.lower(), but can take lists of strings.
#    Lowercases all letters in each string within a list of strings. 
#     
#    PARAMETERS
#    ----------
#    values: list of strings. 
#            If values is a single string, it will be 
#            separated into a list of individual letters and all will be
#            lowercased.
#            
#    
#    NOTES
#    -----
#    LIST COMPREHENSION VERSION:
#        _lower = lambda values: [value.lower() for value in values]
#        _lower(words)
#    
#    
#    EXAMPLES
#    --------
#    words = ['Label', 'Axis', 'Axes']
#    _lower(words)
#    _lower('KIM')
#    
#    '''
#    return [value.lower() for value in values]



_upper = lambda values: [value.upper() for value in values]
# THIS IS HOW YOU ENTER DOCSTRINGS FOR LAMBDA FUNCTIONS
_upper.__doc__ = '''
    _upper(values)
    
    Has same functionality of 'word'.upper(), but can take lists of strings.
    Capitalizes all letters in each string within a list of strings. 

     
    PARAMETERS
    ----------
    values: list of strings. 
            If values is a single string, it will be 
            separated into a list of individual letters and all will be
            capitalized.
            
    
    NOTES
    -----
    LIST COMPREHENSION VERSION:
        _upper = lambda values: [value.upper() for value in values]
        _upper(words)
    
    
    EXAMPLES
    --------
    words = ['label', 'axis', 'axes']
    _upper(values)
    _upper('kim')
    
    '''





_lower = lambda values: [value.lower() for value in values]
_lower.__doc__ =  '''
    _lower(values)
    
    Has same functionality of 'Word'.lower(), but can take lists of strings.
    Lowercases all letters in each string within a list of strings. 
     
    PARAMETERS
    ----------
    values: list of strings. 
            If values is a single string, it will be 
            separated into a list of individual letters and all will be
            lowercased.
            
    
    NOTES
    -----
    LIST COMPREHENSION VERSION:
        _lower = lambda values: [value.lower() for value in values]
        _lower(words)
    
    
    EXAMPLES
    --------
    words = ['Label', 'Axis', 'Axes']
    _lower(words)
    _lower('KIM')
    
    '''
    



def _unique(values, sort=False):
    '''
    _unique(values, sort=False)
    
    Similar to numpy's unique function, but default does not sort
    the output into alphabetical order. Sort option available.
    
    PARAMETERS:
    ----------
    values: list of str. 
    sort: True or False. Default is False. 
    		If user wants sorted list, use sort=True
    
    RETURNS:
    -------
    Returns a unique list of values, without sorting. 
    
    EXAMPLES:
    keys = ['label.fontsize', 'ytick.labelright', 'axes.labelsize', 
            'axis.x_label', 'axis.x_label', 'axes.labelsize']
    _unique(keys)
    _unique(keys, sort=True)
    
    EXAMPLES:
    --------
    colors = ['yellow', 'brown', 'green', 'blue', 
              'brown', 'purple', 'red', 'green']
    _unique(colors)  # sort is False by default
    _unique(colors, sort=True)
    
    '''
    unique_values = []
    for val in values:
        if val in unique_values:
            pass
        else:
            unique_values.append(val)
    unique_values = (sorted(unique_values) if sort else unique_values) # sort if sort=True
    return unique_values



