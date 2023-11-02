import pytest
from datetime import date, timedelta
from application.func import verify_input
from application.datefunc import get_currdate, verify_date

future = str(date.today() + timedelta(2))
toolong = "tralala"
for x in range(10000):
    toolong += "la"
wronginputs = ["23-24-62", "1995-11-25", 
               "2022-10-31", "Wrong input", 
               future, toolong, 
               "<h1>HTML Injection testing</h1>", 
               ]

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



