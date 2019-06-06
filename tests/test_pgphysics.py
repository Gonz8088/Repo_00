import math, pytest
from Repo_00.repo00.pgphysics import distance, unit_conversion

def test_dist():
    assert distance((0,0), (5,5)) == 7.0710678118654755
    assert distance((0,0), (0,5)) == 5
    assert distance((0,0), (2,0)) == 2
    assert distance((0,0), (1,2)) == 2.23606797749979
    assert distance((0,0), (0,2)) == 2
    assert distance((0,0), (-1,2)) == 2.23606797749979
    assert distance((0,0), (-2,0)) == 2
    assert distance((0,0), (-1,-2)) == 2.23606797749979
    assert distance((0,0), (0,-2)) == 2
    assert distance((0,0), (1,-2)) == 2.23606797749979

def test_unit_conversion():
    assert unit_conversion(-5, 'E', '*') == -5000000000000000000
    assert unit_conversion(0, 'E', '*') == 0
    assert unit_conversion(5, 'E', '*') == 5000000000000000000
    with pytest.raises(TypeError):
        unit_conversion('X', 'E', '*')
