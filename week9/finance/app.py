import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?",
                          request.form.get("username"))

        # Ensure username exists and password is correct
        # check that password was correct ALSO
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # user is accesing the page
    if request.method == "GET":
        return render_template("quote.html")

    # user is asking for a stock price"
    search = request.form.get("symbol")
    stock = lookup(search)

    # stock does not exist
    if stock == None:
        return apology("Stock does not exist")

    # stock does exist
    stock_name = stock.get("name")
    stock_price = stock.get("price")
    stock_symbol = stock.get("symbol")
    return render_template("quoted.html", stock_name=stock_name, stock_price=stock_price, stock_symbol=stock_symbol)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # if the user is accesing the page
    if request.method == "GET":
        return render_template("register.html")

    # elif the user wants to register aka "POST"
    # Ensure username was submitted
    if not request.form.get("username"):
        return apology("must provide username", 400)

    # Ensure password was submitted
    elif not request.form.get("password"):
        return apology("must provide password", 400)

    elif not request.form.get("confirmation"):
        return apology("must provide password confirmation", 400)

    elif request.form.get("password") != request.form.get("confirmation"):
        return apology("passwords do not match", 400)

    # everithing has worked, therefore user has provided a password and a name.
    username = request.form.get("username")
    password = request.form.get("password")
    HashedPassword = generate_password_hash(password)

    # If the username is already taken
    data = db.execute(
        "SELECT COUNT(*) FROM users WHERE username = :username", username=username)
    for i in list(data[0].values()):
        if i > 0:
            return apology("username already taken, please try again", 400)
    # username hasn´t been taken
        else:
            # add new user into database
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?);", username, HashedPassword)
            # return to homepage
            session["user_id"] = username
            return redirect("/")

    return apology("please try again", 400)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    try:
        id = db.execute("SELECT id FROM users WHERE username= :user;",
                        user=session["user_id"])
        id = id[0]
        id = id.get("id")
    except:
        id = db.execute("SELECT id FROM users WHERE id= :user;",
                        user=session["user_id"])
        id = id[0]
        id = id.get("id")

    """Buy shares of stock"""
    # user is accesing buy page
    if request.method == "GET":
        try:
            # check for current cash
            cash = db.execute(
                "SELECT cash FROM users WHERE id = :user;", user=id)
            cash = cash[0].get("cash")
            return render_template("buy.html", cash=cash)
        except:
            cash = 10000
            return render_template("buy.html", cash=cash)

    # Ensure username was submitted
    if not request.form.get("symbol"):
        return apology("must provide a stock", 400)
    elif request.form.get("symbol").isalpha() != True:
        return apology("must provide a letter, not numbers", 400)

    # check proper usage
    elif request.form.get("shares").isnumeric() != True:
        return apology("must provide a numeric ammount of shares", 400)

     # user is trying to buy shares of stock
    Shares = float(request.form.get("shares"))
    # Ensure password was submitted
    if Shares <= 0:
        return apology("must buy at least 1 share of stock", 400)

    # user is asking for a stock price
    Symbol = request.form.get("symbol")
    Symbol = Symbol.upper()
    Symbol = lookup(Symbol)

    # stock does not exist
    if Symbol == None:
        return apology("Stock does not exist")

    symbol = Symbol.get("symbol")

    # check stock name
    name = Symbol.get("name")

    # check stock price
    price = Symbol.get("price")
    price = float(price)

    # user cash
    try:
        UserCash = db.execute(
            "SELECT cash FROM users WHERE id = :user ;", user=id)
        UserCash = UserCash[0].get("cash")
    except:
        UserCash = 10000

    # total ammount
    TotalValue = Shares * price

    # check if user can afford the ammount of shares asked
    if TotalValue > UserCash:
        return apology("YOUR ARE BROKE haha, you can´t afford it, just yet....", 400)

    # add him into data base
    # fisrt time
    NewUser = db.execute(
        "SELECT COUNT(*) FROM stocks WHERE person_id = :person ;", person=id)
    NewUser = NewUser[0].get("COUNT(*)")
    if NewUser == 0:
        db.execute("INSERT INTO stocks ( person_id, symbol, name, price, shares, total, shares_owned, total_value ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?);",
                   id, symbol, name,  price, Shares, TotalValue, Shares, TotalValue)
    else:
        # calculate new total value
        try:
            PreviousTotal = db.execute(
                "SELECT total_value FROM stocks WHERE person_id= ? AND symbol= ? AND total_value> 0;", id, symbol)
            PreviousTotal = PreviousTotal[0].get("total_value")
        except:
            PreviousTotal = 0
        NewTotalValue = PreviousTotal + TotalValue

        # calculate new shares owned
        try:
            PreviousShares = db.execute(
                "SELECT shares_owned FROM stocks WHERE person_id= ? AND symbol= ? AND total_value> 0;", id, symbol)
            PreviousShares = PreviousShares[0].get("shares_owned")
        except:
            PreviousShares = 0
        NewSharesOwned = Shares + PreviousShares

        db.execute("INSERT INTO stocks (person_id, symbol, name, price, shares, total, shares_owned, total_value ) VALUES ( ?, ?, ?, ?, ?, ?,? , ?);",
                   id, symbol, name,  price, Shares, TotalValue, NewSharesOwned, NewTotalValue)

        # set every other total value to 0
        db.execute("UPDATE stocks SET total_value =0 WHERE person_id=? AND symbol=? AND total_value < ?;",
                   id, symbol, NewTotalValue)

        # set every other shares owned to 0 but the latest one
        db.execute("UPDATE stocks SET shares_owned =0 WHERE person_id=? AND symbol=? AND shares_owned < ?;",
                   id, symbol, NewSharesOwned)

    # change users cash
    UpdatedMoney = UserCash-TotalValue
    db.execute("UPDATE users SET cash= ? WHERE id= ?; ",
               UpdatedMoney, id)
    # total money both cash and stocks
    TotalMoney = db.execute(
        "SELECT SUM(total_value) AS score FROM stocks WHERE person_id= :id AND total_value > 0;", id=id)
    TotalMoney = TotalMoney[0].get("score")

    TotalMoney = round(UpdatedMoney+TotalMoney)

    return render_template("bought.html", symbol=symbol, name=name, Shares=Shares, price=price, TotalValue=TotalValue, UpdatedMoney=UpdatedMoney, TotalMoney=TotalMoney)


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # user id
    try:
        id = db.execute(
            "SELECT id FROM users WHERE username= :username;", username=session["user_id"])
        id = id[0].get("id")
    except:
        id = db.execute("SELECT id FROM users WHERE id= :username;",
                        username=session["user_id"])
        id = id[0].get("id")
    if request.method == "GET":
        # check for stock ownership
        try:
            SellCheck = db.execute(
                "SELECT COUNT(*) FROM stocks WHERE shares_owned >0;")
            SellCheck = SellCheck[0].get("COUNT(*)")
        except:
            SellCheck = 0
        if SellCheck == 0:
            return apology("You must own at least  share in order to sell")

        # gather user stocks
        stocks = db.execute(
            "SELECT symbol FROM stocks WHERE shares_owned > 0 AND person_id= :id;", id=id)
        return render_template("sell.html", stocks=stocks)

    # else (method POST)
    # check proper usage
    SymbolSold = request.form.get("symbol")
    sold = request.form.get("shares")
    if SymbolSold == "Symbol":
        return apology("must provide a stock")
    if not sold:
        return apology("must provide a number")
    sold = int(sold)
    if sold < 0:
        return apology("must provide a numer higher than 0")
    # check how
    #  stock does he have
    StockAvailable = db.execute(
        "SELECT shares_owned FROM stocks WHERE symbol= ? AND person_id= ? AND shares_owned > 0; ", SymbolSold, id)

    StockAvailable = StockAvailable[0].get("shares_owned")

    if sold > StockAvailable:
        return apology("You dont own that many shares")

    # gather some stock info
    name = db.execute(
        "SELECT name FROM stocks WHERE symbol= ? AND person_id = ? LIMIT 1;", SymbolSold, id)
    name = name[0].get("name")

    price = db.execute(
        "SELECT price FROM stocks WHERE symbol= ? AND person_id = ? LIMIT 1;", SymbolSold, id)
    price = price[0].get("price")

    if sold == StockAvailable:
        db.execute("INSERT INTO stocks (person_id, symbol, name, price, shares, total, shares_owned, total_value ) VALUES ( ?, ?, ?, ?, ?, ?,? , ?);",
                   id, SymbolSold, name,  price, (-(sold)), price*sold, 0, 0)
        # set every value to 0 (you dont own any now)
        db.execute(
            "UPDATE stocks SET total_value =0 WHERE person_id=? AND symbol=?;", id, SymbolSold)

        # set every share owned to 0 (you also dont own any)
        db.execute(
            "UPDATE stocks SET shares_owned =0 WHERE person_id=? AND symbol=? ;", id, SymbolSold)
    else:
        # get previous shares
        OldShares = db.execute(
            "SELECT shares_owned FROM stocks WHERE person_id= ? AND symbol= ? AND total_value> 0;", id, SymbolSold)
        OldShares = OldShares[0].get("shares_owned")

        # get previous total
        OldTotal = db.execute(
            "SELECT total_value FROM stocks WHERE person_id= ? AND symbol= ? AND total_value> 0;", id, SymbolSold)
        OldTotal = OldTotal[0].get("total_value")

        db.execute("INSERT INTO stocks (person_id, symbol, name, price, shares, total, shares_owned, total_value ) VALUES ( ?, ?, ?, ?, ?, ?,? , ?);",
                   id, SymbolSold, name,  price, (-(sold)), price*sold, OldShares-sold, OldTotal-(price*sold))
        # set every other share owned to 0
        db.execute(
            "UPDATE stocks SET shares_owned =0 WHERE person_id=? AND symbol=? AND shares_owned!= ?;", id, SymbolSold, (OldShares-sold))
        # set every other total owned to 0
        db.execute(
            "UPDATE stocks SET total_value =0 WHERE person_id=? AND symbol=? AND total_value!= ?;", id, SymbolSold, (OldTotal-(price*sold)))

    # update cash
    UserMoney = db.execute(
        "SELECT cash FROM users WHERE id = ?;", id)
    UserMoney = UserMoney[0].get("cash")

    # total money after selling
    NewMoney = UserMoney+(price*sold)

    db.execute("UPDATE users SET cash= ? WHERE id = ?;", NewMoney, id)

    # total cash (stocks and money)

    return render_template("sold.html", SymbolSold=SymbolSold, name=name, sold=sold, price=price, total=(sold*price), NewMoney=NewMoney)


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    """Show portfolio of stocks"""

    # user is accesing the homepage
    if request.method == "GET":
        try:
            id = db.execute(
                "SELECT id FROM users WHERE username= :username;", username=session["user_id"])
            id = id[0].get("id")
        except:
            id = db.execute(
                "SELECT id FROM users WHERE id= :username;", username=session["user_id"])
            id = id[0].get("id")

        # cash
        cash = db.execute(
            "SELECT cash FROM users WHERE id = ?;", id)
        cash = cash[0].get("cash")

        # TOTAL
        try:
            TotalMoney = db.execute(
                "SELECT SUM(total_value) AS sum FROM stocks WHERE  person_id= :id AND total_value>0;", id=id)
            TotalMoney[0].get("sum")
            TotalMoney = round(cash+TotalMoney)
        except:
            TotalMoney = 10000
        # Get user data
        database = db.execute(
            "SELECT * FROM stocks WHERE person_id= :id AND shares_owned>0;", id=id)

        return render_template("index.html", database=database, cash=cash, TotalMoney=TotalMoney)


@app.route("/history")
@login_required
def history():
    if request.method == "GET":
        try:
            id = db.execute(
                "SELECT id FROM users WHERE username= :username;", username=session["user_id"])
            id = id[0].get("id")
        except:
            id = db.execute(
                "SELECT id FROM users WHERE id= :username;", username=session["user_id"])
            id = id[0].get("id")
        # gather database
        historyDB = db.execute("SELECT * FROM stocks WHERE person_id = ?;", id)

        return render_template("history.html", historyDB=historyDB)

    return apology("TODO")
