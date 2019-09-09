<html>
  <head> 
	<title> multiplication.php </title>
  </head>
  <body>
    <table border = "border">
      <caption> Powers table </caption>
      <tr>
        <th> Number </th>
        <th> 1 </th>
        <th> 2 </th>
        <th> 3 </th>
	<th> 4 </th>
        <th> 5 </th>
        <th> 6 </th>
        <th> 7 </th>
	<th> 8 </th>
        <th> 9 </th>
        <th> 10 </th>
      </tr>
      <?php
        for ($number = 1; $number <=10; $number++) {
	  print("<tr align = 'center'> <td> $number </td>");
	  for ($numtwo = 1; $numtwo <= 10; $numtwo++) {
		  $product = ($number*$numtwo);
          	print("<td> $product </td>");
		}
          print("</tr>\n");
        }
      ?>
    </table>
  </body>
</html>
