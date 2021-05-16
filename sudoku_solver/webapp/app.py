import os
import json

from flask import Flask, render_template, request

from sudoku_solver.tasks.solver import solve

dir_path = os.path.dirname(os.path.realpath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(dir_path, "..", "templates"),
    static_folder=os.path.join(dir_path, "..", "static"),
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve_api():
    return solve(json.loads(request.values.get("key", "{}")))
