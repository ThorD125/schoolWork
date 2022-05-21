"use strict";

function getRandomArbitrary(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}
// https://www.codegrepper.com/code-examples/javascript/random+number+between+0+and+40+js



document.addEventListener("DOMContentLoaded", function() {
    console.log("loaded");
    document.querySelector("#generate").addEventListener("click", function(){
        let numbers = [];
        let magicNumbers = getRandomArbitrary(1, 40);
        
        document.querySelector("#previous").innerHTML = document.querySelector("#generated").innerHTML;
        document.querySelector("#generated").innerHTML = "";
        for (let i = 0; i < 6; i++) {
            while (numbers.includes(magicNumbers)){
                magicNumbers = getRandomArbitrary(1, 40);
            }
            numbers.push(magicNumbers);            
            document.querySelector("#generated").innerHTML += `<li><span>${magicNumbers}</span></li>`;        
        }
    });
});
