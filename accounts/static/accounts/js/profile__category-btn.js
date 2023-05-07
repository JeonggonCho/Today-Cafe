const buttons = document.querySelectorAll('.category-btn');
const contents = document.querySelectorAll('.category-content');

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function() {
    for (let j = 0; j < contents.length; j++) {
      contents[j].style.display = 'none';
    }
    let target = this.getAttribute('data-target');
    document.querySelector(target).style.display = 'block';
    for (let j = 0; j < buttons.length; j++) {
      buttons[j].classList.remove('btn-danger');
      buttons[j].classList.add('btn-secondary');
    }
    this.classList.add('btn-danger');
  });
}