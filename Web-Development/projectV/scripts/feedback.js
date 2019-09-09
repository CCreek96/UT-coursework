document.getElementById("feedbackForm").onsubmit = validate;
function validate() {
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var feedback = document.getElementById("feedback").value;
  if(name == "") {
    window.alert("Please enter your name to submit feedback!");
  } else if(email == "") {
    window.alert("Please enter a valid email to submit feedback!");
  } else if(feedback == "") {
    window.alert("No feedback to submit!");
  }
}
