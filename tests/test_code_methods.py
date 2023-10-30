import pytest
from datetime import timedelta
from application.func import verify_input
from application.datefunc import get_currdate, verify_date

future = str(get_currdate() + timedelta(2))
wronginputs = ["23-24-62", "1995-11-25", "2022-10-31", "Wrong input", "future", ]

def test_verify_date():
    for input in wronginputs:
        returnvalue = verify_date(input)
        if returnvalue is True:
            break
    assert returnvalue == False

def test_verify_input():
    pricegroup = "NO "
    for x in wronginputs:
        returnvalue = verify_input(x, pricegroup)
        if returnvalue is True:
            break
        pricegroup = "SE1"
    for x in wronginputs:
        returnvalue = verify_input(x, pricegroup)
        if returnvalue is True:
            break
    assert returnvalue == False



