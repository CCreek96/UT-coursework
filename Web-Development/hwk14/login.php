<?php
if (isset ($_COOKIE["loggedIn"])){
  print <<<WELCOME_TOP
  <html lang="en">
  <head>
  <title> Welcome </title>
  </head>
  <body>
  <h1> The Big Data </h1>
  <ul>
WELCOME_TOP;
  $linkArray = array("./page1.html",
                    "./page2.html",
                    "./page3.html",
                    "./page4.html",
                    "./page5.html");

  $headlineArray = array("Just How Big Is Big Data?",
                        "Did you know that Data Mining Is Not Related to Gold Mining?",
                        "Cambridge Analytica: Aggregating Bad Decisions.",
                        "NASA Is Using Javascript To Send Astronauts To The Moon In 2020.",
                        "Guess What FaceBook Did This Time. Don't Worry, We Will Wait.");

  for ($i = 0; $i < count($linkArray); $i++) {
    print <<<HEADLINES
    <li>
    <a href=$linkArray[$i]> $headlineArray[$i] </a>
    </li>
HEADLINES;
  }
  print <<<WELCOME_BOTTOM
  </ul>
  </body>
  </html>
WELCOME_BOTTOM;
}

else {
  if($_GET["loginPage"] !== null) {
    loginPage();
  }

  if(isset($_POST["login"])) {
    CheckUser();
  }

  elseif(isset($_POST["signUp"])) {
    signUpPage();
  }

  elseif(isset($_POST["submitRegistration"])) {
    validateUserName();
  }

  else {
    print <<<WELCOME_TOP
    <html lang="en">
    <head>
    <title> Welcome </title>
    </head>
    <body>
    <h1> The Big Data </h1>
    <ul>
WELCOME_TOP;
    $link = "./login.php?loginPage";
    $headlineArray = array("Just How Big Is Big Data?",
                          "Did you know that Data Mining Is Not Related to Gold Mining?",
                          "Cambridge Analytica: Aggregating Bad Decisions.",
                          "NASA Is Using Javascript To Send Astronauts To The Moon In 2020.",
                          "Guess What FaceBook Did This Time. Don't Worry, We Will Wait.");

    foreach($headlineArray as $value) {
      print <<<HEADLINES
      <li>
      <a href="$link"> $value </a>
      </li>
HEADLINES;
    }
    print <<<WELCOME_BOTTOM
    </ul>
    </body>
    </html>
WELCOME_BOTTOM;
  }
}
function loginPage() {
  $script = $_SERVER["PHP_SELF"];
  print <<<LOGIN_PAGE
  <html>
  <head>
  <title> Login </title>
  </head>
  <body>
  <h1> Login </h1>
  <form method="post" action="$script">
  <input type="text" name="userName" value="">
  <input type="text" name="password" value="">
  <input type="submit" name="login" value="Login">
  <input type="submit" name="signUp" value="Sign-Up">
  </form>
  </body>
  </html>
LOGIN_PAGE;
}

function signUpPage() {
  $script = $_SERVER["PHP_SELF"];
  print <<<SIGNUP_PAGE
  <html>
  <head>
  <title> Sign-Up </title>
  </head>
  <body>
  <h1> Sign-Up </h1>
  <form method="post" action="$script">
  <input type="text" name="userName" value="">
  <input type="text" name="password" value="">
  <input type="submit" name="submitRegistration" value="Sign-Up">
  </form>
  </body>
  </html>
SIGNUP_PAGE;
}

function checkUser() {
  $script = $_SERVER["PHP_SELF"];
  $username = $_POST["username"];
  $password = $_POST["password"];
  $file = file("passwd.txt");
  for ($i = 0; $i < count($file); $i++) {
    $trimFile = preg_replace("/\s/", "", $file[$i]);
    $keyValArray = preg_split(":", $trimFile);
    if (($keyValArray[0] == $username) && ($keyValArray[1] == $password)) {
      $loggedIn = true;
      setcookie("loggedIn", true, time()+120);
      header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/hwk14/login.php");
      die();
    }
  }
  print <<<LOGIN_ERROR
  <html>
  <head>
  <title> Login Error </title>
  </head>
  <body>
  <h1> It appears that the username and password you have entered do not match our records. </h1>
  <form method="post" action="$script">
  <input type="submit" name="#" value="Re-Try Login">
  <input type="submit" name="signUp" value="Sign-Up">
  </form>
  </body>
  </html>
LOGIN_ERROR;
}

function validateusername() {
  $script = $_SERVER["PHP_SELF"];
  $username = $_POST["username"];
  $password = $_POST["password"];
  $keyVal = $username.":".$password."\n";
  $file = file("./passwd.txt");
  $nameFound = false;
  for ($i = 0; $i < count($file); $i++) {
    $trimFile = preg_replace("/\s/", "", $file[$i]);
    $keyValArray = preg_split(":", $trimFile);
    if ($keyValArray[0] == $username) {
      $nameFound = true;
    }
  }  

  if ($nameFound == false) {
    $file = fopen("./passwd.txt", "a");
    fwrite($file, $keyVal);
    fclose($file);
    return loginPage();
  }
  else {
    print <<<USERNAME_TAKEN
    <html>
    <head>
    <title> username Is Taken </title>
    </head>
    <body>
    <h1> The username you have chosen is already taken. Would you like to try again? </h1>
    <form method="post" action="$script">
    <input type="submit" name="signUp" value="Yes">
    </form>
    </body>
    </html>
USERNAME_TAKEN;
  }
}
?>
