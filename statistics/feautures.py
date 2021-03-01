from . import utils

def ioc(st):
    res = 0
    counted_runes = utils.count_runes(st)
    for key in counted_runes.keys():
        res += (counted_runes[key]*(counted_runes[key]-1))/(29*28)
    return res

def _runes_frequency(st):
    return utils.count_rune_frequency(st)

def runes_entropy(st):
    return utils.entropy(st)
