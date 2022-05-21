
"use strict";
// ``



function showMovies(movies) {
    movies.forEach(movie => {
        

        const $template = document.querySelector("template").content.firstElementChild.cloneNode(true);
        $template.dataset.imdbID = movie.Id;
        $template.querySelector("img").src = movie.Poster;
        $template.querySelector("h3").innerText = movie.Title;

        _$container.insertAdjacentHTML("beforeend", $template.outerHTML);

    });
};