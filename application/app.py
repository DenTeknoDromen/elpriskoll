from flask import Flask, render_template, redirect, request
from markupsafe import escape
from datefunc import verify_date, get_currdate
from func import get_graph
import plotly.express as px

# py -m flask --app app run --debug

# Att göra:
# plotly på apin, snyggare presentation av data
# Ska kunna installeras också
# Snygga till html
# fler testcase


app = Flask(__name__)
price_class = ["SE1: Luleå / Norra Sverige", 
                "SE2: Sundsvall / Norra Mellansverige", 
                "SE3: Stockholm / Södra Mellansverige", 
                "SE4: Malmö / Södra Sverige "]

@app.route("/index")
def index():
    curr_date = f"tex: {get_currdate()}"
    return render_template("form.html", price_class=price_class, curr_date=curr_date)

@app.route("/api", methods=["POST"])
def post_api():

    date = request.form["date"]
    pricegroup = request.form["priceclass"]

    if verify_date(date) == False:
        return redirect("/index")
    else:
        data = get_graph(date, pricegroup)

    # Dubbelkoll ifall apin har returneat data
    # Är tex inte alltid säkert att api uppdaterat inför morgondagen
    if type(data) == ValueError:
        return redirect("/index")
    else:
        return render_template("print.html", data=data)

# Hanterar error 404 genom redirect
@app.errorhandler(404)
def page_notfound(error):
    return redirect("/index")

# Hanterar error 405 genom redirect
@app.errorhandler(405)
def api_get(error):
    return redirect("/index")
