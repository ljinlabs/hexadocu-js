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
    console.log(puzzle);
    return true;
}

function parseId(id) {
    
}

function colorBorders() {
    const allCells = document.querySelectorAll(".cell");
    allCells.forEach(elem => {
        let cellId = elem.getAttribute('id');
    })
}

function main() {
    buildPuzzle();
}

main();