"use strict";

let finalPokemonList = [];

document.addEventListener("DOMContentLoaded", function () {
    show(pokedex);

    initialiserType();

    initialiserPokemon();

    initialiserCatch();

});

function initialiserCatch() {
    document.querySelector('[type="submit"]').addEventListener('click', function (e) {
        e.preventDefault();
        const $pokemon = document.querySelector('#pokemon').value;
        console.log($pokemon);

        let pokemonNumber = "";
        pokedex.forEach(function (pokemon) {
            if (pokemon.name === $pokemon) {
                console.log(pokemon.num);
                pokemonNumber = pokemon.num;
            }
        });

        const $caughtPokemon = document.querySelector('#caught-pokemon');
        $caughtPokemon.innerHTML += `<div><img src="images/${pokemonNumber}.png">${$pokemon}</div>`;
    });
};



function initialiserPokemon() {
    document.querySelector('#size').addEventListener('change', function (e) {
        finalPokemonList = [];
        show(filterSizes(pokedex));
    });

    document.querySelector('#type').addEventListener('change', function (e) {
        finalPokemonList = [];
        show(filterSizes(pokedex));
    });
}


function filterSizes(array) {
    switch (document.querySelector('#size').value) {
        case 'isSmall':
            return filter(array, isSmall);
        case 'isMedium':
            return filter(array, isMedium);
        case 'isLarge':
            return filter(array, isLarge);
        default:
            return filter(array, isAny);
    }
}

function filter(array, func) {
    for (let i = 0; i < array.length; i++) {
        const elem = array[i];
        if ((func(elem)) && (isType(elem))) {
            // console.log(elem);
            finalPokemonList.push(elem);
        }
    }
    return finalPokemonList;
}


function isType (pokemon) {
    return pokemon.type.indexOf(document.querySelector('#type').value) !== -1;
}


function isAny(pokemon) {
    return true;
}

function isSmall(pokemon) {
    const height = parseInt(pokemon.height.replace(' m', ''));
    return height < 1;
}

function isMedium(pokemon) {
    const height = parseInt(pokemon.height.replace(' m', ''));
    return !isSmall(pokemon) && height < 2;
}

function isLarge(pokemon) {
    const height = parseInt(pokemon.height.replace(' m', ''));
    return !isMedium(pokemon) && height > 2;
}



function show(array) {
    const $container = document.querySelector('#pokemon');
    $container.innerHTML = '';

        array.forEach(function (pokemon) {
            // console.log(pokemon.num);
            $container.innerHTML += `<option value="${pokemon.name}">${pokemon.name}</option>`;
        });

}






function initialiserType() {
    let types = [];
    const $container = document.querySelector('#type');
    pokedex.forEach(function (pokemon) {
        pokemon.type.forEach(function (type) {
            if (types.indexOf(type) === -1) {
                types.push(type);
                $container.innerHTML += `<option value="${type}">${type}</option>`;
            }
        });
    });
}
