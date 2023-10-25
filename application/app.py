from flask import Flask, render_template, redirect, request
from markupsafe import escape
from datefunc import verify_date, get_currdate
from func import get_graph
import plotly.express as px

# py -m flask --app app run --debug

# Att göra:
# plotly på apin, snyggare presentation av data
# Fixa errormedelande vid ogiltig input
# Fixa placeholder
# Fixa errorhandering (404, 405)
# Ska kunna installeras också
# Snygga till html
# en till endpoint?
# Gör en favicon


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
def post_api():

    date = request.form["date"]
    pricegroup = request.form["priceclass"]

    if verify_date(date) == False:
        # Error message  och felhantering här
        print("Det här ska vara en error!")
    
    data = get_graph(date, pricegroup)
    return render_template("print.html", data=data)

@app.route("/searchresults")
def searchresults():
    return "Hello World!"
