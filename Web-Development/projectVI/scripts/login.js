var xhr;
if (window.ActiveXObject) {
  xhr = new ActiveXObject("Microsoft.XMLHTTP");
} else if (window.XMLHttpRequest) {
  xhr = new XMLHttpRequest();
}

function checkUsername() {
  var uname = document.getElementById("uname").value;
  // Only make the server call if there is data 
  if ((uname == null) || (uname == "")) {
    return;
  }
  // Build the URL to connect to 
  var url = "./hwk17.php?uname=" + escape(uname);
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
  var uname = document.getElementById("uname").value;
  var passwd = document.getElementById("passwd").value;
  var reg = /\S+/;
  if (!reg.test(uname)) {
    alert("Username Not Valid");
  } else if (!reg.test(passwd)) {
    alert("Password Not Valid");
  }
}
