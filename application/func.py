from urllib import request
import pandas
import ssl
import json

def get_apidf(url, columns=None):
    context = ssl._create_unverified_context()

    try:
        json_data = request.urlopen(url, context=context).read()
        data = json.loads(json_data)
        df = pandas.DataFrame(data)
        if columns == None:
            html_df = df.to_html(classes="table p-5", justify="left")
        else:
            html_df = df.to_html(columns=columns, classes="table p-5", justify="left")
        
        return html_df
    
    except Exception as e:
        return e





    
