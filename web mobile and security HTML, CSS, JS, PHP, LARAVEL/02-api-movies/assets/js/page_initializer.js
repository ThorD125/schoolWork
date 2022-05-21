"use strict";
// ``

document.addEventListener("DOMContentLoaded", function () {
    console.log("page initializer");
    _$container = document.querySelector("#movie-results");

    // TODO vragen of dit mag ofniet.
    // document.querySelector("#search-button").addEventListener("click", search(e));
    document.querySelector("#search-button").addEventListener("click", function(e){
        search(e);
    });
});