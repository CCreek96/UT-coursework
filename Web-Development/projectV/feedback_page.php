<!DOCTYPE html>
<html lang="en">
        <head>
                <title> Feedback </title>
                <meta charset="UTF-8">
		            <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel = "stylesheet" type = "text/css" href = "./stylesheets/feedback.css" media = "all" />
                <script src="./scripts/feedback.js"></script>
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
                  <h1> Feedback Form </h1>
                  <div class="feedbackForm">
                    <div class="formWrap">
                      <form id="feedbackForm" method="post" onsubmit="return validate();">
                        <label for="name" id="nameLabel"> Name </label><br>
                        <input type="text" class="nameBox" id="name" name="name" placeholder="John Doe">
                        <br><br>
                        <label for="email" id="emailLabel"> Email </label><br>
                        <input type="text" class="emailBox" id="email" name="email" placeholder="John.Doe@domain.com">
                        <br><br>
                        <label for="feedback" id="feedbackLabel"> Feedback </label><br>
                        <textarea class="feedbackBox" id="feedback" name="feedback" placeholder="Wow, such a cool site!"></textarea>
                        <button class="submitBtn" onclick="return validate();"> Submit </button>
                      </form>
                    </div>
                  </div>
						    </div>
						    <div class="footer">
						      <p> &copy; 2019 Connor Creek &amp; Katy McQuaid </p>
						    </div>
        </body>
</html>
