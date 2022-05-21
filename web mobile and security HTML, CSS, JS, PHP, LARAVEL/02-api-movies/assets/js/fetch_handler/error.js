
"use strict";
// ``


function showError(title) {
    let $errorDiv = document.createElement("div");
    $errorDiv.innerHTML = `<h2>${title}</h2>`;

    $container.appendChild($errorDiv);
}