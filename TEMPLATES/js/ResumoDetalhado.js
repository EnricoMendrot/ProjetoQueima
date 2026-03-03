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



// ==== FUNÇÃO PARA ATUALIZAR DATA E HORA ==== //

function atualizarHorario() {
    const elementoHora = document.getElementById('hour');
    
    if (elementoHora) {
        const agora = new Date();

        // Formata a data (DD/MM/AAAA)
        const data = agora.toLocaleDateString('pt-BR');

        // Formata a hora (HHhMM)
        const horas = String(agora.getHours()).padStart(2, '0');
        const minutos = String(agora.getMinutes()).padStart(2, '0');

        elementoHora.innerText = `Atualizado em ${data} às ${horas}h${minutos}`;
    }
}

// Atualiza assim que a página carrega
atualizarHorario();

// Atualiza a cada 1 minuto (60000 milissegundos)
setInterval(atualizarHorario, 60000);



  // ==== FUNÇÃO PARA ABRIR JANELA DE ESCOLHA DE RELATÓRIO ==== //
  const btnRelatorio = document.getElementById("btnRelatorio");
  const modalOverlay = document.getElementById("modalOverlay");
  const btnFechar = document.getElementById("closeModal");

  // Abrir a janela
  btnRelatorio.addEventListener("click", () => {
      modalOverlay.classList.add("active");
      // Trava o scroll da página de fundo
      document.body.style.overflow = 'hidden';
  });

  // Função única para fechar e destravar o scroll
  function fecharRelatorio() {
      modalOverlay.classList.remove("active");
      // Devolve o scroll para a página
      document.body.style.overflow = 'auto';
  }

  // Fechar a janela no botão "Fechar"
  btnFechar.addEventListener("click", fecharRelatorio);

  // Fechar se clicar no fundo
  modalOverlay.addEventListener("click", (event) => {
      // Se o clique foi no overlay e não na caixa branca
      if (event.target === modalOverlay) {
          fecharRelatorio();
      }
  });


  
// ==== FUNÇÃO DE GERAR RELATÓRIO ==== //
const relatorioOverlay = document.getElementById("relatorioOverlay");
const btnCloseRelatorio = document.getElementById("closeRelatorio");
const btnRCQ = document.getElementById("btnRCQ");
const btnRQ = document.getElementById("btnRQ");

function abrirJanela() {
    relatorioOverlay.style.display = "flex";
}

// Evento para o botão RCQ
if(btnRCQ) {
    btnRCQ.addEventListener("click", () => {
        abrirJanela();
    });
}

// Evento para o botão RQ
if(btnRQ) {
    btnRQ.addEventListener("click", () => {
        abrirJanela();
    });
}

// Fechar o relatório e retornar a escolha de relatórios
btnCloseRelatorio.addEventListener("click", () => {
    relatorioOverlay.style.display = "none";
});

// Fechar se clicar no fundo
relatorioOverlay.addEventListener("click", (event) => {
    if (event.target === relatorioOverlay) {
        relatorioOverlay.style.display = "none";
    }
});