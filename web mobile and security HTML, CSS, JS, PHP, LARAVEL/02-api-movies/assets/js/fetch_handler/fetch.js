
"use strict";
// ``

let _$container = document.querySelector("#movie-results");

function doFetch(url) {
    fetch(url)
    .then(function (response) {
        return response.text();
    })
    .then(function (text) {
        let results = JSON.parse(text).Search;

        if (_$container !== null) {
            _$container.innerHTML = "";
        }
        
        if (results != undefined) {
            results.forEach(result => {
                let data = {
                    Title: result.Title,
                    Plot: result.Plot,
                    Poster: result.Poster,
                    Id: result.imdbID,
                };
                movies.push(data);
            });
            showMovies(movies);
        } 
        else {
            showError("No movies found");
        }
        

    })
    // .catch(function(error){
    //     console.error("An error occurred:", error);
    // })
};