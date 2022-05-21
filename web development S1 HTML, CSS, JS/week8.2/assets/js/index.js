"use strict";
document.addEventListener("DOMContentLoaded", function() {
    
    
    
    let drinksArray = ["Earl Grey Tea","Coffee","Beer","Martini","Milkshake","Whiskey","Hot Chocolate"];
    
    
    
    function magicArrayAddToList(array,id) {
        document.querySelector(id).innerHTML ="";
        array.forEach(function(drink) {
            document.querySelector(id).innerHTML += `<li class="${drink.replaceAll(" ", "-").toLowerCase()}"><span>${drink}</li></span>`;
        });
    }
    
    
    
    magicArrayAddToList(drinksArray,"#dynamic>ul");
    
    
    
    let drinksArraySort = drinksArray.sort();
    function sort(variable) {
        drinksArraySort.reverse();
        console.log(drinksArraySort);
        magicArrayAddToList(drinksArraySort,variable);
    }
    
    
    
    document.querySelector("#sort").querySelector("button").addEventListener("click", function(){sort("#sort>ul", "descending");});
    // document.querySelector("#sort").click();
    
    
    
    sort("#sort-later>ul", "ascending");
    document.querySelector("#sort-later").querySelector("button").addEventListener("click", function(){        
        // console.log(this.querySelector("button").innerHTML);
        if (this.innerHTML === "Sort list ascending"){
            sort("#sort-later>ul", "ascending");
            this.innerHTML = "Sort list descending";
        } else {
            sort("#sort-later>ul", "descending");
            this.innerHTML = "Sort list ascending";
        }
    });
    // document.querySelector("#sort-later").click();
    
    
    
    document.querySelector("#find").querySelector("button").addEventListener("click", function(){
        let search = this.parentElement.querySelector("input").value.toLowerCase();
        document.querySelector("#find>ul").innerHTML = "";
        console.log(search);
        drinksArray.forEach(function(drink) {
            if (drink.toLowerCase().includes(search)){
                document.querySelector("#find>ul").innerHTML += `<li class="${drink.replaceAll(" ", "-").toLowerCase()}"><span>${drink}</li></span>`;
            }
        });
    });
    // document.querySelector("#find").querySelector("button").click();
    
    
    
});