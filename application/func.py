from urllib import request
import pandas
import ssl
import json
import plotly.express as px
from application.datefunc import verify_date


def verify_input(date, pricegroup):
    if verify_date(date) == False:
        return False
    elif pricegroup == "No ":
        return False
    else:
        return True


def get_api(date, pricegroup):
    url = f"https://www.elprisetjustnu.se/api/v1/prices/{date[0:4]}/{date[5:]}_{pricegroup}.json"
    context = ssl._create_unverified_context()
    try:
        json_data = request.urlopen(url, context=context).read()
        data = json.loads(json_data)
        df = pandas.DataFrame(data)
        return df

    except Exception as e:
        return e


def get_graph(data, data_opt, lst_dates):
    try:     
        # Lägger till en column i data och anger namnet till plotlylistan
        if type(data_opt) != bool:
            data = data.assign(SEK_per_kWh_2=data_opt["SEK_per_kWh"])
            data = data.rename(columns= {"SEK_per_kWh_2":lst_dates[1]})

        data = data.rename(columns= {"SEK_per_kWh":lst_dates[0], "time_start":"Time of day"})

        fig = px.line(data, x="Time of day", y=lst_dates,
                      title="Elpris per timme", template="plotly_dark")
        fig.update_traces(mode="markers+lines", hovertemplate=None)
        fig.update_layout(hovermode="x")

        diagram = fig.to_html()
        return diagram

    except Exception as e:
        return e
