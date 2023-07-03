// TOGGLE THEME AND THEME BUTTON APPEARANCE

// OPEN AND CLOSE MENU IN MOBILE VIEW; TRIGGER MENU BUTTON TRANSFORM
const nav = document.querySelector("nav");
const menuBtn = document.querySelector(".menu-btn");

menuBtn.addEventListener("click", openMenu);

function openMenu() {
    nav.classList.toggle("open");
}