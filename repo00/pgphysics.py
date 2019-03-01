import math

def distance(p1: int, p2: int) -> float:
    """distance -- takes two points as tuples, and returns the distance between them"""
    return math.sqrt((math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2)))
