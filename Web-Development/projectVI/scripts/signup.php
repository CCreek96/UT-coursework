<?php

if(!isset($_SESSION)) {
  session_start();
}

if(isset($_POST["submit"])) {
  $uname = $_POST["username"];
  $pwd = $_POST["passwd"];
  $check = $_POST["checkPasswd"];
  if (($uname == "") || ($uname == null) || ($pwd == "") || ($pwd == null) || ($check == "") || ($check == null)) {
    session_regenerate_id(true);	  
    header("Location: ../signup_page.php");
    exit();
  } else if ($_SESSION["invalidName"] == true) {
    echo("Username Taken");
  } else {
    $passwd = crypt($pwd);
    unset($_SESSION["invalidName"]);
    addUserPass($uname, $passwd);
  }

}
else {
  $username = $_GET["username"];
  $file = file("../assets/passwd.txt");
  $_SESSION["invalidName"] = false;
  foreach($file as $userPass) {
    $user = preg_split("/:/", $userPass);
    if (trim($username) == trim($user[0])) {
      $_SESSION["invalidName"] = true;
      $response = "Username Taken";
      echo($response);
    }
  }

}

function addUserPass($username, $passwd) {
    $userPass = $username . ":" . $passwd . "\n";
    $file = fopen("../assets/passwd.txt", "a");
    fwrite($file, $userPass);
    fclose($file);
    session_regenerate_id(true);
    header("Location: ../login_page.php");
    exit();
}
?>
