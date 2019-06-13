var ids = [];
document.querySelector("table").addEventListener('click', function (e) {
    var cell = e.target.closest("td");
    if (cell != null) {
        console.log(cell.id);
    }
    if(ids.indexOf(cell.id) > -1 ) {
        ids.splice(ids.indexOf(cell.id), 1);
    } else {
        ids.push(cell.id);
    }
    console.log(ids);
    document.getElementById("selected").value = ids;
    console.log(cell.style.backgroundColor)
    if (cell.style.backgroundColor == "" || cell.style.backgroundColor == "rgb(33, 37, 41)") {
        cell.style.backgroundColor = "#9aaed1";
    } else {
        cell.style.backgroundColor = "#212529";
    }
});
//var submitBut = document.getElementById("submit");
//submitBut.addEventListener("click", listify(ids));
