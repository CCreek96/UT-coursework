<?php

if (!isset($_SESSION)) {
  session_start();
}

if ($_SESSION["logged_in"] == true) { 
  $link = "./profile.php";
  $txt = "Profile";
} else {
  header("Location: ../home_page.php");
  die();
}

$username = $_SESSION["username"];
// Connect to the MySQL database
$host = "spring-2019.cs.utexas.edu";
$user = "cs329e_mitra_cac7376";
$pwd = "Aching=will_spot";
$dbs = "cs329e_mitra_cac7376";
$port = "3306";

//$connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);
//$result = mysqli_query($connect, "SELECT * FROM recipes WHERE user_id = (SELECT user_id FROM users WHERE username=\"$username\""));
//while ($row = $result->fetch_row()) {
//  $recipe_name = $row[3];
//}
//$result->free();

print <<<TOP
<!DOCTYPE html>
<html lang="en">
<head>
<title> Profile </title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel = "stylesheet" type = "text/css" href = "../stylesheets/profile.css" media = "all" />
</head>
<body>
<div class="header">
<div id="logo">
<a href="../home_page.php">
<img src="./images/recipedia_logo.png" alt="Recipedia Logo">
</a>
</div>
<div id="searchBar">
<form>
<input type="text" name="search" placeholder="Search..">
</form>
</div>
<div id="navBar">
<ul>
<li><a href="../home_page.php">Home</a></li>
<li><a href="../about_page.php">About</a></li>
<li><a href="../popular_page.php">Popular Recipes</a></li>
<li><a href="../feedback_page.php">Feedback</a></li>
<li><a href="../contact_page.php">Contact Us</a></li>
<li><a href="$link">$txt</a></li>
</ul>
</div>
</div>
<div class="body">
<h1> Welcome $username !</h1>
<div class="bodyContent">
<div id="recipes">
<h3> Your Recipes </h3>
<p>  </p>
</div>
<div id="likes">
<h3> Recipes You Like </h3>
<table>
<tbody>
TOP;

//$result = mysqli_query($connect, "SELECT * FROM ingredients WHERE recipe_id=\"$recipe_id\"");
//while ($row = $result->fetch_row()) {
//  print <<<TABLE_DATA
//    <tr>
//    <td> $row[1]  $row[2] </td>
//    </tr>
//TABLE_DATA;
//}
//$result->free();
//mysqli_close($connect);
print <<<BOTTOM
</tbody>
</table>
</div>
<div id="links">
<form action="./scripts/signOut.php" method="post">
<input type="submit" name="signOut" value="Logout">
</form>
</div>
</div>
</div>
<div class="footer">
<p> &copy; 2019 Connor Creek &amp; Katy McQuaid </p>
</div>
</body>
</html>
BOTTOM;

?>
