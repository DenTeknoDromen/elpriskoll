from flask import Flask, render_template, redirect
from markupsafe import escape

# py -m flask --app app run --debug

app = Flask(__name__)
price_class = ["SE1 = Luleå / Norra Sverige",
               "SE2 = Sundsvall / Norra Mellansverige",
               "SE3 = Stockholm / Södra Mellansverige", 
               "SE4 = Malmö / Södra Sverige"]


@app.route("/index")
def index():
    return render_template("form.html", price_class=price_class)

@app.route("/searchresults")
def searchresults():
    return "Hello World!"