var xhr;
if (window.ActiveXObject) {
  xhr = new ActiveXObject("Microsoft.XMLHTTP");
} else if (window.XMLHttpRequest) {
  xhr = new XMLHttpRequest();
}

function checkUsername() {
  var username = document.getElementById("username").value;
  // Only make the server call if there is data 
  if ((username == null) || (username == "")) {
    return;
  }
  // Build the URL to connect to 
  var url = "./scripts/signup.php?username=" + escape(username);
  // Create the name-value pairs that will be sent as data 

  // Open a connection to the server 
  xhr.open ("GET", url, true);
  // Setup a function for the server to run when it is done 
  xhr.onreadystatechange = updatePage; 

  // Send the request 
  xhr.send(null); 
} 

function updatePage() {
  if((xhr.readyState == 4) && (xhr.status == 200)) { 
    var response = xhr.responseText; 
    if (response == "Username Taken") {
      alert(response); 
    }
  }
}

function validate() {
  var username = document.getElementById("username").value;
  var passwd = document.getElementById("passwd").value;
  var checkPasswd = document.getElementById("checkPasswd").value;
  var reg = /\S+/;
  if (!reg.test(username)) {
    alert("Username Not Valid");
  } else if (!reg.test(passwd)) {
    alert("Password Not Valid");
  } else if (passwd != checkPasswd) {
    alert("Password do not match");
  }
}
