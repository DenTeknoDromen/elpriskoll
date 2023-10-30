from flask import Flask, render_template, redirect, request
from markupsafe import escape
from application.datefunc import get_currdate
from func import get_graph, get_api, verify_input
import plotly.express as px

# py -m flask --app app run --debug

# Att göra:
# fler testcase


app = Flask(__name__)
price_class = ["No input", 
               "SE1: Luleå / Norra Sverige", 
                "SE2: Sundsvall / Norra Mellansverige", 
                "SE3: Stockholm / Södra Mellansverige", 
                "SE4: Malmö / Södra Sverige "]

@app.route("/index")
def index():
    curr_date = f"tex: {get_currdate()}"
    return render_template("form.html", price_class=price_class, curr_date=curr_date)

@app.route("/api", methods=["POST"])
def post_api():

    # Sparar input för att användas i grafen senare
    lst_dates = []

    date = request.form["date"]
    pricegroup = request.form["priceclass"]

    date_opt = request.form["date_opt"]
    pricegroup_opt = request.form["pricegroup_opt"]

    # Verifierar input för huvudformen
    if verify_input(date, pricegroup) == False:
        return redirect("/index")
    else:
        data = get_api(date, pricegroup)
        lst_dates.append(f"SEK/kWh den {date}, Område: {pricegroup}")

    # Verifierar inputen från opt formen, inget händer om inputen skulle vara invalid
    if verify_input(date_opt, pricegroup_opt) != False:
        data_opt = get_api(date_opt, pricegroup_opt)
        lst_dates.append(f"SEK/kWh den {date_opt}, Område: {pricegroup_opt}")
    else:
        data_opt = False

    diagram = get_graph(data, data_opt, lst_dates)


    # Dubbelkoll ifall apin har returneat data
    # Är tex inte alltid säkert att api uppdaterat inför morgondagen
    if type(diagram) == ValueError:
        return redirect("/index")
    else:
        return render_template("print.html", data=diagram)

# Hanterar error 404 genom redirect
@app.errorhandler(404)
def page_notfound(error):
    return redirect("/index")

# Hanterar error 405 genom redirect
@app.errorhandler(405)
def api_get(error):
    return redirect("/index")
