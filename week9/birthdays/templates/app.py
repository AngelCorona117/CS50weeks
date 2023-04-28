import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database
        Name = request.form.get("NAME")
        Month = request.form.get("MONTH")
        Day = request.form.get("DAY")
        # CHECK FOR CORRECT USAGE
        # for day form
        if Name.isalpha() == True:
            Name = Name.capitalize()
        else:
            return redirect("/")
        # for month and day form
        try:
            Day = int(Day)
            Month = int(Month)
            if ((Month > 0 and Month <= 12) and (Day > 0 and Day <= 31)) == False:
                return redirect("/")
        except:
            return redirect("/")

        # TODO: Display the entries in the database on index.html
        db.execute(
            "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?);", Name, Month, Day)

    rows = db.execute("SELECT * FROM birthdays;")
    return render_template("index.html", rows=rows)
