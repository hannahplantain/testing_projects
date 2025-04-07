from lib.report_length import *

def test_report_length():
    result = report_length("A not very long string.")
    assert result == "This string was 23 characters long."

