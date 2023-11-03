import pytest
from application.func import verify_input, get_api
from application.datefunc import get_currdate, verify_date
from tests.inputs import Inputs

i = Inputs()
def test_verify_date():
    for input in i.inputs["wronginputs"]:
        returnvalue = verify_date(input)
        if returnvalue is True:
            break
    assert returnvalue == False

def test_verify_date_positive():
    for input in i.inputs["correctinputs"]:
        returnvalue = verify_date(input)
        if returnvalue is False:
            break
    assert returnvalue == True

def test_verify_input():
    pricegroup = "No "
    for x in i.inputs["wronginputs"]:
        returnvalue = verify_input(x, pricegroup)
        if returnvalue is True:
            break
    assert returnvalue == False

    pricegroup = "SE1"
    for x in i.inputs["wronginputs"]:
        returnvalue = verify_input(x, pricegroup)
        if returnvalue is True:
            break
    assert returnvalue == False

def test_verify_input_positive():
    for x in i.inputs["pricegroups"]:
        for y in i.inputs["correctinputs"]:
            returnvalue = verify_input(y, x)
            if returnvalue is False:
                break
        assert returnvalue == True

def test_get_api():
    for x in i.inputs["pricegroups"]:
        for y in i.inputs["correctinputs"]:
            returnvalue = get_api(y, x)
            if type(returnvalue) != "pandas.core.frame.DataFrame":
                break
        assert type(returnvalue) != "pandas.core.frame.DataFrame"
    

