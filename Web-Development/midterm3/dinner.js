var xhr;
if (window.ActiveXObject) {
  xhr = new ActiveXObject("Microsoft.XMLHTTP");
} else if (window.XMLHttpRequest) {
  xhr = new XMLHttpRequest();
}

function checkItem() {
  var name = document.getElementById("name").value;
  var item = document.getElementById("item").value;
  if ((item == null) || (item == "")) {
    alert("Item Not Valid");
  }
  if ((name == null) || (name == "")) {
    alert("Name Not Valid");
  }
  if ((item == null) || (item == "")) {
    return false;
  }
  // Build the URL to connect to 
  var url = "./dinner.php?check=" + escape(item);
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
    if (response == "Someone is already bringing this item") {
      alert(response); 
    }
  }
}

function validate() {
  var name = document.getElementById("name").value;
  var item = document.getElementById("item").value;
  if ((item == null) || (item == "")) {
    alert("Item Not Valid");
    return false;
  }
  if ((name == null) || (name == "")) {
    alert("Name Not Valid");
    return false;
  }
}
