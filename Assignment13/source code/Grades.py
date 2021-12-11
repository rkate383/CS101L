import math

def total(values):
    return sum(values)

def average(values):
    if len(values)== 0:
        return math.nan
    else:
        return total(values)/len(values)

def median(values):
    l = len(values)
    if l == 0:
        raise ValueError
    index = l // 2
    if l % 2:
        return sorted(values)[index]
    return sum(sorted(values)[index - 1: index + 1]) / 2

