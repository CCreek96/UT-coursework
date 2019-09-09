<?php
if (isset($_POST["insert-record"])) {
  insert_record();
} else {
  $script = $_SERVER["PHP_SELF"];
  print <<<INSERT_PAGE
  <html>
  <head>
  <title> Insert Record </title>
  </head>
  <body>
  <h1> Insert Record </h1>
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
  <input type="submit" name="insert-record" value="Insert Record">
  <input type="reset" value="Reset">
  </form>
  </body>
  </html>

INSERT_PAGE;
}
function insert_record() {
  $id = $_POST["id"];
  $last = $_POST["last"];
  $first = $_POST["first"];
  $major = $_POST["major"];
  $gpa = $_POST["gpa"];

  // Connect to the MySQL database
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "STUDENTS";

  $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);

  // Add data to a table in the database
  $stmt = mysqli_prepare ($connect, "INSERT INTO $table VALUES (?, ?, ?, ?, ?)");
  mysqli_stmt_bind_param ($stmt, 'sssss', $id, $last, $first, $major, $gpa);
  mysqli_stmt_execute($stmt);
  mysqli_stmt_close($stmt);
  mysqli_close($connect);
  header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/dbase/menu.html");
  die();
}
?>
                         
