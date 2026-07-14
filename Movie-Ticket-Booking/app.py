from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/booking", methods=["POST"])
def booking():
    if not request.form.get("name") or not request.form.get("movie"):
        return render_template("failure.html")
    return render_template("success.html")