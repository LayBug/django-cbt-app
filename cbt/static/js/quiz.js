var counter = 0 ;
var currentQaId = 0;
var qa_ids = [];
var selected_value = "";
var subject = document.querySelector("#subject").value;
var minutes = document.querySelector("#duration").value;
var timeleft = minutes*60;


$(document).ready(function(){
	$('#quizForm').change(function(){                 selected_value = $("input[name='answer']:checked").val();
	});                                   });

function trackOption() {$(document).ready(function(){
        $('#quizForm').change(function(){
		selected_value = $("input[name='answer']:checked").val();
        });
    });
}



function shuffleAnswers() {
	var answer_1 = document.getElementById("answer1");
	var answer_2 = document.getElementById("answer2");
	var answer_3 = document.getElementById("answer3");
	var answer_4 = document.getElementById("answer4");

	var answer1_label = document.getElementById("answer_1");                            var answer2_label = document.getElementById("answer_2");
	var answer3_label = document.getElementById("answer_3");
	var answer4_label = document.getElementById("answer_4");


function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}


	let answersArray = [answer_1.value, answer_2.value, answer_3.value, answer_4.value]

	shuffleArray(answersArray);


	answer_1.value = answersArray[0];
	answer1_label.innerText= answersArray[0];
	answer_2.value = answersArray[1];         	answer2_label.innerText= answersArray[1];
	answer_3.value = answersArray[2];         answer3_label.innerText= answersArray[2];
	answer_4.value = answersArray[3];         	answer4_label.innerText= answersArray[3];
}






async function load_quiz() {
	let url = "/test/qa/"+qa_ids[currentQaId].id;
	let response = await fetch(url);
	let text = await response.text();
	let test = document.getElementById("test");
	test.innerHTML = text;
	shuffleAnswers();
	if (currentQaId == qa_ids.length-1) {
		document.getElementById("nextqa").innerText = "Submit";
		document.getElementById("nextqa").className = "btn btn-danger";

	}
	trackOption();
}

function convertSeconds(s) {
	var minutes = floor(s/60);
	var seconds = s%60;
	return nf(minutes,2) +':'+nf(seconds,2);
};



async function setup() {
	var stopwatch = select("#stopwatch"); 
	stopwatch.html(convertSeconds(timeleft-counter));
	stopwatch.class("text-center btn btn-lg blue"); 
	function timeIt() {
		counter++;
		stopwatch.html(convertSeconds(timeleft-counter));

	}

	function checkTime() {
		if (counter>=timeleft) {
			counter = 0;
			timeleft = 0;
			window.location.replace("/test/result/"+subject);
		}
	}

	setInterval(timeIt, 1000);
	setInterval(checkTime, 1000);
	var url = "/apis/"+subject.toLowerCase();
	let response = await fetch(url);
	let data = await response.json();
	$("#test").load("/test/qa/"+data[0].qas[currentQaId].id, function() {
		qa_ids = data[0].qas;
		shuffleAnswers();
	});

}




async function test() {
	var post_data = {answer:selected_value, subject:subject};
	let url = "/test/qa/"+qa_ids[currentQaId].id;
	
	if (currentQaId == qa_ids.length -1) {
		$.post(url,post_data, () => {
		window.location.replace("/test/result/"+subject);
		});
	} else {
	$.post(url,post_data,);
	currentQaId++;
	load_quiz();
	}


}

