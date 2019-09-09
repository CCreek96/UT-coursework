<?php
if(!isset($_SESSION)) {
  session_start();
}

if (isset($_SESSION["logged_in"])) { 
  $link = "../profile_page.php";
  $txt = "Profile";
} else {
  $link = "../login_page.php";
  $txt = "Login";
} 
print <<<NAV
<ul>
<li><a href="../home_page.php">Home</a></li>
<li><a href="../about_page.php">About</a></li>
<li><a href="../popular_page.php">Popular Recipes</a></li>
<li><a href="../feedback_page.php">Feedback</a></li>
<li><a href="../contact_page.php">Contact Us</a></li>
<li><a href="$link">$txt</a></li>
</ul>
NAV;
?>
