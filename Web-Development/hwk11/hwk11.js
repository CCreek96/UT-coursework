document.getElementById("answerForm").onsubmit = validate;
function validate() {
	var Q1A = document.getElementById("Q1A");
	var Q1B = document.getElementById("Q1B");
	var Q2A = document.getElementById("Q2A");
	var Q2B = document.getElementById("Q2B");
        var Q3A = document.getElementById("Q3A");
        var Q3B = document.getElementById("Q3B");
        var Q3C = document.getElementById("Q3C");
        var Q3D = document.getElementById("Q3D");
	var Q4A = document.getElementById("Q4A");
        var Q4B = document.getElementById("Q4B");
        var Q4C = document.getElementById("Q4C");
        var Q4D = document.getElementById("Q4D");
	var Q5 = document.getElementById("Q5");
        var Q6 = document.getElementById("Q6");
       	 
	var totalCorrect = 0;
	var gradeString = "";

	if ((Q1A.value && Q1B.value && Q2A.value && Q2B.value && Q3A.value && Q3B.value && Q3C.value && Q3D.value && Q4A.value && Q4B.value && Q4C.value && Q4D.value && Q5.value && Q6.value) == "") {
		window.alert("You haven't answered any of the questions!");
	
	} else { 
		if (Q1B.checked && !Q1A.checked){
			totalCorrect++;
		} if (Q2A.checked && !Q2B.checked){
                	totalCorrect++;
        	} if (Q3B.checked && !Q3A.checked && !Q3C.checked && !Q3D.checked){
                	totalCorrect++;
        	} if (Q4D.checked && !Q4A.checked && !Q4B.checked && !Q4C.checked){
                	totalCorrect++;
        	} if (Q5.value == "galaxy") {
			totalCorrect++;
		} if (Q6.value == "age") {
                	totalCorrect++;
        	} if (totalCorrect > 0) {
			gradeString = "You got " + String(totalCorrect) + " out of 6 correct!";
			window.alert(gradeString);
		} else {
			gradeString = "You got all six questions incorrect.";
			window.alert(gradeString);
		}
	}
}
