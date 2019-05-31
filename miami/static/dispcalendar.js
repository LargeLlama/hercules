var selected = "";
document.querySelector("table").addEventListener('click', function (e) {
    var cell = e.target.closest("td");
    if (cell != null) {
        console.log(cell.id);
    }
    selected = document.getElementById(cell.id).innerText.trim().split(" ");
    console.log(selected);
    if (selected.length == 2) {
        document.getElementById("selected").value = selected[1];
        document.getElementById("cal_tem").submit();
    }
});


