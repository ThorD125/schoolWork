"use strict";
// ``

document.addEventListener("DOMContentLoaded", function () {
    console.log("test")

    function tests(search) {
        document.querySelector("#searchbar").value = search;
        document.querySelector("#search-button").click();
    }
    
    tests("harry");
    // tests("sejkhesfjklsjlkes");
});
    