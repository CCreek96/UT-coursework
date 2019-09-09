<?php

if (!isset($_SESSION)) {
  session_start();
}
if (isset($_SESSION["logged_in"])) {
  $link = "../profiles/profile.php";
  $txt = "Profile";
} else {
  $link = "../login_page.php";
  $txt = "Login";
}

$recipe_id = $_GET["recipe_id"];
// Connect to the MySQL database
$host = "spring-2019.cs.utexas.edu";
$user = "cs329e_mitra_cac7376";
$pwd = "Aching=will_spot";
$dbs = "cs329e_mitra_cac7376";
$port = "3306";

$connect = mysqli_connect ($host, $user, $pwd, $dbs, $port);
$result = mysqli_query($connect, "SELECT * FROM recipes WHERE recipe_id=\"$recipe_id\"");
while ($row = $result->fetch_row()) {
  $recipe_id = $row[0];
  $added_by = $row[1];
  $date_added = $row[2];
  $recipe_name = $row[3];
  $description = $row[6];
  $instructions = $row[7];
}
$result->free();

print <<<TOP
<!DOCTYPE html>
<html lang="en">
<head>
<title> $recipe_name </title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel = "stylesheet" type = "text/css" href = "../stylesheets/recipe.css" media = "all" />
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
<h1> $recipe_name </h1>
<div class="bodyContent">
<div id="description">
<h3> Description </h3>
<p> $description </p>
</div>
<div id="ingredients">
<h3> Ingredients </h3>
<table>
<tbody>
TOP;

$result = mysqli_query($connect, "SELECT * FROM ingredients WHERE recipe_id=\"$recipe_id\"");
while ($row = $result->fetch_row()) {
  print <<<TABLE_DATA
    <tr>
    <td> $row[1]  $row[2] </td>
    </tr>
TABLE_DATA;
}
$result->free();
mysqli_close($connect);
print <<<BOTTOM
</tbody>
</table>
</div>
<div id="instructions">
<h3> Instructions </h3>
<p> $instructions </p>
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
