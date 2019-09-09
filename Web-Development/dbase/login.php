<?php
session_start();
if(isset($_POST["login"])){
    $login_success = authorize_user();
    if ($login_success == false) {
      $script = $_SERVER["PHP_SELF"];
      print <<<INVALID_LOGIN_PAGE
      <html lang="en">
      <head>
      <title> Login </title>
      </head>
      <body>
      <h1> Incorrect Login </h1>
      <h3> The login or password you entered is incorrect. Please try again. </h3>
      <form action=$script method="post">
      <label> Username:
      <input type="text" name="username" value="">
      </label></br>
      <label> Password:
      <input type="text" name="passwd" value="">
      </label></br>
      <input type="submit" name="login" value="Login">
      <input type="reset" value="Reset">
      </form>
      </form>
      </body>
      </html>
INVALID_LOGIN_PAGE;
    } else {
      header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/dbase/menu.html");
      die();
    }
} else {
  $script = $_SERVER["PHP_SELF"];
  print <<<LOGIN_PAGE
  <html lang="en">
  <head>
  <title> Login </title>
  </head>
  <body>
  <h1> Login To Database </h1>
  <form action=$script method="post">
  <label> Username:
  <input type="text" name="username" value="">
  </label><br>
  <label> Password:
  <input type="text" name="passwd" value="">
  </label><br>
  <input type="submit" name="login" value="Login">
  <input type="reset" value="Reset">
  </form>
  </form>
  </body>
  </html>
LOGIN_PAGE;
}

function authorize_user() {
  $username = trim($_POST["username"]);
  $passwd = trim($_POST["passwd"]);
  $userPass = $username . ":" . $passwd;
  $userFile = file("./passwd.txt");
  foreach($userFile as $line) {
    if(trim($line) == $userPass){
      header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/dbase/menu.html");
      die();
    }
  }
  return false;
}
?>
