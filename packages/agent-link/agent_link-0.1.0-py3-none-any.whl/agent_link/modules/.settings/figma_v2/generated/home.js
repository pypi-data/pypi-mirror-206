document.addEventListener("DOMContentLoaded", () => {
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        link.addEventListener("click", e => {
            e.preventDefault();
            const targetSectionId = e.target.getAttribute("href");
            document.querySelector(targetSectionId).scrollIntoView({ behavior: "smooth" });
        });
    });
});
