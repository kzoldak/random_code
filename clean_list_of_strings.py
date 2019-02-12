

def identify_characters(string2search, chars2search):
    '''
    Return characters found in string.
    
    string2search - string
    chars2search - list of characters
    '''
    chars = chars2search
    return [ch for ch in string2search if ch in chars]


def replace_characters(string2fix, chars2remove):
    '''
    string2fix - string
    chars2remove - list of characters to remove
    '''
    for ch in chars2remove:
        string2fix = string2fix.replace(ch,'')
    return string2fix



def clean_strings(listOfStrings, chars2keep=None):
    '''
    listOfStrings: list of strings 
    chars2keep: list of str, characters you wish the cleaning to ignore.
                such as '_' or '.'.
    
    '''
    import string  # characters
    chars = string.punctuation
    # remove underscores. We want to keep all underscores.
    
    if chars2keep is not None:
        for ch in chars2keep:
            chars = chars.replace('\%s'%ch,'')
    
    # GET RID OF CHARACTERS
    los = listOfStrings
    for i,s in enumerate(los):
        if any(char in s for char in chars):
            chars2remove  = identify_characters(s, chars)
            s  = replace_characters(s, chars2remove)
            los[i] = s  # update column name 
    
    del s
    los = [s.replace(' ','_') for s in los]
    los = [(s.rstrip('_') if s.endswith('_') else s) for s in los]
    los = [(s.lstrip('_') if s.startswith('_') else s) for s in los]
    return los


strings_to_clean = ['_dog_', ' cat ', 'h@ampster', 'ho.rse ', 'du^%ck*', 'tu!!tle__']


clean_strings(strings_to_clean)


