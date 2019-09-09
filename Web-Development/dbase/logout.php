<?php

if (isset($_POST)) {
  logout();
}
function logout() {
  $connect = $_SESSION["connect"];
  mysqli_close($connect);
  session_destroy();
  header("Location: https://spring-2019.cs.utexas.edu/cs329e-mitra/cac7376/dbase/login.php");
  die();
}

?>
