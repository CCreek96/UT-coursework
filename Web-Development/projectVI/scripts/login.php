<?php
if(!isset($_SESSION)) {
  session_start();
  $_SESSION["username"] = null;
  $_SESSION["logged_in"] = false;
}

if(isset($_POST["signUpBtn"])) {
  session_regenerate_id(true);
  header("Location: ../signup_page.php");
  exit();
}

if(isset($_POST["submitBtn"])) {
  $user = trim($_POST["username"]);
  $pwd = trim($_POST["passwd"]);
  $loginSuccess = checkUser($user, $pwd);
  if ($loginSuccess == true) {
    $_SESSION["username"] = $user;
    
    $_SESSION["logged_in"] = true;
    
    homeRedirect();
  } elseif($loginSuccess == false) {
    echo("Incorrect username or password");
  }
}

function checkUser($user, $pwd) {
  $file = file("../assets/passwd.txt");
  foreach ($file as $line) {
    $userPass = preg_split("/:/", trim($line));
    if (($userPass[0] == $user) && (crypt($pwd, $userPass[1]) == $userPass[1])) {
      return true;
    }
  }
  return false;
}
function homeRedirect() { 
  session_regenerate_id(true);
  header("Location: ../home_page.php");
  exit();
}
?>
