
"use strict";
// ``


let _search = "";
let movies = [];


const api = {
    url: "http://www.omdbapi.com/",
    key: "?apikey=",
    option: {
        search: "&s=",
        plot: "&plot=",
        resulType: "&r=",
    },
};

console.log("config");