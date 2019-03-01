import math

def distance(p1, p2):
    """distance -- takes two points as tuples, and returns the distance between them"""
    return math.sqrt((math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2)))

def test_dist():
    assert distance((0,0), (5,5)) == 7.0710678118654755
