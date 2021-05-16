function generateCellId(index) {
    return "input_" + index;
}

function setup() {
    let grid = this.document.getElementById("sudoku-grid");

    let count = 0;
    for (let i = 0; i < 9; i++) {
        let row = this.document.createElement("tr");

        for (let j = 0; j < 9; j++) {
            let cell = this.document.createElement("td");
            let input = this.document.createElement("input");
            input.setAttribute("id", generateCellId(count++));
            input.setAttribute("type", "number");
            input.setAttribute("max", 9);
            input.setAttribute("min", 1);
            input.setAttribute("step", 1);
            cell.appendChild(input);
            row.appendChild(cell);
        }
        grid.appendChild(row);
    }

    let button = this.document.createElement("button");
    button.innerHTML = "Solve";
    button.className = "solve-button";
    let clearButton = this.document.createElement("button");
    clearButton.innerHTML = "Clear";
    clearButton.className = "clear-button";

    button.addEventListener("click", solve);
    clearButton.addEventListener("click", clear);

    this.document.getElementById("solver").appendChild(button);
    this.document.getElementById("solver").appendChild(clearButton);
}

function solve() {
    let xhttp = new XMLHttpRequest();
    let that = this;

    let sudokuData = {};
    let regex = new RegExp("^[0-9]{1}");

    for (let i = 0; i < 81; i++) {
        cellValue = document.getElementById(generateCellId(i)).value;
        if (cellValue && cellValue.match(regex)) {
            value = parseInt(cellValue.match(regex)[0]);
            if (value > 9 || value < 1) {
                alert("Each cell can only take values from 1 to 9");
                return;
            }
            sudokuData[i] = value;
        }
    }

    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            if (response.status == "success") {
                Object.keys(response.solution).forEach( function (key) {
                    document.getElementById(generateCellId(key)).value = response.solution[key];
                    document.getElementById(generateCellId(key)).setAttribute("disabled", "disabled");
                } )
            } else {
                alert("This sudoku solver is infeasible!!!");
            }
        }
    }
    xhttp.open("POST", "solve", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("key=".concat(JSON.stringify(sudokuData)));
}

function clear() {
    for (let i = 0; i < 81; i++) {
        document.getElementById(generateCellId(i)).value = "";
        document.getElementById(generateCellId(i)).removeAttribute("disabled");
    }
}

setup();