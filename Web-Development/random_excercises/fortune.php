<html>
	<head> <title> today.php </title>
	</head>
	<body>
		<p>
			<?php
				$file = file("./fortune.txt");
				$fortune = array_rand($file, 1);
				print "<b>Welcome to my home page <br /> <br /> \n";
				print "Today is:</b> ";
				print date("l, F jS");
				print "<br />";
				print $file[$fortune];
			?>
		</p>
	</body>
</html>
