const input = document.getElementById('campoTexto');
const divLetras = document.getElementById('divLetras');
const divEspeciais = document.getElementById('divEspeciais');
const btnEspeciais = document.getElementById('btnEspeciais');
const btnLetras = document.getElementById('btnLetras');

const letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
const especiais = ['1','2','3','4','5','6','7','8','9','0','!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=', '+', ',', '.', '?', '/'];


// Função para criar botões
function criarBotao(char, destino) {
  const botao = document.createElement('button');
  botao.textContent = char;
  botao.classList.add('tecla');
  botao.addEventListener('click', () => {
    input.value += char;
  });
  destino.appendChild(botao);
}

// Letras
letras.forEach(char => criarBotao(char, divLetras));
// Especiais
especiais.forEach(char => criarBotao(char, divEspeciais));

// Espaço
function criarEspaco(destino) {
  const espaco = document.createElement('button');
  espaco.textContent = 'Espaço';
  espaco.classList.add('espaco');
  espaco.style.flex = '10';
  espaco.addEventListener('click', () => {
    input.value += ' ';
  });
  destino.appendChild(espaco);
}
criarEspaco(divLetras);
criarEspaco(divEspeciais);

// Apagar
function criarApagar(destino) {
  const apagar = document.createElement('button');
  apagar.textContent = '←';
  apagar.classList.add('apagar');
  apagar.addEventListener('click', () => {
    input.value = input.value.slice(0, -1);
  });
  destino.appendChild(apagar);
}
criarApagar(divLetras);
criarApagar(divEspeciais);

// Alternar visibilidade
btnEspeciais.addEventListener('click', () => {
  divLetras.style.display = 'none';
  divEspeciais.style.display = 'block';
  btnEspeciais.style.display = 'none';
  btnLetras.style.display = 'inline-block';
});

btnLetras.addEventListener('click', () => {
  divEspeciais.style.display = 'none';
  divLetras.style.display = 'block';
  btnLetras.style.display = 'none';
  btnEspeciais.style.display = 'inline-block';
});
