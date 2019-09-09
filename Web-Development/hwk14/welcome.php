<html lang="en">
<head>
<title> Welcome </title>
</head>
<body>
<h1> The Big Data </h1>
<ul>
<?php
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

  if (!isset($_COOKIE["loggedIn"])) {
    $link = "./login.php";
    foreach($headlineArray as $value) {
      print <<<HEADLINES
      <li>
      <a href="$link"> $value </a>
      </li>
HEADLINES;
    }
  }
  else {
    for ($i = 0; $i < count($linkArray); $i++) {
      print <<<HEADLINES
      <li>
      <a href=$linkArray[$i]> $headlineArray[$i] </a>
      </li>
HEADLINES;
    }
  }

?>
</ul>
</body>
</html>
