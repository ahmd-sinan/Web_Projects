from flask import Flask, render_template, redirect, request

app = Flask(__name__)

ORDERS = {}

ITEMS = [
    "Pizza",
    "Burger",
    "Sandwich"
]

DRINKS = [
    "Coffee",
    "Tea",
    "Pepsi"
]
@app.route("/")
def index():
    return render_template("index.html", Items=ITEMS, Drinks=DRINKS)

@app.route("/place_order", methods=["POST"])
def place_order():
    name = request.form.get("name")
    item = request.form.get("item")
    drink = request.form.get("drink")

    # Validate customer name
    if not name:
        return render_template("error.html", message="Missing name")
    
    # Validate item and drink
    if not item or not drink:
        return render_template("error.html", message="Missing item or drink")
    
    # Validate item and drink selection
    if item not in ITEMS or drink not in DRINKS:
        return render_template("error.html", message="Invalid item or drink")

    ORDERS[name] = {"food": item, "drink": drink}
    return redirect("/orders")

@app.route("/orders")
def orders():
    return render_template("orders.html", orders=ORDERS)