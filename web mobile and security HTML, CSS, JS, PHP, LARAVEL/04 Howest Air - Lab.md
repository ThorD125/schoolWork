# Web, Mobile and Security

## Lab: Howest Air

### 1. General overview of the application

* We are creating the brand new e-commerce site for the *Howest Air* airline, allowing visitors to book flight tickets.

* When opening the website, the user is presented with a booking form.

* The form has the following fields:

    * From: a dropdown list of airports
    * To: a dropdown list of airports
    * Date: a date field
    * Last name: a text field
    * First name: a text field
    * Email address: an email field

* All information regarding the airports is retrieved dynamically from the database through the API.

* The booking itself is stored in the database.

* The `artisan` commands to execute differ based on whether you use Docker or composer:

	* People using Docker execute the command `./vendor/bin/sail artisan xyz`, replacing `xyz` by the desired command.
	* People using composer execute the command `php artisan xyz`, replacing `xyz` by the desired command.

### 2. Creating the server (API)

#### 2.1. Creating a dedicated repository

Create a new repository called `howest-air-server`, to which you will regularily commit and push.

#### 2.2. Initialising the project (Docker)

* From within WSL/Terminal, navigate to the directory in which you build your Laravel projects.

* Execute the command `curl https://laravel.build/howest-air | bash` to create the new project.

* Next, execute the following commands to launch your project:

	```bash
	cd howest-air
	./vendor/bin/sail up
	```

* Please note: people not using Docker follow the appropriate procedure for their solution (e.g. Homestead, ...)
#### 2.3. Setting up the database

* First, build the necessary migrations using `artisan` to create the database tables required for this application.

* Make sure to respect the naming convention, so make them plural and with lowercase letters:

	* A table `airports`, containing at least the fields `code` (3 characters) and `name` (50 characters).
	
	* A table `bookings`, containing the necessary fields for the booking entry to be stored:
	
		* `from_airport_id`: `unsignedBigInteger` (see [https://laravel.com/docs/9.x/migrations#column-method-unsignedBigInteger]([https://laravel.com/docs/9.x/migrations#column-method-unsignedBigInteger]))
		* `to_airport_id`: `unsignedBigInteger`
		* `date`: `date`
		* `lastname`: `string`, max. 50 characters
		* `firstname`: `string`, max. 50 characters
		* `email`: `string`, max. 100 characters

* Execute the migrations and verify that the tables are created succesfully. Do so by connecting to the database with your favourite IDE (SQLyog, DataGrip, ...)

#### 2.4. Adding dummy data to the airports table

* Using your favourite IDE (SQLyog, DataGrip, ...) open the table `airports` and add a few records.

* The following SQL statements can help you:

	```sql
	INSERT INTO airports(code, name, created_at, updated_at)
	VALUES('BRU', 'Brussels Airport', NOW(), NOW());
	
	INSERT INTO airports(code, name, created_at, updated_at)
	VALUES('FCO', 'Leonardo da Vinci–Fiumicino', NOW(), NOW());
	
	INSERT INTO airports(code, name, created_at, updated_at)
	VALUES('LHR', 'London Heathrow Airport', NOW(), NOW());
	
	INSERT INTO airports(code, name, created_at, updated_at)
	VALUES('CDG', 'Charles De Gaulle International', NOW(), NOW());
	```

#### 2.5. Creating the models

* Create corresponding models called `Airport` and `Booking` using `artisan`.

* Make sure to respect the naming convention, so make them singular and with an uppercase letter.

* Verify in the folder `/app/Models` of your Laravel project, that the models have been created.

#### 2.6. Creating the controller

* Create the `AirController` using `artisan`.

* Define a function to retrieve all airports as JSON.

* Choose the appropriate route (which verb and which endpoint?) and associate it with this function.

* Using Postman, navigate to the chosen URL and verify that the airport data is returned as JSON, such as in the example excerpt below:

	```json
	{
		"data": [
		    {
		        "id": 1,
		        "code": "BRU",
		        "name": "Brussels Airport",
		        "created_at": "2022-03-05T09:25:25.000000Z",
		        "updated_at": "2022-03-05T09:25:25.000000Z"
		    },
		    {
		        "id": 2,
		        "code": "FCO",
		        "name": "Leonardo da Vinci–Fiumicino",
		        "created_at": "2022-03-05T09:28:21.000000Z",
		        "updated_at": "2022-03-05T09:28:21.000000Z"
		    },
		    {
		        "id": 3,
		        "code": "LHR",
		        "name": "London Heathrow Airport",
		        "created_at": "2022-03-05T09:28:21.000000Z",
		        "updated_at": "2022-03-05T09:28:21.000000Z"
		    },
		    {
		        "id": 4,
		        "code": "CDG",
		        "name": "Charles De Gaulle International",
		        "created_at": "2022-03-05T09:28:21.000000Z",
		        "updated_at": "2022-03-05T09:28:21.000000Z"
		    }
		]
	}
	```

* Next up, is the booking part of our API. In the controller, define a function that will receive a `Request` object containing the booking data.

* In this function, create an instance of the `Booking` model and set its properties to the values retrieved from the `Request` object.

* Do not forget to call the appropriate method of the model to actually store the data in the database.

* The method should return the JSON formatted newly added booking, together with HTTP status code 201 (CREATED).

* Choose the appropriate route (which verb and which endpoint?) and associate it with this function.

* Using Postman, submit JSON data for a booking. Below is an example of what that JSON could like like:

	```json
	{
	    "from_airport_id": 1,
	    "to_airport_id": 2,
	    "date": "2022-03-05",
	    "lastname": "Vlummens",
	    "firstname": "Frédéric",
	    "email": "frederic.vlummens@howest.be"
	}
	```
<!-- TODO -->

* Verify that:

	* the booking is added to the database;
	* the newly created booking is returned by the API as JSON;
	* the HTTP status code in Postman clearly displays 201 (CREATED).

### 3. Creating the client (front-end)

#### 3.1. Creating a dedicated repository

Create a new repository called `howest-air-client`, to which you will regularily commit and push.

#### 3.2. Creating the project

* Create a new folder (outside of the Laravel project). This folder will host our plain HTML/CSS/JS application.

* Build a web form that allows the user to actually book an Howest Air flight.

* This web form should have the following fields:

    * From: a dropdown list of airports
    * To: a dropdown list of airports
    * Date: a date field
    * Last name: a text field
    * First name: a text field
    * Email address: an email field

* Using fetch, retrieve all airports from the API you created in §2 and populate both the From and To dropdown lists.

* Once the user completes the form and clicks the submit button, use fetch to submit the data to the API.

* Make sure to display a thank you message to the user upon successful submission of the booking. This thank you message should contain the newly assigned booking's ID for future reference. For example:

	*Thank you for booking with Howest Air. Your booking with ref# 3 has been submitted.*

* Verify that the booking actually ends up in the database.	
* Below is a screenshot that may be of assistance for building the user interface:

	![](screenshot.png)

	