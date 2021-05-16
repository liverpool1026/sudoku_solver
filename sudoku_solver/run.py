import click
import pkg_resources

from sudoku_solver.webapp.app import app


@click.command()
def run():
    sudoku_solver = click.style("sudoku_solver", fg="cyan", bold=True)
    version = pkg_resources.get_distribution("sudoku_solver").version
    click.echo(sudoku_solver + " " + version)
    click.echo("Simple Sudoku Solver by using binary solve.")
    app.config[
        "SECRET_KEY"
    ] = "sdf123gk12awefhu21InFPAw4dNwOa16a4IGRC8GOGjZcg95z5SRQsgBQp412TLLCr59Y"

    app.config["TEMPLATES_AUTO_RELOAD"] = True

    app.run(host="127.0.0.1", port=8000)


def main():
    run()


if __name__ == "__main__":
    main()
