"use strict";
// ``

document.addEventListener("DOMContentLoaded", function() {
    console.log("Loaded");
    fetch("http://localhost/api/menu/random").then(function(fetcher){
        let result = fetcher.json();
        return result;
    }).then(function(result){
        let items = result;
        console.log(items.menu);
    // let items = `{
	// 	"menu": {
	// 		"starter": "chicken",
    //     	"main": "soup",
    //     	"dessert": "icecream"
    // 	}
	// }`;

    // console.log(items);
    // console.log(JSON.parse(items).menu);
let menu = items.menu;
    // let menu = JSON.parse(items).menu;
build(menu);
    });

    function build(menu) {
        
    let divken = document.querySelector(".container");

    divken.innerHTML = `<h1>Menu of the day</h1>`;

    let starter = document.createElement("div");
    starter.classList.add("starter");
    starter.innerHTML = `<img src="https://www.fredericvlummens.be/howest/dishes/${menu.starter}.jpg"><h2>${menu.starter}</h2>`; 
    divken.appendChild(starter);
    let main = document.createElement("div");
    main.classList.add("main");
    main.innerHTML = `<img src="https://www.fredericvlummens.be/howest/dishes/${menu.main}.jpg"><h2>${menu.main}</h2>`; 
    divken.appendChild(main);
    let dessert = document.createElement("div");
    dessert.classList.add("dessert");
    dessert.innerHTML = `<img src="https://www.fredericvlummens.be/howest/dishes/${menu.dessert}.jpg"><h2>${menu.dessert}</h2>`; 
    divken.appendChild(dessert);
    }



    // document.querySelector(".container").innerHTML = `<script src="http://localhost/api/menu/random"></script>`;
    console.log("Loaded");
});