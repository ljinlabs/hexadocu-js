const puzzle = document.getElementById("puzzle");

//build puzzle from js
function buildPuzzle() {
    for (let i = 0; i < 12; i++) {
        const tr = document.createElement("tr");
        for (let j = 0; j < 12; j++) {
            const td = document.createElement("td");
            td.setAttribute("id", `row-${i}-col-${j}`)
            td.setAttribute('class', 'cell');
            tr.appendChild(td);
        }
        tr.setAttribute('class','row');
        puzzle.appendChild(tr);
    }
    return true;
}

function parseId(id) {
    const idSplit = id.split("-");
    return [parseInt(idSplit[1]), parseInt(idSplit[3])];
}

function colorBorders() {
    const allCells = document.querySelectorAll(".cell");
    allCells.forEach(elem => {
        const cellId = elem.getAttribute('id');
        const splits = parseId(cellId);
        const i = splits[0];
        const j = splits[1];
        
        if (i % 4 == 0 && i != 0) {
            elem.classList.add("top-border");
        }
        if (j % 4 == 0 && j != 0) {
            elem.classList.add("left-border");
        }
    });
}

function main() {
    buildPuzzle();
    colorBorders();
}

main();