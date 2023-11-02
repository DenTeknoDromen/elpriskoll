from urllib import request
import pandas
import ssl
import json
import plotly.express as px
from datetime import date


#from datefunc import verify_date, get_pastdate

# pandas.options.plotting.backend = "plotly"


# dateA = str(date.today())
# dateB = date(2023, 10, 25)

# def get_api(get_date, pricegroup):
#     url = f"https://www.elprisetjustnu.se/api/v1/prices/{get_date[0:4]}/{get_date[5:]}_{pricegroup}.json"
    
#     context = ssl._create_unverified_context()
#     try:
#         json_data = request.urlopen(url, context=context).read()
#         data = json.loads(json_data)
#         return data
    
#     except Exception as e:
#         return e

# #print(get_api(dateA, "SE1"))
# data = get_api(dateA, "SE1")
# data2 = get_api(dateA, "SE4")
# df = pandas.DataFrame(data)
# gap = px.data.gapminder().to_dict()
# #df = pandas.DataFrame(data, columns=['SEK_per_kWh', 'time_start'])
# # test = [x for x in range(24)]
# # df['SEK_per_kWh2'] = test
# #fig = df.plot()
# #   fig.add_line()
# def get_fig():
#     return gap    #df.to_html()


# #print(df)

dict_test = {1:"Hello", 2: "World"}
df = pandas.DataFrame(dict_test, columns={1, 2})
print(df)
