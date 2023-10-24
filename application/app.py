from flask import Flask, render_template, redirect, request
from markupsafe import escape
from datefunc import verify_date, get_currdate
from func import get_apidf

# py -m flask --app app run --debug

app = Flask(__name__)
price_class = ["SE1 = Luleå / Norra Sverige", 
                "SE2 = Sundsvall / Norra Mellansverige", 
                "SE3 = Stockholm / Södra Mellansverige", 
                "SE4 = Malmö / Södra Sverige "]


@app.route("/index")
def index():
    curr_date = get_currdate()
    return render_template("form.html", price_class=price_class, curr_date=curr_date)

@app.route("/api", methods=["GET", "POST"])
def _post_api():

    date = request.form["date"]
    pricegroup = request.form["priceclass"]
    print(pricegroup) # test

    if verify_date(date) == False:
        # Error message  och felhantering här
        print("Det här ska vara en error!")
    
    testurl = "https://www.elprisetjustnu.se/api/v1/prices/2023/10-24_SE3.json"
    api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{date[0:4]}/{date[5:]}_{pricegroup}.json"
    data = get_apidf(api_url)

    return render_template("print.html", data=data)




@app.route("/searchresults")
def searchresults():
    return "Hello World!"
