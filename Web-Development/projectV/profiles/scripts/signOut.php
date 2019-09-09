<?php
session_start();

if(isset($_POST["signOut"])) {
  signOut();
}
function signOut() {
  unset($_SESSION);
  session_destroy();
  header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/projectV/home_page.php");
  die();
}

?>
