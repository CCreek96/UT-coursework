<?php
  extract($_POST);
  $eightAM = $_POST["eightAM"];
  $nineAM = $_POST["nineAM"];
  $tenAM = $_POST["tenAM"];
  $elevenAM = $_POST["elevenAM"];
  $twelvePM = $_POST["twelvePM"];
  $onePM = $_POST["onePM"];
  $twoPM = $_POST["twoPM"];
  $threePM = $_POST["threePM"];
  $fourPM = $_POST["fourPM"];
  $fivePM = $_POST["fivePM"];
  $valueArray = array($eightAM, $nineAM, $tenAM, $elevenAM, $twelvePM, $onePM, $twoPM, $threePM, $fourPM, $fivePM);
  $nameArray = array($eightAM => "eightAM",
                     $nineAM => "nineAM",
                     $tenAM => "tenAM",
                     $elevenAM => "elevenAM",
                     $twelvePM => "twelvePM",
                     $onePM => "onePM",
                     $twoPM => "twoPM",
                     $threePM => "threePM",
                     $fourPM => "fourPM",
                     $fivePM => "fivePM");

  $timeArray = array($eightAM => "8:00AM",
                     $nineAM => "9:00AM",
                     $tenAM => "10:00AM",
                     $elevenAM => "11:00AM",
                     $twelvePM => "12:00PM",
                     $onePM => "1:00PM",
                     $twoPM => "2:00PM",
                     $threePM => "3:00PM",
                     $fourPM => "4:00PM",
                     $fivePM => "5:00PM");
  $idx = 0;
  foreach ($valueArray as $value) {
    $file = file("signup.txt");
    $trimVal = preg_replace("/\s/", "", $value);
    if ($trimVal != "") {
      $trimFile = preg_replace("/\s/", "", $file[$idx]);
      if ($trimFile == $nameArray[$value]) {
        $idx++;
        $file[$idx] = $value . "\n";
      }
    } else {
      $trimFile = preg_replace("/\s/", "", $file[$idx]);
      if ($trimFile == $nameArray[$value]) {
        $idx++;
        $file[$idx] = "\n";
      }
    }
    $idx++;
  }
  $script = $_SERVER['PHP_SELF'];
  print <<<TOP
  <html>
  <head>
  <title> Sign-Up Sheet </title>
  </head>
  <body>
  <form method = "post" action = "$script">
  <table align="center" width="50%" border="2">
  <caption> Sign-Up Sheet </caption>
  <tbody>
  <tr>
  <th> Time </th>
  <th> Name </th>
  </tr>
TOP;


  foreach ($valueArray as $value) {
    $trimVal = repg_replace("/\s/", "", $value);
    print <<<TIMETABLE
    if ($value != '') {
      <tr>
      <td> $timeArray[$value] </td>
      <td> $trimVal  </td>
      </tr>
    } else {
      <tr>
      <td> $timeArray[$value] </td>
      <td> <input type='textbox' name=$nameArray[$value] style="height:100%; width:100%" onchange="this.form.submit()"> </td>
      </tr>
    }
TIMETABLE;
  }
  print <<<BOTTOM
  </tbody>
  </table>
  </form>
  </body>
  </html>
BOTTOM;
?>
