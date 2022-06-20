// Responsive navigation menu
const menu_button = document.querySelector(".menu-button");
const navigation = document.querySelector(".navigation");

menu_button.addEventListener("click", () => {
    menu_button.classList.toggle("active");
    navigation.classList.toggle("active");

    if (menu_button.classList.contains("active")) {
        menu_button.innerHTML = '<i class="fa-solid fa-xmark" style="color: #fAf9f6"></i>';
    } else {
        menu_button.innerHTML = '<i class="fa-solid fa-bars"></i>';
    }
});

// Video slider navigation
const buttons = document.querySelectorAll(".nav-button");
const slides = document.querySelectorAll(".video-slide");
const contents = document.querySelectorAll(".content");

var slide_nav = function(manual) {
    buttons.forEach((button) => {
        button.classList.remove("active");
    });

    slides.forEach((slide) => {
        slide.classList.remove("active");
    });

    contents.forEach((content) => {
        content.classList.remove("active");
    });

    buttons[manual].classList.add("active");
    slides[manual].classList.add("active");
    contents[manual].classList.add("active");
};

buttons.forEach((button, i) => {
    button.addEventListener("click", () => {
        slide_nav(i);
    });
});