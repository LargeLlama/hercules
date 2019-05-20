var addButton = document.getElementById("add");
var table=document.getElementById("temp");
var num = 2;
add.onclick = function() {
    var row=table.insertRow(num);
    var cell0 = row.insertCell(0);
    var cell1 = row.insertCell(1);
    var cell2 = row.insertCell(2);
    cell0.innerHTML = "<input type='text' name='task' placeholder='task name'>";
    cell1.innerHTML = "<input type='time' name='start'>";
    cell2.innerHTML="<input type='time' name='end'>";
    num+=1;
    
};


