import math

"""def ord_of_mag(x, prefix=None):
    if prefix == "E":         # exa
        return x * (10**18)
    elif prefix == "P":      # peta
        return x * (10**15)
    elif prefix == "T":      # tera
        return x * (10**12)
    elif prefix == "G":      # giga
        return x * (10**9)
    elif prefix == "M":      # mega
        return x * (10**6)
    elif prefix == "k":      # kilo
        return x * (10**3)
    elif prefix == "h":     # hecto
        return x * (10**2)
    elif prefix == "da":      # deka
        return x * (10**1)
    elif prefix == None:
        return x * (10**0)
    elif prefix == "d":      # deci
        return x * (10**(-1))
    elif prefix == "c":     # centi
        return x * (10**(-2))
    elif prefix == "m":     # milli
        return x * (10**(-3))
    elif prefix == "u":     # micro
        return x * (10**(-6))
    elif prefix == "n":      # nano
        return x * (10**(-9))
    elif prefix == "p":      # pico
        return x * (10**(-12))
    elif prefix == "f":     # femto
        return x * (10**(-15))
    elif prefix == "a":      # atto
        return x * (10**(-18))
    else:
        return NULL"""

def unit_conversion(x, frm, to):
    if isinstance(frm, str):
        raise TypeError
    # exa(E) --> *
    if frm == 'E':
        if to == '*':
            return x * (10**18)
    '''# TODO: m --> kilo(k)
    if from == '*':
        if to == 'k':
            return (x * (1/1000))
    # TODO: m --> centi(c)
        elif to == 'c':
            return (x * 100)
    # TODO: m --> micro(u)
        elif to == 'u':
            return (x * 1000000)
    # TODO: m --> nano(n)
        elif to == 'n':
            return (x * 1000000000)

    # TODO: kilo(k) --> m
    if from == 'k':
        if to == None:
            return (x * 1000)
    # TODO: kilo(k) --> centi(c)
        elif to == 'c':
            return (x * 100000)

    # TODO: centi(c)--> kilo(k)
    if from == 'c':
        if to == 'k':
            return (x * 100000)
    # TODO: centi(c) --> m
        elif to == None:
            return
    # TODO: centi(c) --> micro(m)
        elif to == 'm':
            return
    # TODO: centi(c) --> nano(n)
        elif to == 'n':
            return

    # TODO: micro(u) --> centi(c)
    if from == 'u':
        if to == 'c':
            return
    # TODO: micro(u) --> nano(n)
        elif to == 'n':
            return'''

def distance(p1: int, p2: int) -> float:
    """distance -- takes two points as tuples, and returns the distance between them"""
    return math.sqrt((math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2)))
