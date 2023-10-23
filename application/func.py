from urllib import request
import ssl
import json


def get_priceclass(url):
    context = ssl.create_default_context()
    json_data = request.urlopen(url, context=context).read()
    data = json.loads(json_data)
    return data


    
