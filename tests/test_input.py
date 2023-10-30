import pytest
from flask import g, session
import ssl
from urllib import request, response

context = ssl._create_unverified_context()

def test_input():
    assert request.urlopen("http://127.0.0.1:5000/index", context=context, timeout=10)