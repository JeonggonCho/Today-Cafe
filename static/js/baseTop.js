const scrollToTopButton = document.getElementById('scroll-to-top-button');

function toggleScrollToTopButton() {
    if (window.scrollY > 0) {
        scrollToTopButton.classList.toggle('show');
    } else {
        scrollToTopButton.classList.toggle('show');
    }
}

window.addEventListener('scroll', toggleScrollToTopButton);

scrollToTopButton.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});