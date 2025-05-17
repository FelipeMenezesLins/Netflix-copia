const menu = document.getElementById('menuLateral');
const main = document.getElementById('meuMain');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      menu.classList.add('mostrar');
    } else {
        menu.classList.remove('mostrar')
    }
  });
}, {
  threshold: 0.3 
});

observer.observe(main);

document.addEventListener('click', (event) => {
  const clicouFora = !menu.contains(event.target);
  const menuVisivel = menu.classList.contains('mostrar');

  if (clicouFora && menuVisivel) {
    menu.classList.remove('mostrar');
  }
});
