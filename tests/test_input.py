import pytest
from flask import g, session
import ssl
# from urllib import request, response
import sys
import os
parent = os.path.abspath("")
sys.path.append(parent)
from application.app import create_app

#context = ssl._create_unverified_context()

# #def test_input():
# @pytest.fixture
# def client():
#     app = test_client

client = create_app()
response = client.post("index/", data={"date": "2023-11-01", 
                                       "priceclass": "SE1"})

assert response.status_code == 200