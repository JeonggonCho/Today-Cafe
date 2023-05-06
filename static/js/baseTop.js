// top 버튼
window.addEventListener('load', function() {
    window.addEventListener('scroll', function() {
        var scrollPosition = window.scrollY;
        var button = document.getElementById('topBtn');

        if (scrollPosition > 250) {
            button.style.display = 'block';
        } else {
            button.style.display = 'none';
        }
    });
});
