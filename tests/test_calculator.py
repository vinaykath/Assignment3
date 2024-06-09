'''My Calculator Test'''
import pytest
from calculator import add, subtract, multiply, divide

def test_addition():
    '''Test that addition function works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction function works '''    
    assert subtract(2,2) == 0

def test_multiply():
    '''Testing if Multiplication works'''
    assert multiply(2,2) ==4

def test_divide():
    '''Testing if division works'''
    assert divide(2,2) ==1

def test_Zero():
    """Dividing by Zero"""
    with pytest.raises(ZeroDivisionError):
        divide (2,0)
