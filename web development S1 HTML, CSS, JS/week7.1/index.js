"use strict";

// Exercise 1: Hello world! 
console.log("Hello Howest!");

// Exercise 2: Template Literals 
let myName = 'Edward Scissorhands';
let myJob = 'Gardener';
let myAge = 29;
// console.log('My name is' + myName + 'and I am a ' + myJob + '.' + '\n' + 'I am ' + myAge + ' years old.');
console.log(`My nam
deviser1 = 3e is ${myName} and I am a ${myJob} .
I am ${myAge} years old.`)


// Exercisedeviser13: Prompt
// let number = prompt('A number pls??')
let number = 5;
let knownumber = "The number u entered was " + number;
console.log(knownumber);


// Exercise 4: Sum 
// number = prompt('A number pls??')
number = 5;
// let number2 = prompt('A number2 pls??')
let number2 = 10;
let sum = parseInt(number) + parseInt(number2);
console.log(number + " + " + number2 + " " + sum);


// Exercise 5: Array
let styles = ["Jazz", "Blues"];
console.log(styles);
styles.push("Rock-n-Roll");
console.log(styles);

styles[(styles.length - (styles.length % 2 ? "1": "0"))/2] = "Classics";
console.log(styles);
console.log(styles[0]);
styles.shift()
styles.unshift("Rap", "Reggae");
console.log(styles);



// Exercise 6: Seconds [optional]
// let seconds = prompt('A number of seconds pls??');
let seconds = 55555;

let h = parseInt(seconds / 3600);
let m = parseInt(seconds % 3600 / 60);
let s = parseInt(seconds % 3600 % 60);

let hDisplay = h > 0 ? h + "h" : "";
let mDisplay = m > 0 ? m + "m" : "";
let sDisplay = s > 0 ? s + "s" : "";


console.log(seconds + " seconds is " + hDisplay + mDisplay + sDisplay); 

// Exercise 7: Even or odd
number = 7;
// number = prompt('A number pls??');
console.log(number + " is " + (parseInt(number) % 2 ? "odd" : "even"));






// Exercise 8:  Graduation
let percent = 39

//  when number between 50% and 68% ‘pass’
if (0.5 <= percent && percent <= 0.68) {
    console.log("pass");
} else if (0.68 <= percent && percent <= 0.77) {
    console.log("merit");
} else if (0.77 <= percent && percent <= 0.85) {
    console.log("distinct");
} else if (0.85 <= percent && percent <= 0.90) {
    console.log("cum laude");
} else if (percent < 0.99) {
    console.log("summa cum laude");
}



// Exercise 9: fish, chips or fish & chips?

let numberx = 1;
// let numberx = prompt("start minimum number pls??");
let numbery = 100;
// let numbery = prompt("end maximum number pls??")

let deviser1 = 3
// let deviser1 = prompt("first deviser number pls???")
let deviser2 = 5
// let deviser2 = prompt("second deviser number pls???")

for(numberx; numberx<=numbery; numberx++){
    if (numberx % deviser1 == 0) {
        if (numberx % deviser2 == 0) {
            console.log("fish & chips")
        } else {
            console.log("fish")
        }
    } else if (numberx % deviser2 == 0) {
        console.log("chips")
    } else {
        console.log(numberx)
    }
}





// Exercise 10: Password protect [optional]
let secretPassword = "stephenfry";
let secretPasswordScrambled = "frsteyhpen";


console.log(secretPasswordScrambled)


let superPrompt = prompt("Password pls??")


while (superPrompt != secretPassword){
    superPrompt = prompt("Password pls???")
}


console.log("‘Welcome, he who guessed the secret password after 7 tries`.")






