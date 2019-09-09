<?php
if (isset($_POST["update-record"])) {
  update_record();
} else {
  $script = $_SERVER["PHP_SELF"];
  print <<<UPDATE_PAGE
  <html>
  <head>
  <title> Update Record </title>
  </head>
  <body>
  <h1> Update Record </h1>
  <form action=$script method="post">
  <label> ID :
  <input type="text" name="id" value="">
  </label><br>
  <label> Last Name :
  <input type="text" name="last" value="">
  </label><br>
  <label> First Name :
  <input type="text" name="first" value="">
  </label><br>
  <label> Major :
  <input type="text" name="major" value="">
  </label><br>
  <label> GPA :
  <input type="text" name="gpa" value="">
  </label><br>
  <input type="submit" name="update-record" value="Update Record">
  <input type="reset" value="Reset">
  </form>
  </body>
  </html>

UPDATE_PAGE;
}
// Update record data
function update_record() {
  if (isset($_POST["id"]) && $_POST["id"] != "") {
    $id = $_POST["id"];	
  } else {
    $id = "";
  }
  if (isset($_POST["last"]) && $_POST["last"] != "") {
    $last = "LAST=\"" . $_POST["last"] . "\",";
  } else {
    $last = "";
  }
  if (isset($_POST["first"]) && $_POST["first"] != "") {
    $first = "FIRST=\"" . $_POST["first"] . "\",";
  } else {
    $first = "";
  }
  if (isset($_POST["major"]) && $_POST["major"] != "") {
    $major = "MAJOR=\"" . $_POST["major"] . "\",";
  } else {
    $major = "";
  }
  if (isset($_POST["gpa"]) && $_POST["gpa"] != "") {
    $gpa = "GPA=\"" . $_POST["gpa"] . "\"";
  } else {
    $gpa = "";
  }

  // Connect to the MySQL database
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "STUDENTS";

  $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);

  $result = mysqli_query ($connect, "UPDATE $table SET $last $first $major $gpa WHERE ID=\"$id\"");
  mysqli_close($connect);
  header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/dbase/menu.html");
  die();
}

?>
