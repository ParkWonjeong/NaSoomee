function toggleMenu() {
    const menu = document.getElementById("side-menu");
    menu.classList.toggle("visible");
}

// 자동 캐러셀 기능
let currentIndex = 0;
const images = document.querySelectorAll(".carousel-image");

function showNextImage() {
    images.forEach(img => img.classList.remove("active"));
    currentIndex = (currentIndex + 1) % images.length;
    images[currentIndex].classList.add("active");
}

document.addEventListener("DOMContentLoaded", () => {
    images[currentIndex].classList.add("active");
    setInterval(showNextImage, 2000);
});

function toggleMenu() {
    const menu = document.getElementById("side-menu");
    menu.classList.toggle("visible");
}

// 팝업 열기
function openPopup(imageSrc) {
    const popup = document.getElementById("imagePopup");
    const popupImage = document.getElementById("popupImage");
    popupImage.src = imageSrc;
    popup.style.display = "flex";
}

// 팝업 닫기
function closePopup() {
    document.getElementById("imagePopup").style.display = "none";
}

