from overlap import overlap_area
from pytest import approx
def test_basic():
    ''' Tests that basic example works '''
    big_field = (1, 1, 4, 4)
    inner_field = (2, 2, 3, 3)
    assert overlap_area(big_field, inner_field) == 1

def test_partial_overlap():
    ''' Tests when there's a partial overlap'''
    base_field = (1, 1, 4, 3)
    over_field = (2, 2, 3, 4)
    assert overlap_area(base_field, over_field) == 1

def test_corner_overlap():
    ''' Tests when there's a partial overlap'''
    base_field = (1, 0, 3, 5)
    over_field = (2, 4, 4, 6)
    assert overlap_area(base_field, over_field) == 1

def test_edge_touching():
    ''' Test when there is an edge '''
    base_field = (1, 1, 4, 4)
    over_field = (2, 2, 3, 4)
    assert overlap_area(base_field, over_field) == 2

def test_edge_touching():
    ''' Test when there is an edge '''
    base_field = (1, 1, 4, 4)
    over_field = (2, 1, 3, 4)
    assert overlap_area(base_field, over_field) == 3

def test_outside_edge_touching():
    ''' Test when they are touching on the outside '''
    base_field = (1, 1, 4, 4)
    over_field = (2, 4, 3, 5)
    assert overlap_area(base_field, over_field) == 0

def test_no_overlap():
    ''' Test when they are not touching each other '''
    base_field = (0, 0, 3, 3)
    over_field = (4, 4, 5, 5)
    assert overlap_area(base_field, over_field) == 0

def test_floats():
    ''' Test that still works when using floats '''
    base_field = (1, 1., 3.5, 3.5)
    over_field = (3, 3, 5, 5)
    assert overlap_area(base_field, over_field) == 0.5 * 0.5

def test_floats():
    ''' Test that still works when using floats '''
    base_field = (1, 1., 3.3, 3.1)
    over_field = (3, 3, 5, 5)
    assert overlap_area(base_field, over_field) == approx(0.3 * 0.1, rel=1e-3)
