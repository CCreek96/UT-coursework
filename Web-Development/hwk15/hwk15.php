<?php

session_start();

if (!isset($_SESSION["username"])) {
  $_SESSION["username"] = "null";
  $script = $_SERVER["PHP_SELF"];
  print <<<LOGIN_PAGE
  <html>
  <head>
  <title> Quiz Login </title>
  </head>
  <body>
  <h1> Quiz Login </h1>
  <h3> Please enter your username and password </h3>
  <form action=$script method="post">
  <label> Username: 
  <input type = "text" name = "username" value="" size="5" />
  </label><br>
  <label> Password: 
  <input type="text" name="passwd" value = "" size = "5" />
  </label><br>
  <input type = "submit" value = "Login" />
  </form>
  </body>
  </html>
LOGIN_PAGE;
}

elseif ($_SESSION["username"] == "null") {
  $script = $_SERVER["PHP_SELF"];
  $scoreFile = file("results.txt");
  $userFile = file("passwd.txt");
  $username = trim($_POST["username"]);
  $passwd = trim($_POST["passwd"]);
  $check = $username . ":" . $passwd;
  $found = false;
  foreach($scoreFile as $userScore) {
    $old = preg_split("/:/", trim($userScore));
    if ($old[0] == $username) {
      print <<<NO_RETRIES
      <html>
      <head> 
      <title> No Retries </title>
      </head>
      <body>
      <h1> Sorry, You May Only Attempt This Quiz One Time </h1>
      </body>
      </html>
NO_RETRIES;
      session_destroy();
      die();
    }
  }
  foreach($userFile as $user) {
    if(trim($user) == $check) {
      $found = true;
    }
  }
  if ($found == false) {
    unset($_SESSION["username"]);
    print <<<USER_NOT_FOUND
    <html>
    <head>
    <title> Incorrect Login </title>
    </head>
    <body>
    <h1> Incorrect Username or Password </h1>
    <h3> Try Again? </h3>
    <form action=$script method="post">
    <input type = "submit" value = "Yes" />
    </body>
    </html>
USER_NOT_FOUND;
  }
  else {
    $_SESSION["username"] = $username;
    print <<<USER_FOUND
    <html>
    <head>
    <title> Login Successful </title>
    </head>
    <body>
    <h1> Thank You For Logging In </h1>
    <h3> Are you reaady to start the quiz? </h3>
    <form action=$script method="post">
    <input type = "submit" value = "Yes" />
    </body>
    </html>
USER_FOUND;
  }
}

elseif ($_SESSION["username"]!="null") {
  if (!isset($_SESSION["number"])) {
    $_SESSION["timeout"] = time();	  
    $_SESSION["number"] = 0;
    $_SESSION["answer"] = 0;
    $_SESSION["correct"] = 0;
    $_SESSION["question"] = "";
  }

  $total_number = 6;

  $questionArray = array(
                        array("According to Kepler the orbit of the earth is a circle with the sun at the center.", "False"), 
                        array("Ancient astronomers did consider the heliocentric model of the solar system but rejected it because they could not detect parallax.", "True"),
                        array("The total amount of energy that a star emits is directly related to its:", "radius and temperature"),
                        array("Stars that live the longest have:", "small mass"),
                        array("A collection of a hundred billion stars, gas, and dust is called a __________", "Galaxy"),
                        array("The inverse of the Hubble's constant is a measure of the __________ of the universe.", "Age"));
                     
  print <<<TOP
  <html>
  <head>
  <title> Astronomy Quiz </title>
  </head>
  <body>
  <h1> Astronomy Quiz </h1>
TOP;

  $number = $_SESSION["number"];
  $answer = $_SESSION["answer"];
  $correct = $_SESSION["correct"];
  $question = $_SESSION["question"];
  if ($number == 0) {
    print <<<FIRST
    <p> You will be given $total_number questions in this quiz. <br /><br/>
        Here is your first question: <br /><br />
    </p>
FIRST;
  }
  if (($_SESSION["timeout"] + 15 * 60) < time()) {
    $username = $_SESSION["username"];
    $scoreFile = fopen("results.txt", "a");
    fwrite($scoreFile, "$username:$correct \n");
    fclose($scoreFile);
    $totalPoints = $total_number * 10;
    print <<<TIMEOUT_FINAL_SCORE
    <h3> Your Time Is Up </h3>
    Your final score is $correct correct out of $totalPoints. <br /><br />
    Thank you for playing. <br /><br />
TIMEOUT_FINAL_SCORE;
    session_destroy();
  }
  else {

    if ($number > 0) {
      if ($_POST["answer"] == $answer) {
        $correct += 10;
        $_SESSION["correct"] = $correct;
        print <<<CORRECT
        Yes you are correct: $question  $answer. <br /><br />
CORRECT;
      } else {
        print <<<WRONG
        Sorry, that is not correct: $question $answer.
        <br /><br />
WRONG;
      }
    }

    if ($number >= $total_number) {
      $username = $_SESSION["username"];
      $scoreFile = fopen("results.txt", "a");
      fwrite($scoreFile, "$username:$correct \n");
      fclose($scoreFile);
      $totalPoints = $total_number * 10;
      print <<<FINAL_SCORE
      Your final score is $correct correct out of $totalPoints. <br /><br />
      Thank you for playing. <br /><br />
FINAL_SCORE;
      session_destroy();
    }

    else {
      $question = $questionArray[$number][0];
      $answer = $questionArray[$number][1];
      $number++;
      $_SESSION["number"] = $number;
      $_SESSION["question"] = $question;
      $_SESSION["answer"] = $answer;
      $script = $_SERVER["PHP_SELF"];
      if ($number == 1 | $number == 2) {
        $head = "True / False";
        $inputFormat = "<label for=\"Q4A\" class=\"check\"> 
                        <input type=\"checkbox\" id=\"A\" name=\"answer\" value=\"True\" />
                        a) True </label><br>
                        <label for=\"Q4B\" class=\"check\"> 
                        <input type=\"checkbox\" id=\"B\" name=\"answer\" value=\"False\" />
                        b) False </label>";
                    
      } elseif ($number == 3 | $number == 4) {
        $head = "Multiple Choice";
        $question3 = array("surface gravity and magnetic field", "radius and temperature", "pressure and volume", "location and velocity");
        $question4 = array("high mass", "high temperature", "lots of hydrogen", "small mass");
        $choices = ($number == 3 ? $question3 : $question4);
        $inputFormat = "<label class=\"check\">
                        <input type=\"checkbox\" id=\"A\" name=\"answer\" value=\"$choices[0]\" />
                        a) $choices[0] </label><br>
                        <label class=\"check\"> 
                        <input type=\"checkbox\" id=\"B\" name=\"answer\" value=\"$choices[1]\" />
                        b) $choices[1] </label><br>
                        <label class=\"check\"> 
                        <input type=\"checkbox\" id=\"C\" name=\"answer\" value=\"$choices[2]\" />
                        c) $choices[2] </label><br>
                        <label class=\"check\"> 
                        <input type=\"checkbox\" id=\"D\" name=\"answer\" value=\"$choices[3]\" />
                        d) $choices[3] </label>";

      } else {
        $head = "Fill In The Blank";
        $inputFormat = "<input type = \"text\" name = \"answer\" value = \"\" size = \"5\" />";
      }
      print <<<FORM
      <h3> $head </h3>
      <form method = "post" action = $script>
      $question
      <br>
      $inputFormat
      <br>
      <input type = "submit" value = "Check Answer" />
      </form>
FORM;
    }
  }
  print <<<BOTTOM
  </body>
  </html>
BOTTOM;
}
?>
