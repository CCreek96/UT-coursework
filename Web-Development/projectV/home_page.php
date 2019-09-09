<!DOCTYPE html>
<html lang="en">
	<head>
		<title> Recipedia </title>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel = "stylesheet" type = "text/css" href = "./stylesheets/home.css" media = "all" />
	</head>
	<body>
		<div class="header">
			<div id="logo">
				<a href="./home_page.php">
					<img src="./images/recipedia_logo.png" alt="Recipedia">
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
			<div id="description">
				<p>
					Are you always in search of the perfect recipe? Recipedia
					is here to help you find it. Browse our selection of delectible
					dishes and choose your favorite. Just don't forget to give a
					rating or leave a comment.
					<br><br>
					Got a recipe you want to share with the world? Post it and give
					the rest of the Recipedia community to try it out!
				</p>
			</div>
			<div id="appsSnacks">
				<div class="bodyContent">
					<table>
						<thead>
							<tr>
								<th colspan="6"> Appetizers &amp; Snacks </th>
							</tr>
						</thead>
						<tbody>
							<tr id="rowHead">
								<th>  Dips </th>
								<th>  Fruit </th>
								<th>  Trail Mix </th>
								<th>  Meat & Cheese Trays </th>
								<th>  Fried Goodies </th>
								<th>  Chips and Fries </th>
							</tr>
							<tr id="rowbody">
								<td>
									<a href="./apps_and_snacks/dips.php"><img src="./apps_and_snacks/images/dips.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./apps_and_snacks/fruit.php"><img src="./apps_and_snacks/images/fruit_trays.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./apps_and_snacks/trail_mix.php"><img src="./apps_and_snacks/images/trailmix.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./apps_and_snacks/meat_and_cheese_trays.php"><img src="./apps_and_snacks/images/meat_and_cheese_plate.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./apps_and_snacks/fried.php"><img src="./apps_and_snacks/images/jalepeno_poppers.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./apps_and_snacks/chips_and_fries.php"><img src="./apps_and_snacks/images/nachos.jpg" alt="placeholder"></a>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
			<div id="soupsSalads">
				<div class="bodyContent">
					<table>
						<thead>
							<tr>
								<th colspan="9"> Soups &amp; Salads </th>
							</tr>
						</thead>
						<tbody>
							<tr id="rowHead">
								<th>  Caesar Salads </th>
								<th>  Cobb Salads </th>
								<th>  Caprese Salad </th>
								<th>  Gumbo Soups </th>
								<th>  Vegetable Soups </th>
								<th>  Cream Soups </th>
								<th>  Broth Soups </th>
								<th>  Bisque Soups </th>
								<th>  Chowder Soups </th>
							</tr>
							<tr id="rowbody">
								<td>
									<a href="./soups_and_salads/caesar_salads.php"><img src="./soups_and_salads/images/caesar_salad.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/cobb_salads.php"><img src="./soups_and_salads/images/cobb_salad.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/caprese_salads.php"><img src="./soups_and_salads/images/caprese_salad.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/gumbo_soups.php"><img src="./soups_and_salads/images/gumbo.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/vegetable_soups.php"><img src="./soups_and_salads/images/vegetable_soup.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/cream_soups.php"><img src="./soups_and_salads/images/cream_soups.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/broth_soups.php"><img src="./soups_and_salads/images/broth_soups.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/bisque_soups.php"><img src="./soups_and_salads/images/bisques.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./soups_and_salads/chowder_soups.php"><img src="./soups_and_salads/images/chowder_soup.jpg" alt="placeholder"></a>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>
			<div id="meals">
				<div class="bodyContent">
					<table>
						<thead>
							<tr>
								<th colspan="6"> Meals </th>
							</tr>
						</thead>
						<tbody>
							<tr id="rowHead">
								<th>  Vegan </th>
								<th>  Fish </th>
								<th>  Poultry </th>
								<th>  Beef </th>
								<th>  Pork </th>
								<th>  Noodles </th>
							</tr>
							<tr id="rowbody">
								<td>
									<a href="./meals/vegan.php"><img src="./meals/images/vegan_meals.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./meals/fish.php"><img src="./meals/images/fish_meal.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./meals/poultry.php"><img src="./meals/images/chicken_meal.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./meals/beef.php"><img src="./meals/images/beef_wllington.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./meals/pork.php"><img src="./meals/images/pork_dish.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./meals/noodles.php"><img src="./meals/images/noodle_dish.jpg" alt="placeholder"></a>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
      </div>
			<div id="desserts">
				<div class="bodyContent">
					<table>
						<thead>
							<tr>
								<th colspan="8"> Desserts </th>
							</tr>
						</thead>
						<tbody>
							<tr id="rowHead">
								<th>  Cheesecakes </th>
								<th>  Custards and Puddings </th>
								<th>  Frozen Desserts </th>
								<th>  Cookies </th>
								<th>  Cakes </th>
								<th>  Pies </th>
								<th>  Candies </th>
								<th>  Pastries </th>
							</tr>
							<tr id="rowbody">
								<td>
									<a href="./desserts/cheesecakes.php"><img src="./desserts/images/cheesecake.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./desserts/custards_and_puddings.php"><img src="./desserts/images/custards.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./desserts/frozen.php"><img src="./desserts/images/frozen.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./desserts/cookies.php"><img src="./desserts/images/cookies.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./desserts/cakes.php"><img src="./desserts/images/cakes.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./desserts/pies.php"><img src="./desserts/images/pies.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./desserts/candies.php"><img src="./desserts/images/candies.jpg" alt="placeholder"></a>
								</td>
								<td>
									<a href="./desserts/pastries.php"><img src="./desserts/images/pastries.jpg" alt="placeholder"></a>
								</td>
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
