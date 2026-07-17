from flask import Flask, render_template, redirect, request

app = Flask(__name__)

ORDERS = {}

ITEMS = [
    "Pizza",
    "Burger",
    "Sandwich"
]

@app.route("/")
def index():
    return render_template("index.html", Items=ITEMS)

@app.route("/place_order", methods=["POST"])
def place_order():
    name = request.form.get("name")
    item = request.form.get("item")

    # Validate customer name
    if not name:
        return render_template("error.html", message="Missing name")
    
    # Validate item
    if not item:
        return render_template("error.html", message="Missing item")
    
    # Validate item selection
    if item not in ITEMS:
        return render_template("error.html", message="Invalid item")
    
    ORDERS[name] = item
    return redirect("/orders")

@app.route("/orders")
def orders():
    return render_template("orders.html", orders=ORDERS)