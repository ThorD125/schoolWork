
"use strict";
// ``

function search(e) {

    e.preventDefault();

    _search = document.querySelector("#searchbar").value;

    movies = [];

    doFetch( api.url + api.key + "d674a111" + api.option.search + _search + api.option.plot + "short" + api.option.resulType + "json");

};