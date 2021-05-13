import pulp

from collections import defaultdict


class Solver(object):
    def __init__(self):
        self._problem = pulp.LpProblem("Sudoku")
        self._variables = defaultdict(lambda: defaultdict(lambda: list()))
        self._solution = defaultdict(lambda: dict())
        self.setup_problem()

    def setup_problem(self):
        self.create_variables()
        self.create_constraints()

    def create_variables(self):
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    self._variables[i][j].append(pulp.LpVariable(f"({i}, {j}): is {k+1}", cat=pulp.LpBinary))

    def create_constraints(self):
        for i in range(9):
            for j in range(9):
                self._problem += pulp.lpSum(self._variables[i][j]) == 1, f"Only 1 value per cell: ({i}, {j})"
                self._problem += pulp.lpSum([self._variables[i][k][j] for k in range(9)]) == 1, f"Only 1 {j+1} for column {i})"
                self._problem += pulp.lpSum([self._variables[k][i][j] for k in range(9)]) == 1, f"Only 1 {j+1} for row {i})"

        for i in range(3):
            for j in range(3):
                for k in range(9):
                    self._problem += pulp.lpSum([self._variables[i*3+l][j*3+m][k] for l in range(3) for m in range(3)]) == 1, f"Only 1 {k+1} for box ({i}, {j})"

    def lock_in_value(self, x: int, y: int, value: int):
        for i in range(9):
            self._variables[x][y][i].setInitialValue(int(i+1 == value))
            self._variables[x][y][i].fixValue()

    def read_solution(self):
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if pulp.value(self._variables[i][j][k]) == 1:
                        self._solution[i][j] = k+1

    def print_solution(self):
        for i in range(9):
            for j in range(9):
                print(self._solution[i][j], end=" ")
            print()

    def solve(self):
        self._problem.solve()
        self.read_solution()

    def get_solution(self):
        return "".join([str(self._solution[i][j]) for i in range(9) for j in range(9)])


def solve(problem):
    solver = Solver()

    for (x, y), value in problem.items():
        solver.lock_in_value(x, y, value)

    solver.solve()
    solver.print_solution()

