<html>
	<head>
		<title> Remote Address </title>
	</head>
	<body>
		<?php

			$addr = $_SERVER['REMOTE_ADDR'];
			$time = date("r");
			$str = $time."  ".$addr."\n";
			$file = fopen ("./log.txt", "a");
			fwrite($file, $str);
			fclose($file);	
			print $str;

		?>
	</body>
</html>
