from flask import render_template, request
from . import app
from app.nvidia_api import query_nvidia 


@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["prompt"]
        response = query_nvidia(user_input)
    return render_template("index.html", response=response)