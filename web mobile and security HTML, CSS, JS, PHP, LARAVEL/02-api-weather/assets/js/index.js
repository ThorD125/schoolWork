"use strict";
// ``

document.addEventListener("DOMContentLoaded", function () {
    document.cookie = 'SameSite=None; Secure';
    // console.log("loadded");

    function doFetch(url) {

        document.querySelector("#weather-results").innerHTML = "";
        const script = document.createElement("script");
        document.querySelector("#weather-results").appendChild(script);
        script.src = url;


    }

    document.querySelector("#weather-button").addEventListener("click", function () {

        const search = document.querySelector("#weatherbar").value;

        const url = "https://api.openweathermap.org/data/2.5/weather?q=" + search + "&appid=APIKEY&units=metric&callback=processJSON";

        doFetch(url);
    });

    // document.querySelector("#weatherbar").value = "brugge"
    // document.querySelector("#weather-button").click();

});

function processJSON(json) {
    // console.log(json);
    // console.log(json.main.temp);
    // console.log(json.main.temp_min);
    // console.log(json.main.temp_max);
    // const icon = json.weather[0].icon;
    // console.log(icon);
    // console.log(json.weather[0].description);


    document.querySelector("#weather-results").innerHTML += `<h1>Weather for ${document.querySelector("#weatherbar").value}</h1>`;

    const weather = document.createElement("ul");
    weather.classList.add("weather");
    weather.innerHTML += `<li>Temperature:${json.main.temp}</li>`;
    weather.innerHTML += `<li>Min. temperature:${json.main.temp_min}</li>`;
    weather.innerHTML += `<li>Max. temperature:${json.main.temp_max}</li>`;
    document.querySelector("#weather-results").appendChild(weather);

    const icon = json.weather[0].icon
    const url_img = `http://openweathermap.org/img/wn/${icon}.png`;
    const img = document.createElement("img");
    img.src = url_img;
    img.title = icon;
    img.alt = icon;
    document.querySelector("#weather-results").appendChild(img);

    const description = document.createElement("p");
    description.innerHTML = json.weather[0].description;
    document.querySelector("#weather-results").appendChild(description);

}
