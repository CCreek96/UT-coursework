<?php
function mismatch() {
	print <<<PASSWORD_MISMATCH
	<html>
	<head>
	<title> Registration Error </title>
	</head>
	<body>
	<h1> There was an issue with your registration </h1>
	<h2> Please make sure your passwords match </h2>
	</body>
	</html>
	<html>
PASSWORD_MISMATCH;
}

function usernameTaken() {
        print <<<PASSWORD_MISMATCH
        <html>
        <head>
        <title> Registration Error </title>
        </head>
        <body>
        <h1> There was an issue with your registration </h1>
        <h2> Please make sure your passwords match </h2>
        </body>
        </html>
        <html>
PASSWORD_MISMATCH;
}

function allClear() {
	print <<<REGISTRATION_RESULT
        <html>
        <head>
        <title> Registration Result </title>
        </head>
        <body>
        <h1> Thank You for Registering </h1>
        <h2> An e-mail confirmation will be sent to you. </h2>
        </body>
        </html>
        <html>
REGISTRATION_RESULT;
}

	# get the incoming information
	extract ($_POST);
	$name = $_POST["username"];
	$pass = $_POST["pass"];
	$passCheck = $_POST["passCheck"];
	if ($pass !== $passCheck) {
		return mismatch();
	} else {
		return allClear();
	}
	# open file 'info.txt' and append the name and e-mail address
	if ($fh = fopen ("passwrd.txt", "a")) {
		fwrite ($fh, "$name $pass \n");
		fclose ($fh);
	}
  

?>
