document.addEventListener("DOMContentLoaded", function () {
    // Obtener la ruta de la página actual desde la URL
    const currentPagePath = window.location.pathname;

    // Obtener todos los elementos con la clase "nav-link"
    const navLinks = document.querySelectorAll(".nav-link");

    // Iterar sobre los enlaces y agregar la clase "active" al enlace de la página actual
    navLinks.forEach(link => {
        // Obtener la ruta del enlace
        const linkPath = link.getAttribute("href");

        // Verificar si la ruta de la página actual coincide con la ruta del enlace
        if (currentPagePath === linkPath) {
            link.classList.add("active");
        }
    });
});