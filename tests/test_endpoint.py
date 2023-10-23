import pytest
import urllib.request
import ssl

context = ssl._create_unverified_context()

def test_is_online_index():
    assert urllib.request.urlopen("http://127.0.0.1:5000/index", context=context, timeout=10)

def test_is_online_searchresult():
    assert urllib.request.urlopen("http://127.0.0.1:5000/searchresults", context=context, timeout=10)
