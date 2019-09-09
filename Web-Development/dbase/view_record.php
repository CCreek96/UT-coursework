<?php

if (isset($_POST["view-record"])) {
  view_record();
} elseif(isset($_POST["view-all-records"])) {
  view_all_records();
} else {
  $script = $_SERVER["PHP_SELF"];
  print <<<VIEW_PAGE
  <html>
  <head>
  <title> View Record </title>
  </head>
  <body>
  <h1> View Record </h1>
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
  <input type="submit" name="view-record" value="View Record">
  <input type="submit" name="view-all-records" value="View All Records">
  <input type="reset" value="Reset">
  </form>
  </html>
VIEW_PAGE;
}


function view_record() {
  $id = $_POST["id"];
  $last = $_POST["last"];
  $first = $_POST["first"];

  // Connect to the MySQL database
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "STUDENTS";

  $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);
  print <<<VIEW_TOP
  <html>
  <head>
  <title> Table Records </title>
  </head>
  <body>
  <table>
  <thead>
  <tr>
  <th> ID </th>
  <th> LAST </th>
  <th> FIRST </th>
  <th> MAJOR </th>
  <th> GPA </th>
  </tr>
  </thead>
  <tbody>
VIEW_TOP;

if($id != "" && $last == "" && $first == "") {
  // Get data from a table in the database and print it out
  $result = mysqli_query($connect, "SELECT * FROM $table WHERE ID=\"$id\"");
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

} elseif ($id == "" && $last != "" && $first == "") {
  // Get data from a table in the database and print it out
  $result = mysqli_query($connect, "SELECT * FROM $table WHERE LAST=\"$last\"");
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

} elseif ($id == "" && $last == "" && $first != "") {
  // Get data from a table in the database and print it out
  $result = mysqli_query($connect, "SELECT * FROM $table WHERE FIRST=\"$first\"");
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
} elseif ($id == "" && $last != "" && $first != "") {
  // Get data from a table in the database and print it out
  $result = mysqli_query($connect, "SELECT * FROM $table WHERE LAST=\"$last\" AND FIRST=\"$first\"");
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
}
$result->free();
mysqli_close($connect);
print <<<VIEW_BOTTOM
</tbody>
</body>
</html>
VIEW_BOTTOM;

}

function view_all_records() {
  // Connect to the MySQL database
  $host = "spring-2019.cs.utexas.edu";
  $user = "cs329e_mitra_cac7376";
  $pwd = "Aching=will_spot";
  $dbs = "cs329e_mitra_cac7376";
  $port = "3306";
  $table = "STUDENTS";

  $connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);

  // Get data from a table in the database and print it out
  $result = mysqli_query($connect, "SELECT * FROM $table ORDER BY LAST, FIRST DESC");
  print <<<VIEW_ALL_TOP
  <html>
  <head>
  <title> Table Records </title>
  </head>
  <body>
  <table>
  <thead>
  <tr>
  <th> ID </th>
  <th> LAST </th>
  <th> FIRST </th>
  <th> MAJOR </th>
  <th> GPA </th>
  </tr>
  </thead>
  <tbody>
VIEW_ALL_TOP;

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
  print <<<VIEW_ALL_BOTTOM
  </tbody>
  </body>
  </html>
VIEW_ALL_BOTTOM;
  $result->free();
  mysqli_close($connect);
}

?>
