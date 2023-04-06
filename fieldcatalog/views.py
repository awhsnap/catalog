from fieldcatalog import app
from flask import render_template, request, jsonify


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")