import pytest
from lib.present import *

#using pytest to assert the error that something is already wrapped in the present

def test_wrap_present_with_contents():
    teddy_bear = Present()
    teddy_bear.wrap("Teddy Bear")
    
    with pytest.raises(Exception) as e:
        teddy_bear.wrap("Slinky")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


#using pytest to assert that there is nothing in the present to unwrap

def test_unwrap_present_without_contents():
    teddy_bear = Present()
    with pytest.raises(Exception) as e:
        teddy_bear.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."