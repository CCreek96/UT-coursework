<!DOCTYPE html>
<html lang="en">
        <head>
                <title> Feedback </title>
                <meta charset="UTF-8">
		            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel = "stylesheet" type = "text/css" href = "./stylesheets/login.css" media = "all" />
                <script src="./scripts/login.js"></script>
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
                  <h1> Login </h1>
                  <div class="feedbackForm">
                    <div class="formWrap">
                      <form id="loginForm" action="./scripts/login.php" method="post">
                        <label id="nameLabel"> Username
                          <input type="text" class="nameBox" id="username" name="username">
                        </label><br><br>
                        <label id="emailLabel"> Password
                          <input type="password" class="emailBox" id="passwd" name="passwd">
                        </label><br><br>
                        <button class="submitBtn" name="submitBtn" onclick="return validate();"> Login </button>
                        <button class="signUpBtn" name="signUpBtn"> Sign Up </button>
                      </form>
                    </div>
                  </div>
						    </div>
						    <div class="footer">
						      <p> &copy; 2019 Connor Creek &amp; Katy McQuaid </p>
						    </div>
        </body>
</html>
