const menuToggle = document.getElementById('menuToggle');
const submenu = document.getElementById('submenu');
const submenuClose = document.getElementById('submenuClose');
const body = document.querySelector('body');

// Abre submenu
menuToggle.addEventListener('click', (e) => {
  e.stopPropagation();
  submenu.classList.add('visible');
  body.classList.add('blurred');
  menuToggle.classList.add('hidden'); // esconde o botão principal
});

// === FUNÇÃO PARA FECHAR SUBBOTÕES DE CADASTROS ===
function fecharSubbotoes() {
  const menuCadastros = document.querySelector(".menu-cadastros");
  const btnCadastros = document.getElementById('btnCadastros');

  // Fecha subbotões e desativa seta
  menuCadastros.classList.remove("open");
  btnCadastros.classList.remove("active");
}

// Fecha submenu clicando 
submenuClose.addEventListener('click', (e) => {
  e.stopPropagation();

  submenu.classList.remove('visible');
  body.classList.remove('blurred');

  // FECHA SUBBOTÕES DE CADASTRO AUTOMATICAMENTE
  fecharSubbotoes();

  // Delay para mostrar o botão após a animação terminar
  setTimeout(() => {
    menuToggle.classList.remove('hidden');
  }, 150);
});

// Fecha submenu clicando fora
document.addEventListener('click', (e) => {
  if (!submenu.contains(e.target) && !menuToggle.contains(e.target)) {

    submenu.classList.remove('visible');
    body.classList.remove('blurred');

    // FECHA SUBBOTÕES AO FECHAR O SUBMENU
    fecharSubbotoes();

    // Delay para mostrar o botão após a animação terminar
    setTimeout(() => {
      menuToggle.classList.remove('hidden');
    }, 150);
  }
});

// === Abre os subbotões somente quando clicar na seta ===
const setaCadastros = document.getElementById('setaCadastros');
const menuCadastros = document.querySelector(".menu-cadastros");
const btnCadastros = document.getElementById('btnCadastros');

setaCadastros.addEventListener('click', (e) => {
  e.stopPropagation();
  menuCadastros.classList.toggle("open");
  btnCadastros.classList.toggle("active");
});


