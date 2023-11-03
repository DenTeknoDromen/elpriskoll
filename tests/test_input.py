import pytest
from application.app import app
from tests.inputs import Inputs

i = Inputs()

def test_input():
    app.testing = True
    client = app.test_client()
    with client as c:  
        response = c.post("/api", data={"date": i.inputs["correctinputs"], 
                                        "priceclass": i.inputs["pricegroups"], 
                                        "date_opt": "",
                                        "pricegroup_opt": ""})
        assert response.status_code == 200

def test_input_negative():
    app.testing = True
    client = app.test_client()
    with client as c:  
        response = c.post("/api", data={"date": i.inputs["wronginputs"], 
                                        "priceclass": i.inputs["pricegroups_2"], 
                                        "date_opt": "",
                                        "pricegroup_opt": ""})
        assert response.status_code == 302