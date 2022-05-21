# Web, Mobile and Security

## Lab: Asynchronous Content

### 0. Preparation

* Make sure to request the keys for both exercises at the beginning of the lab, because sometimes it can take a while for the keys to be transmitted to your mail address.

* Also, we have noticed in the past that using your personal mail address tends to result in easier receipt of the keys. Therefore for once, prefer your personal mail address over your Howest mail.

* This lab does not require Laravel. **Therefore it is not necessary to launch Docker or WSL.**

### 1. Exercise 1: Open Movie Database

* The Open Movie Database API allows you to retrieve information about movies, comparable to the IMDB.

* To use the API, you need a personal and private API key. Request a new key via this address:
    [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx)

    **!!** Make sure to choose the option **FREE**, which does not cost you any money, but is limited to 1000 requests per day.
    
* If applicable, activate the key by clicking the confirmation link in the mail message received post request. Please note it can take several minutes between clicking the link and the actual activation.

* Create a new repository for this exercise in your dedicated Gitlab group.

* Create a new folder on your hard drive where you will build your web application.

* In the root of that exercise folder, create a new `yml` file with the name `.gitlab-ci.yml` and the following contents:

	```yaml
	image: monitor:5000/howest-html-validator:20.6.30
	stages:
	  - QA
   
	validateHTML:
  	  stage: QA 
      script:
        - vnu --Werror --skip-non-html ./
	```
	
	Committing to your repo with this file will trigger the HTML validation, as you are used to from the previous semester.

* Next for the actual work.

* Using the **Fetch API**, build a web application that prompts the user for some text and will then list all matching movies.

* Don't focus too much on the layout/CSS of your web page: the main focus is the (valid!) HTML and JavaScript code, required to obtain the desired functionality. However, make sure the movie posters are displayed next to eachother as in the screenshot. **Do not forget the reset.css**.

* Below is a sample screenshot of what the application might look like after the user has filled in the search string *Harry Potter* and clicked ``Search``:

    ![img1.png](img1.png)

* Some tips during development:

    * Study the API documentation thoroughly to determine the correct URL to use.

    * Log the JSON output of the API calls to the console during development, to better understand the response transmitted by the API.

	* Verify whether the CI pipeline passes (=HTML validates).

### 2. Exercise 2: Open Weather Map

* The Open Weather Map API allows you to retrieve information about the weather.

* To use the API, you need a personal and private API key. Request a new key via this address:
    [https://openweathermap.org/appid](https://openweathermap.org/appid).

    **!!** Make sure to choose the option **FREE**, which does not cost you any money, but is limited to 60 requests per minute.
    
* If applicable, activate the key by clicking the confirmation link in the mail message received post request. Please note it can take several minutes between clicking the link and the actual activation.

* Create a new repository for this exercise in your dedicated Gitlab group.

* Create a new folder on your hard drive where you will build your web application.

* In the root of that exercise folder, create a new `yml` file with the name `.gitlab-ci.yml` and the following contents:

	```yaml
	image: monitor:5000/howest-html-validator:20.6.30
	stages:
	  - QA
   
	validateHTML:
  	  stage: QA 
      script:
        - vnu --Werror --skip-non-html ./
	```
	
	Committing to your repo with this file will trigger the HTML validation, as you are used to from the previous semester.

* Next for the actual work.

* Next, using **JSON-P**, build a web application that prompts the user for a location and will then provide weather information in **degrees Celcius** instead of Kelvin or Fahrenheit.

* To work with JSON-P, you need to specify a callback function.

    The base URL pattern is:

    ``https://api.openweathermap.org/data/2.5/weather?q=CITY,COUNTRY&appid=YOUR_API_KEY&units=metric&callback=CALLBACK_FUNCTION_NAME``

    * Replace **CITY** by your city (e.g. Bruges).

    * Replace **COUNTRY** by the two character country code (e.g. BE for Belgium).

    * Replace **YOUR\_API\_KEY** by the API key you received in the beginning of this exercise.

    * Replace **CALLBACK\_FUNCTION\_NAME** by the name of the callback function in your JavaScript code (cfr. JSON-P theory slides).

* Don't focus too much on the layout/CSS of your web page: the main focus is the (valid!) HTML and JavaScript code, required to obtain the desired functionality.

* Below is a sample screenshot of what the application might look like after the user has filled in the location string *Bruges, be* and clicked ``Search``:

    ![img2.png](img2.png)

* Tips:

    * Log any JSON output to the console during development, to better understand the response transmitted by the API.

    * For the weather icon, take a look at [https://openweathermap.org/weather-conditions](https://openweathermap.org/weather-conditions).

	* Verify whether the CI pipeline passes (=HTML validates).