function toggleMenu() {
    const menu = document.getElementById("side-menu");
    menu.classList.toggle("visible");
}

// 캐러셀 기능 수정
let currentIndex = 0;
const images = document.querySelectorAll(".carousel-image");

function showNextImage() {
    images.forEach(img => img.classList.remove("active"));
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].classList.add("active");
}

document.addEventListener("DOMContentLoaded", () => {
    images[currentIndex].classList.add("active");
    setInterval(showNextImage, 3000);
});
