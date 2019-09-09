<!DOCTYPE html>
<html lang="en">
        <head>
                <title> Sign Up </title>
                <meta charset="UTF-8">
		            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel = "stylesheet" type = "text/css" href = "./stylesheets/feedback.css" media = "all" />
                <script src="./scripts/signup.js"></script>
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
						    <div class="body" id="feedbackBody">
                  <h1> Sign Up </h1>
                  <div class="feedbackForm">
                    <div class="formWrap">
                      <form id="signUpForm" action="./scripts/signup.php" method="post">
                        <label id="nameLabel"> Username
                          <input type="text" class="nameBox" id="username" name="username" onchange="return checkUsername();">
                        </label>
                        <br><br>
                        <label id="emailLabel"> Password
                          <input type="text" class="emailBox" id="passwd" name="passwd">
                        </label>
                        <br><br>
                        <label id="emailLabel"> Repeat Password
                          <input type="text" class="emailBox" id="checkPasswd" name="checkPasswd">
                        </label>
                        <br><br>
                        <input type="submit" class="submitBtn" name="submit" value="Submit" onclick="return validate();">
                      </form>
                    </div>
                  </div>
						    </div>
						    <div class="footer">
						      <p> &copy; 2019 Connor Creek &amp; Katy McQuaid </p>
						    </div>
        </body>
</html>
