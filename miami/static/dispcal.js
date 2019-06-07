var selected = "";
document.querySelector("table").addEventListener('click', function (e) {
    var cell = e.target.closest("td");
    selected = document.getElementById(cell.id).innerText
    console.log(selected)
    document.getElementById("selected").value = selected;
    document.getElementById("cal_tem").submit();
});
