import pytest
from urllib import request, response
import ssl

context = ssl._create_unverified_context()

# Testar om index endpoint är öppen
def test_is_online_index():
    assert request.urlopen("http://127.0.0.1:5000/index", context=context, timeout=10)

# Testar om api endpoint är öppen
def test_is_online_api():
    assert request.urlopen("http://127.0.0.1:5000/api", context=context, timeout=10)

# Testar att apin funkar
def test_is_online_external_api():
    assert request.urlopen("https://www.elprisetjustnu.se/api/v1/prices/2022/11-25_SE3.json", context=context, timeout=10)

#Testar olika felaktiga endpoints
def test_wrong_url():
    with request.urlopen("http://127.0.0.1:5000/auth/", context=context, timeout=10) as response:
        html = str(response.read())
        assert "Elpriskollen" in html    
    with request.urlopen("http://127.0.0.1:5000/projects/", context=context, timeout=10) as response:
        html = str(response.read())
        assert "Elpriskollen" in html            

def test_catch_404_error():
    with request.urlopen("http://127.0.0.1:5000/noneexistantpath", context=context, timeout=10) as response:
        html = str(response.read())
        assert "404" not in html

def test_catch_405_error():
    with request.urlopen("http://127.0.0.1:5000/api", context=context, timeout=10) as response:
        html = str(response.read())
        assert "Method not allowed" not in html
