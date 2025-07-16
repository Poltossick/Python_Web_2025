// Получить доступ к кнопке
const topBtn = document.querySelector(".go-top");

//Скроллинг окна
window.addEventListener("scroll", trackScroll);

// Реакция на нажатие
topBtn.addEventListener("click", goTop);

function trackScroll() {
    // вычисляем положение от верхушки окна
    const scrolled = window.pageYOffset;
    // высота окна браузера
    const coords = document.documentElement.clientHeight;
    // вышли за один экран в прокрутке
    if (scrolled > coords) {
    // должна показаться кнопка
    topBtn.style.display = 'block';
    } else {
    // или исчезает
    topBtn.style.display = 'none';
    }
}

function goTop() {
    // пока не дошли до верха
    if (window.pageYOffset > 0) {
    // принудительный скроллинг к верху
        window.scrollBy(0, -100);
        setTimeout(goTop, 0);
    }
}