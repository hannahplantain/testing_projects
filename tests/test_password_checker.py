import pytest
from lib.password_checker import *

#get the code to return the error message

def test_password_checker_invalid_password():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check("1234")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
