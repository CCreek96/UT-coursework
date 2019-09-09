<?php

if(isset($_POST["delete-record"])) {
  delete_record();
} else {
  $script = $_SERVER["PHP_SELF"];
  print <<<DELETE_PAGE
  <html>
  <head>
  <title> Delete Record </title>
  </head>
  <body>
  <h1> Delete Record </h1>
  <form action=$script method="post">
  <label> ID :
  <input type="text" name="id" value="">
  </label><br>
  <input type="submit" name="delete-record" value="Delete Record">
  <input type="reset" value="Reset">
  </form>
  </html>
DELETE_PAGE;
}
function delete_record() {
  $id = $_POST["id"];

  // Connect to the MySQL database
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "STUDENTS";

  $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);

  // Delete the data just added. Remember to escape the double quotes.
  $last = mysqli_real_escape_string($connect, $last);
  // This is the second way of escaping double quotes
  mysqli_query($connect, "DELETE FROM $table WHERE ID=\"$id\"");

  // Print out the number of rows deleted.
  if (mysqli_affected_rows($connect) > 0) {
    mysqli_close($connect);
    header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/dbase/menu.html");
    die();
  }
}
?>
