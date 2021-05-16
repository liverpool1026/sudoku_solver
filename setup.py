from setuptools import setup

requires = [
    "pulp",
    "flask",
]

setup(
    name="sudoku-tasks",
    version="0.0.0",
    description="Sudoku GUI Interface + Solver",
    author="Hawkvine",
    author_email="liverpool1026.bne@gmail.com",
    url="https://kevinhwa.com",
    packages="sudoku_solver",
    include_package_data=True,
    install_requires=requires,
)
