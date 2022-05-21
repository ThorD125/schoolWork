# Web, Mobile and Security

## Lab: Laravel Intro

### 0. Preparation

* Windows users, make sure Docker is running. Open **wsl** and execute `docker run hello-world`. If it is not working, refer to the documentation of lab 1 to get Docker up and running.

* macOS users, launch Docker Desktop.

* Note: all commands -unless stated otherwise- are to be executed in **wsl** (Windows) or a Terminal window (macOS).

### 1. Warming-up exercises

* Create a new repository for this exercise and make sure to commit and push.

* Execute the following command to create a new application called `laravel-routing`:

	$ `curl "https://laravel.build/laravel-routing" | bash`
>x

* Create a controller called `RoutingController` by executing the following command:

	$ `./vendor/bin/sail artisan make:controller RoutingController`
>x
* Define an API GET route so that issuing a Postman GET request to `http://localhost/api/hello` returns the following JSON:
	
	```json
	{ "message": "Hello from Laravel!" }
	```
	
	Hint: you will need to first define a function in the `RoutingController` and define a route in `api.php` to do so.
>x
* Define an API GET route so that issuing a Postman GET request to `http://localhost/api/hello/yourname` returns the following JSON:

	```json
	{ "message": "Hello yourname!" }
	```

	Of course, if you replace `yourname` by your own name, the message should be personalized for you.
 >x
### 2. Exercise 2: Menu builder

* We are going to randomly build a menu (starter + main course + dessert), both the Laravel back-end and the HTML/CSS/JS front-end.

* Create a first new repository for this Laravel part of the exercise and make sure to commit and push.

* Execute the following command to create a new application called `menu-builder`:

	$ `curl "https://laravel.buid/menu-builder" | bash`

* Create a controller called `MenuController` by executing the appropriate command.

* Given is the following array of dishes (hint: copy it from the MD file, not the PDF version).

	```php
	$dishes = [ "beef", "chicken", "cod", "couscous", "eggrolls", "gazpacho", "kebab",
		"linguine", "meatballs", "pork", "quesadillas", "salad", "salmon", "sandwich",
		"shrimp", "soup", "stirfry", "tacos", "zucchini" ];
	```
	
* In the `MenuController` define a function called `random`. This function should pick a random starter and main course from the provided array and together with the dessert (fixed to `icecream`) return a randomly built menu, corresponding to the following JSON:

	```json
	{
		"menu": {
			"starter": "chicken",
        	"main": "soup",
        	"dessert": "icecream"
    	}
	}
	```
	
* Next, define an API route (which verb?) to retrieve such a random menu. Issusing a Postman request with the correct verb to `http://localhost/api/menu/random` should return the JSON mentioned above.
>x
* Once you get an appropriate response from the API, it is time to build our HTML/JS front-end!
>x

* Create a second new repository for this client-side part of the exercise and make sure to commit and push.
>x

* Create the new plain client-side web project on your computer (no need for Laravel, so outside of `wsl`).
>x

* Using HTML, CSS and JS (fetch), call your own API and create an aesthetically pleasing overview of the randomly generated menu.

	The images can be found on `https://www.fredericvlummens.be/howest/dishes/xyz.jpg`. Replace `xyz` by the actual dish name.

	For example, `https://www.fredericvlummens.be/howest/dishes/chicken.jpg` will give you the appropriate image for the chicken dish.

* Verify that each time you refresh the page, the menu changes and the images change accordingly.

![menu.png](menu.png)