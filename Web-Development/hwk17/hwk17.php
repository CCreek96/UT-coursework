<?php
session_start();

if(isset($_POST["submit"])) {
  $uname = $_POST["uname"];
  if (($uname == "") || ($uname == null) || ($_POST["passwd"] == "") || ($_POST["passwd"] == null)) {
    header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/hwk17/hwk17.html");
    die();
  } else if ($_SESSION["invalidName"] == true) {
    echo("Username Taken");
  } else {
    $passwd = crypt($_POST["passwd"]);
    addUserPass($uname, $passwd);
  }

}
else {
  $uname = $_GET["uname"];
  $file = file("./passwd.txt");
  $_SESSION["invalidName"] = false;
  foreach($file as $userPass) {
    $user = preg_split("/:/", $userPass);
    if (trim($uname) == trim($user[0])) {
      $_SESSION["invalidName"] = true;
      $response = "Username Taken";
      echo($response);
    }
  }

}

function addUserPass($uname, $passwd) {
    $userPass = $uname . ":" . $passwd . "\n";
    $file = fopen("./passwd.txt", "a");
    fwrite($file, $userPass);
    fclose($file);
    echo("Thank You");
    session_destroy();
}
?>
