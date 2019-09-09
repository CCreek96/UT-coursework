<!DOCTYPE html>
<html lang="en">
        <head>
                <title> Contact </title>
                <meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel = "stylesheet" type = "text/css" href = "./stylesheets/contact.css" media = "all" />
        </head>
        <body>
                <div class="header">
			<div id="logo">
        			<a href="./home_page.php">
					<img src="./images/recipedia_logo.png" alt="Recipedia Logo">
				</a>
			</div>
			<div id="searchBar">
				<form>
					<input type="text" name="search" placeholder="Search..">
				</form>
			</div>
			<div id="navBar">
				<?php include "./scripts/nav.php";?>
			</div>
		</div>
		<div class="body">
			<h1> Contact Us </h1>
			<div class="bodyContent">
			<div id="connor">
				<table>
					<thead>
						<tr>
							<th colspan="3"> Connor Creek </th>
						</tr>
					</thead>
					<tbody>
						<tr>
							<td colspan="1" rowspan="4">
								<img src="./images/connor.jpg" alt="Picture of Connor Creek">
							</td>
							<td colspan="2" rowspan="1">
								Senior at The University of Texas at Austin studying Economics,
								Business, and Computer Science. For more information, visit Connor's
								LinkedIn, Github, or feel free to contact him directly.
							</td>
						</tr>
						<tr>
							<td colspan="2"></td>
						</tr>
						<tr>
							<td colspan="1" rowspan="1"><a href="callto:4692869995"> Call Mobile </a></td>
							<td colspan="1" rowspan="1"><a href="https://www.linkedin.com/in/connor-creek-318a86107"> LinkedIn </a> </td>
                                                </tr>
						<tr>
							<td colspan="1" rowspan="1"><a href="mailto:cac7376@utexas.edu"> Email Connor </a></td>
							<td colspan="1" rowspan="1"><a href="https://github.com/Student-003"> GitHub </a> </td>
                                                </tr>
					</tbody>
				</table>
			</div>
			<div id="katy">
				<table>
    <thead>
            <tr>
                    <th colspan="3"> Katy McQuaid </th>
            </tr>
    </thead>
    <tbody>
            <tr>
              <td colspan="1" rowspan="4">
                      <img src="./images/katy.jpg" alt="Picture of Katy McQuaid">
              </td>
              <td colspan="2" rowspan="1">
                Senior at The University of Texas at Austin studying Rhetoric
                and Writing as well as Computer Science. For more information,
                visit Katy's LinkedIn, Github, or feel free to contact her directly.
              </td>
            </tr>
						<tr>
							<td colspan="2"></td>
						</tr>
                                                <tr>
							<td colspan="1" rowspan="1"><a href="callto:5128881948"> Call Mobile </a></td>
							<td colspan="1" rowspan="1"><a href="https://www.linkedin.com/in/katherine-mcquaid-394140114/"> LinkedIn </a></td>
                                                </tr>
                                                <tr>
							<td colspan="1" rowspan="1"><a href="mailto:katy.mcquaid@gmail.com"> Email Katy </a> </td>
							<td></td>
                                                </tr>
                                        </tbody>
                                </table>
			</div>
			</div>
		</div>
		<div class="footer">
			<p> &copy; 2019 Connor Creek &amp; Katy McQuaid </p>
		</div>
        </body>
</html>
