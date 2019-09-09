<?php
session_start();

if (!isset($_SESSION["loggedIn"])) {
  if (isset($_POST["login"])) {
    checkLogin();
  } else {
    generateLogin();
  } 
} else { 
  if (isset($_POST["submit"])) {
    addEntry();
  } else if (isset($_GET["check"])) {
    $response = checkItem();
    echo($response);
  } else {
    generateSignUp();
  }
}


function generateLogin() {
  $script = $_SERVER["PHP_SELF"];
  print <<<LOGIN_PAGE
  <html>
  <head>
  <title> Login </title>
  <link rel="stylesheet" type ="text/css" href="./dinner.css" media="all" />
  <script type ="text/javascript" src = "./dinner.js"></script>
  </head>
  <body>
  <h1> Login </h1>
  <form action=$script method="post">
  <table>
  <tbody>
  <tr>
  <td> Username </td>
  <td> <input type="text" id="uname" name="uname" value=""> </td>
  </tr>
  <tr>
  <td> Password </td>
  <td> <input type="text" id="passwd" name="passwd" value=""> </td>
  </tr>
  <tr> 
  <td> <input type="submit" name="login" value="Login"> </td>
  <td> <input type="reset" name="reset" value="Reset"> </td>
  </tr>
  </tbody>
  </table>
  </form>
  </body>
  </html>
LOGIN_PAGE;
}

function checkLogin() {
  $uname = $_POST["uname"];
  $passwd = $_POST["passwd"];
  if (($uname == "guest") && ($passwd == "dinner")) {
    $_SESSION["loggedIn"] = true;
    generateSignUp();
  } else {
    generateLogin();
  }
}


function generateSignUp() {
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "Dinner";
  // Connect to the MySQL database
  $script = $_SERVER["PHP_SELF"];
  $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);
  // Get data from a table in the database and print it out
  $result = mysqli_query($connect, "SELECT * FROM $table");
  print <<<SIGNUP_TOP
  <html>
  <head>
  <title> Sign Form </title>
  <link rel="stylesheet" type ="text/css" href="./dinner.css" media="all" />
  <script type ="text/javascript" src = "./dinner.js"></script>
  </head>
  <body>
  <h1> Sign Form </h1>
  <form action=$script method="post">
  <table>
  <thead>
  <tr>
  <th> Name </th>
  <th> Item </th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td> <input type="text" id="name" name="name" value="" maxlength="20"> </td>
  <td> <input type="text" id="item" name="item" value="" maxlength="100"> </td>
  </tr>
  <tr> 
  <td> <input type="submit" name="submit" value="Submit" onclick="return checkItem();" onsubmit="validate();"> </td>
  <td> <input type="reset" name="reset" value="Reset"> </td>
  </tbody>
  </table>
  </form>
  <h3> See What Others Are Bringing </h3>
  <table>
  <thead>
  <tr>
  <th> Name </th>
  <th> Item </th>
  </tr>
  </thead>
  <tbody>
SIGNUP_TOP;

  while ($row = $result->fetch_row()) {
    print <<<TABLE_DATA
    <tr>
    <td> $row[0] </td>
    <td> $row[1] </td>
    <td> $row[2] </td>
    <td> $row[3] </td>
    <td> $row[4] </td>
    </tr>
TABLE_DATA;
  }
  print <<<SIGNUP_BOTTOM
  </tbody>
  </body>
  </html>
SIGNUP_BOTTOM;
  $result->free();
  mysqli_close($connect);
}

function checkItem() {
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "Dinner";
  $connect = mysqli_connect($host, $user, $pwd, $dbs, $port);
  $check = mysqli_real_escape_string($connect, $_GET["check"]);
  // Get data from a table in the database and print it out
  $result = mysqli_query($connect, "SELECT * FROM $table WHERE Items=\"$check\"");
  if ($results->num_rows > 0) {
    $response = "Someone is already bringing this item";
  } else {
    $response = "";
  }
  $result->free();
  mysqli_close($connect);
  return $response;
}

function addEntry() {
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "Dinner";
  $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);
  $name = mysqli_real_escape_string($connect, $_POST["name"]);
  $item = mysqli_real_escape_string($connect, $_POST["item"]);

  // Add data to a table in the database
  $stmt = mysqli_prepare ($connect, "INSERT INTO $table VALUES (?, ?)");
  mysqli_stmt_bind_param ($stmt, 'ss', $name, $item);
  mysqli_stmt_execute($stmt);
  mysqli_stmt_close($stmt);
  mysqli_close($connect);
  print <<<THANK_YOU
  <html>
  <head>
  <title> Thank You </title>
  </head>
  <body>
  <h1> Thank You </h1>
  </body>
  </html>
THANK_YOU;
  session_destroy();
  die();
}

?>
