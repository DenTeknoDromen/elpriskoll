import pytest
from flask import g, session
import ssl
from urllib import request, response

#context = ssl._create_unverified_context()

#def test_input():
@pytest.fixture
def client():
    app = test_client