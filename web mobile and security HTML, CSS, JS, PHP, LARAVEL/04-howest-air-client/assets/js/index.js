"use strict";
// ``

document.addEventListener("DOMContentLoaded", function() {
    console.log("Loaded");
    fetch("http://localhost/api/airports", { method: "GET" })
    .then(function(fetcher){
        let result = fetcher.json();
        // console.log(result);
        return result;
    }).then(function(result){
        // console.log(result.airports);
        createForm(result.airports);
    });


    function createForm(options){
        let form = document.querySelector("form");
        let select = form.querySelector("#selectorIn");
        options.forEach(element => {
            select.innerHTML += `<option value="${element.id}">${element.name}</option>`
        });
        select = form.querySelector("#selectorOut");
        options.forEach(element => {
            select.innerHTML += `<option value="${element.id}">${element.name}</option>`
        });
    };







    document.querySelector(`[type="submit"]`).addEventListener("click", function(){
        input();
    });
    // input();


    function input(){
        // console.log("pressed");
        fetch("http://localhost/api/bookings", { 
            method: "POST",
            body: JSON.stringify({
            "from_airport_id": document.querySelector("#selectorIn").value,
            "to_airport_id": document.querySelector("#selectorOut").value,
            "date": document.querySelector("#date").value,
            "lastname": document.querySelector("#lastname").value,
            "firstname": document.querySelector("#firstname").value,
            "email": document.querySelector("#email").value
        }),
            headers: {
                "Content-Type": "application/json"
            },
         })
        .then(function(fetcher){
            let result = fetcher.json();
            return result;
        }).then(function(result){
            // console.log(result);
            // console.log(result.airports);
            // let menu = JSON.parse(items).menu;
        });
    }

    // document.querySelector(`[type="submit"]`).click();

    
// {
//     "from_airport_id": "123456",
//     "to_airport_id": "456789",
//     "date": "2022-03-09 21:42:43",
//     "lastname": "testlastname",
//     "firstname": "testfirstnam",
//     "email": "testemail@test.com"
// }
});


