import os
from flask import Flask, render_template

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__, template_folder=os.path.join(dir_path, "..", "templates"), static_folder=os.path.join(dir_path, "..", "static"))


@app.route("/")
def index():
    return render_template(
        "index.html"
    )


@app.route("/solve", methods=["POST"])
def solve():
    pass
