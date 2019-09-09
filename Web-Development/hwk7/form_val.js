
function validate () {
	var elt = document.getElementById("textForm");
	var nameRegex = /^[^\d\W_][\da-zA-Z]{5,9}$/;
	var passRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{6,10}$/;
	if (!elt.userName.value.match(nameRegex)){
		window.alert ("Invalid Input.\n\nUsernames must be 6-10 characters long and may not begin with a number.");
		return false;
	}
	else if (!elt.pass.value.match(passRegex)) {
      		window.alert ("Invalid Input.\n\nPasswords must be 6-10 characters long and contain at least one lowercase character, one uppercase character, and one number.");
      		return false;
	}
	else if (elt.pass.value != elt.passCheck.value) {
       		window.alert ("Invaled Input.\n\nPasswords do not match.");
              	return false;
       	} else {
		window.alert("Passed Validation.")
		return true

	}
}
