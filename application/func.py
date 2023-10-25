from urllib import request
import pandas
import ssl
import json
import plotly.express as px
from datefunc import verify_date, get_pastdate

def get_api(date, pricegroup):
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{date[0:4]}/{date[5:]}_{pricegroup}.json"
    context = ssl._create_unverified_context()
    json_data = request.urlopen(url, context=context).read()
    data = json.loads(json_data)
    df = pandas.DataFrame(data)
    return df

def get_graph(date, pricegroup, columns=None):
    try:
        #df = pandas.DataFrame(data)

        # Dubbelkolla denna kod
        # if columns == None:
        #     html_df = df.to_html(classes="table p-5", justify="left", index=False)
        # else:
        #     html_df = df.to_html(columns=columns, classes="table p-5", justify="left", index=False)
        data = get_api(date,pricegroup)
        fig = px.line(data, x="time_start", y="SEK_per_kWh", title="Elpris per timme", template="plotly_dark")
        fig.update_traces(line={"width":10}) 
                          #line_color="#ff4500")
        
        # date = get_pastdate(date)
        # if verify_date(date) == True:
        #     data_2 = get_api(date, pricegroup)
        #     fig.add_trace(data_2)    #,  line={"width":7}, line_color="#6495ed")

        diagram = fig.to_html()    
        return diagram
    
    except Exception as e:
        return e





    
