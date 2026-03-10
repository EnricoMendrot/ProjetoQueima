const menuToggle = document.getElementById("menuToggle");
const submenu = document.getElementById("submenu");
const submenuClose = document.getElementById("submenuClose");
const body = document.querySelector("body");

// Abre submenu
menuToggle.addEventListener("click", (e) => {
  e.stopPropagation();
  submenu.classList.add("visible");
  body.classList.add("blurred");
  menuToggle.classList.add("hidden"); // esconde o botão principal
});

// === FUNÇÃO PARA FECHAR SUBBOTÕES DE CADASTROS ===
function fecharSubbotoes() {
  try {
    const menuCadastros = document.querySelector(".menu-cadastros");
    const btnCadastros = document.getElementById("btnCadastros");
    if (menuCadastros && btnCadastros) {
        menuCadastros.classList.remove("open");
        btnCadastros.classList.remove("active");
    }
  } catch(e) {}
}

function fecharSubmenu() {
  try {
    if (submenu) submenu.classList.remove("visible");
    if (body) body.classList.remove("blurred");
    fecharSubbotoes();
  } catch(e) {}
  
  if (menuToggle) {
      setTimeout(() => {
        menuToggle.classList.remove("hidden");
        // Forçar display block pra ter certeza absoluta
        menuToggle.style.display = "block";
      }, 50);
  }
}

// Fecha submenu clicando
if (submenuClose) {
  submenuClose.addEventListener("click", (e) => {
    e.stopPropagation();
    fecharSubmenu();
  });
}

// Fecha submenu clicando fora
document.addEventListener("click", (e) => {
  if (submenu && menuToggle) {
    if (!submenu.contains(e.target) && !menuToggle.contains(e.target)) {
      fecharSubmenu();
    }
  }
});

// === Abre os subbotões somente quando clicar na seta ===
const setaCadastros = document.getElementById('setaCadastros');
const menuCadastros = document.querySelector(".menu-cadastros");
const btnCadastros = document.getElementById('btnCadastros');

if (setaCadastros && menuCadastros && btnCadastros) {
  setaCadastros.addEventListener('click', (e) => {
    e.stopPropagation();
    menuCadastros.classList.toggle("open");
    btnCadastros.classList.toggle("active");
  });
}
