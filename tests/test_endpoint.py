import pytest
from urllib import request, response
import ssl

context = ssl._create_unverified_context()

def test_is_online_index():
    assert request.urlopen("http://127.0.0.1:5000/index", context=context, timeout=10)

def test_catch_404_error():
    with request.urlopen("http://127.0.0.1:5000/", context=context, timeout=10):
        html = str(response.read())
        assert "404" not in html

def test_catch_405_error():
    with request.urlopen("http://127.0.0.1:5000/api", context=context, timeout=10):
        html = str(response.read())
        assert "Method not allowed" not in html
