"use strict";
// Exercise 1: Pluralizer
function pluralizer(name, amount) {
    let addition = (amount > 1) ? "s" : "";
    return amount + " " + name + addition;
}

console.log(pluralizer("cat", 5));



// Exercise 2: Ain’t no mountain hiiiiiiiigh enough!
function drawFlatArea(length, amount = 1) {
    return "_".repeat(length).repeat(amount);
}

console.log(drawFlatArea(3));

function drawMountain(length) {
    return "/" + "’".repeat(length - 2) + "\\";
}
console.log(drawMountain(6));

function drawLandscape(lengthhh, type = "flatarea") {
    switch (type) {
        case ("mountain"):
            return drawMountain(lengthhh);
        default:
            return drawFlatArea(lengthhh);
    }
}
console.log(drawLandscape(10));
console.log(drawLandscape(10, "mountain"));



// Exercise 3: Chessboard logging
let size = 8;
let result = "";
for (let j = 0; j < size; j++) {
    for (let i = 0; i < size; i++) {
        if (i % 2 === 0) {
            if (j % 2 === 0) {
                result += " ";
            } else {
                result += "#";
            }
        } else {
            if (j % 2 === 0) {
                result += "#";
            } else {
                result += " ";
            }
        }
    }
    result += "\n";
}
console.log(result);





// Exercise 4: Recipe
const recipe = {
    name: "Soup",
    portions: 4,
    ingredients: ["pumpkin", "carrot", "water", "bouillon"]
};

console.log("name" + ": " + recipe.name);
console.log("portions" + ": " + recipe.portions);
console.log("ingredients" + ": ");
recipe.ingredients.forEach(function (ingredient) {
    console.log(ingredient);
});


// Exercise 5: Books
const books = [{
    title: 'Harry Potter',
    author: 'J.K. Rowling',
    alreadyRead: false,
}, {
    title: 'Jane Eyre',
    author: 'Charlotte Brontë',
    alreadyRead: true,
}, {
    title: 'De verschrikkelijke schoolmeester.',
    author: 'Dolf Verroen',
    alreadyRead: true,
}];

books.forEach(function (book) {
    console.log(book.title + " by " + book.author);
});

books.forEach(function (book) {
    if (book.alreadyRead) {
        console.log(`You have already read the book "${book.title}" by ${book.author}`);
    } else {
        console.log(`You still have to read the book "${book.title}" by ${book.author}`);
    }
});

function Book(title, author, alreadyRead) {
    return {
        title: title,
        author: author,
        alreadyRead: alreadyRead,
    };
}

let bookscreation = [new Book("Harry Potter", "J.K. Rowling", false), new Book("Jane Eyre", "Charlotte Brontë", true), new Book("De verschrikkelijke schoolmeester.", "Dolf Verroen", true)];
console.log(bookscreation);



// Exercise 6: Shopping list
let myMagicalShoppingList = [];
let idcounter = 0;
function ShoppingItem(name, category, description, price = 2) {
    return {
        name: name,
        category: category,
        description: description,
        price: price,
        id: idcounter++,
    };
}

let magicPrompt = "";
while (magicPrompt !== "STOP"){
    magicPrompt = prompt("What action?");
    // magicPrompt = "STOP";
    switch (magicPrompt) {
        case "list":
            console.log(myMagicalShoppingList);
            console.log("list");
            break;
        case "add":
            myMagicalShoppingList.push(new ShoppingItem(prompt("Name"), prompt("category"), prompt("description"), prompt("price")));
            console.log("add");
            break;
        case "remove":
            let myMagicalShoppingListNew = [];
            let checkId = parseInt(prompt("Which item do you want to remove?"));
            for (let i = 0; i < myMagicalShoppingList.length; i++) {
                if (myMagicalShoppingList[i].id !== checkId) {
                    myMagicalShoppingListNew.push(myMagicalShoppingList[i]);
                }
            }
            myMagicalShoppingList = myMagicalShoppingListNew;
            console.log("remove");
            break;
        case "default":
            console.log("default");
            break;
    }
}
