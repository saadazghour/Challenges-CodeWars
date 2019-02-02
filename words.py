'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

def find_short(s):

    words = s.split(' ')
    words.sort(key=len)
    return len(words[0])



# other Method

def find_Short(s):
    words = s.split()
    return len(min(words, key=len))