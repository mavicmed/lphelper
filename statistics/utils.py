import math

from ..converters.core import runes

def count_runes(st):
    res = 0
    counted_runes = {}
    for r in runes:
        counted_runes[r] = st.count(r)
    return counted_runes

def count_rune_frequency(st):
    counted_runes = count_runes(st)
    for key in counted_runes.keys():
        counted_runes[key] = counted_runes[key]/len(st)
    return counted_runes

def entropy(st):
        string = ''.join(st)
        "Calculates the Shannon entropy of a string"
        # get probability of chars in string
        prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]
        # calculate the entropy
        entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

        return entropy
