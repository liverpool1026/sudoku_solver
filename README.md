# Sudoku Solver
A flask app with Sudoku Grid Interface that calls a solver that solves Sudoku

![image](https://user-images.githubusercontent.com/29122286/118388219-77565c80-b666-11eb-9885-73f3ecc15737.png)

# How to run

## Pull pre-built docker container

Pull Docker Container
```
docker pull hawkvine/sudoku-solver:version (i.e. docker pull hawkvine/sudoku-solver:1.0.0)
```

Run Docker Container
```
docker run --net="host" hawkvine/sudoku-solver:version
```

Check out https://hub.docker.com/r/hawkvine/sudoku-solver/tags?page=1&ordering=last_updated for available versions. (Latest Stable: 1.0.0)

## Run the code directly

Install
```
git clone https://github.com/liverpool1026/sudoku_solver
cd sudoku_solver
pip install -e .  (Requires python3.6)
```

Run
```
sudoku
```

### Support or Contact

