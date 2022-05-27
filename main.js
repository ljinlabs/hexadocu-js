const puzzle = document.getElementById("puzzle");
const dimension = 16;

//build puzzle from js
function buildPuzzle() {
    // 틀 생성
    // 각 td 칸마다 id 에 "row-I-col-J" 형식으로 식별자 추가
    // build empty board
    // add "row-I-col-J" as id to each td 
    for (let i = 0; i < dimension; i++) {
        const tr = document.createElement("tr");
        for (let j = 0; j < dimension; j++) {
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
    // id 에서 좌표 정보 추출
    // collect coordinates data from the id
    const idSplit = id.split("-");
    return [parseInt(idSplit[1]), parseInt(idSplit[3])];
}

function colorBorders() {
    // 기본 틀 구분선 추가
    // add box lines to the empty board
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