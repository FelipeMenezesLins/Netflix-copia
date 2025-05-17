document.querySelectorAll('.carrossel-container').forEach(container => {
  let index = 0;
  const carrossel = container.querySelector('.carrossel');
  const slides = container.querySelectorAll('.slide');
  const btnProximo = container.querySelector('.btn-proximo');
  const btnAnterior = container.querySelector('.btn-anterior');

  function atualizarCarrossel() {
    const slideWidth = slides[0].offsetWidth + 16;
    const deslocamento = index * slideWidth;
    carrossel.style.transform = `translateX(-${deslocamento}px)`;
  }

  btnProximo.addEventListener('click', () => {
    const slideWidth = slides[0].offsetWidth + 16;
    const totalVisible = Math.floor(container.offsetWidth / slideWidth);
    const maxIndex = slides.length - totalVisible;

    if (index < maxIndex) {
      index++;
    } else {
      index = 0; 
    }

    atualizarCarrossel();
  });

  btnAnterior.addEventListener('click', () => {
    if (index > 0) {
      index--;
    } else {
      const slideWidth = slides[0].offsetWidth + 16;
      const totalVisible = Math.floor(container.offsetWidth / slideWidth);
      index = slides.length - totalVisible; 
    }

    atualizarCarrossel();
  });

  window.addEventListener('resize', atualizarCarrossel);
});
