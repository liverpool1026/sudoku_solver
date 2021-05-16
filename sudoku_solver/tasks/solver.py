import pulp

from collections import defaultdict

from typing import Dict, Tuple, Union


class Solver(object):
    def __init__(self) -> None:
        self._problem = pulp.LpProblem("Sudoku")
        self._variables = defaultdict(lambda: defaultdict(lambda: list()))
        self._solution = defaultdict(lambda: dict())
        self.setup_problem()

    def setup_problem(self) -> None:
        self.create_variables()
        self.create_constraints()

    def create_variables(self) -> None:
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    self._variables[i][j].append(pulp.LpVariable(f"({i}, {j}): is {k+1}", cat=pulp.LpBinary))

    def create_constraints(self) -> None:
        for i in range(9):
            for j in range(9):
                self._problem += pulp.lpSum(self._variables[i][j]) == 1, f"Only 1 value per cell: ({i}, {j})"
                self._problem += pulp.lpSum([self._variables[i][k][j] for k in range(9)]) == 1, f"Only 1 {j+1} for column {i})"
                self._problem += pulp.lpSum([self._variables[k][i][j] for k in range(9)]) == 1, f"Only 1 {j+1} for row {i})"

        for i in range(3):
            for j in range(3):
                for k in range(9):
                    self._problem += pulp.lpSum([self._variables[i*3+l][j*3+m][k] for l in range(3) for m in range(3)]) == 1, f"Only 1 {k+1} for box ({i}, {j})"

    def lock_in_value(self, x: int, y: int, value: int) -> None:
        for i in range(9):
            self._variables[x][y][i].setInitialValue(int(i+1 == value))
            self._variables[x][y][i].fixValue()

    def read_solution(self) -> None:
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if pulp.value(self._variables[i][j][k]) == 1:
                        self._solution[i][j] = k+1

    def print_solution(self) -> None:
        for i in range(9):
            for j in range(9):
                print(self._solution[i][j], end=" ")
            print()

    def solve(self) -> None:
        self._problem.solve()
        self.read_solution()

    def get_solution(self) -> Dict[int, int]:
        solution = dict()
        count = 0
        for i in range(9):
            for j in range(9):
                solution[count] = self._solution[i][j]
                count += 1
        return solution


def convert_index_to_tuple(index_: int) -> Tuple[int, int]:
    return index_ % 9, index_ // 9


def solve(problem: Dict[int, int]) -> Dict[Union[int, str], Union[int, str]]:
    solver = Solver()

    for index_, value in problem.items():
        solver.lock_in_value(*convert_index_to_tuple(int(index_)), value)

    solver.solve()
    solution = solver.get_solution()
    if solution:
        return {
            "status": "success",
            "solution": solution
        }
    return {
        "status": "failed"
    }

