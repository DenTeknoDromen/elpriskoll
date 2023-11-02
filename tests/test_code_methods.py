import pytest
from datetime import date, timedelta
from application.func import verify_input, get_api
from application.datefunc import get_currdate, verify_date
import sys
import os
parent = os.path.abspath("")
sys.path.append(parent)
from application.func import*

# Skapar datum för att testning
future = date.today() + timedelta(2)
past = date(2022,11,1)

# Skapar en lång sträng för testning
toolong = "tralala"
for x in range(10000):
    toolong += "la"

# Lista med inputs som INTE ska funka
wronginputs = ["23-24-62", "1995-11-25", 
               "2022-10-31", "Wrong input", 
               "-2023-10-31", "2023-31-10", 
               "2023-10-31T14:30:43", "23-10-31", 
               str(future), toolong, 
               "<h1>HTML Injection testing</h1>", 
               "<script></script>"
               ]

# Lista med med datum som ska funka
correctinputs = []
while past != future:
    print(str(past))
    correctinputs.append(str(past))
    past += timedelta(1)

#Lista med alla korrekta prisklasser
pricegroups = ["SE1", "SE2", "SE3", "SE4"]

def test_verify_date():
    for input in wronginputs:
        returnvalue = verify_date(input)
        if returnvalue is True:
            break
    assert returnvalue == False

def test_verify_date_positive():
    for input in correctinputs:
        returnvalue = verify_date(input)
        if returnvalue is False:
            break
    assert returnvalue == True

def test_verify_input():
    pricegroup = "No "
    for x in wronginputs:
        returnvalue = verify_input(x, pricegroup)
        if returnvalue is True:
            break
    assert returnvalue == False

    pricegroup = "SE1"
    for x in wronginputs:
        returnvalue = verify_input(x, pricegroup)
        if returnvalue is True:
            break
    assert returnvalue == False

def test_verify_input_positive():
    for x in pricegroups:
        for y in correctinputs:
            returnvalue = verify_input(y, x)
            if returnvalue is False:
                break
        assert returnvalue == True

def test_get_api():
    for x in pricegroups:
        for y in correctinputs:
            returnvalue = get_api(y, x)
            if type(returnvalue) != "pandas.core.frame.DataFrame":
                break
        assert type(returnvalue) != "pandas.core.frame.DataFrame"
    

