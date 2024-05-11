import pytest
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(number_one=1, number_two=4)
    assert result == 5
    

def test_add_strings():
    result = my_functions.add(number_one='i like ', number_two='cars')
    assert result =='i like cars'

    
def test_divide():
    result = my_functions.divide(number_one=16, number_two=8)
    assert result == 2
    
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(number_one= 10, number_two=0)
    