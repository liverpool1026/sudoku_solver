from sudoku_solver.webapp.app import app


app.config[
    "SECRET_KEY"
] = "sdf123gk12awefhu21InFPAw4dNwOa16a4IGRC8GOGjZcg95z5SRQsgBQp412TLLCr59Y"

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.run(host="127.0.0.1", port=8000)
