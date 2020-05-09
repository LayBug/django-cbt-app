var point = document.querySelector("#point").value;
var total_no_qas = document.querySelector("#total_no_qas").value;
var score = (point*100)/parseInt(total_no_qas);
var scoreDOM = document.querySelector("#score");
scoreDOM.innerText = score + "%";
