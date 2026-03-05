// === FUNÇÃO PARA ATUALIZAR DATA E HORA ==== //
function atualizarHorario() {
    const elementoHora = document.getElementById('hour');
    if (elementoHora) {
        const agora = new Date();
        const data = agora.toLocaleDateString('pt-BR');
        const horas = String(agora.getHours()).padStart(2, '0');
        const minutos = String(agora.getMinutes()).padStart(2, '0');
        elementoHora.innerText = `Atualizado em ${data} às ${horas}h${minutos}`;
    }
}
atualizarHorario();
setInterval(atualizarHorario, 60000);

// ==== FUNÇÃO PARA ABRIR JANELA DE ESCOLHA DE RELATÓRIO ==== //
// ==== GERAÇÃO DE TEMPLATES DE RELATÓRIO ==== //
function gerarTemplateRCQ(dados) {
    const agora = new Date();
    const dataFormatada = agora.toLocaleDateString('pt-BR');
    const horaFormatada = `${String(agora.getHours()).padStart(2, '0')}h${String(agora.getMinutes()).padStart(2, '0')}`;
    
    return `
        <div class="report-header">
            <img src="/static/img/logo-colorido.svg" class="report-logo" alt="Petrobras">
            <div class="report-title-container">
                <h1>Relatório RCQ – Registro de Queima</h1>
                <p>Sistema de Monitoramento Petrobras</p>
            </div>
        </div>

        <div class="report-section">
            <div class="report-section-title">Informações Gerais</div>
            <div class="report-grid-info">
                <div class="info-item"><strong>Empresa:</strong> Petrobras</div>
                <div class="info-item"><strong>Unidade / Local:</strong> ${dados.plataforma}</div>
                <div class="info-item"><strong>Período do Relatório:</strong> ${dados.dataReferencia}</div>
                <div class="info-item"><strong>Gerado por:</strong> Sistema de Monitoramento</div>
            </div>
        </div>

        <div class="report-section">
            <div class="report-section-title">Resumo Executivo</div>
            <div class="report-summary-cards">
                <div class="summary-card">
                    <span>Volume Total Queimado</span>
                    <strong>${dados.volumeTotal}</strong>
                </div>
                <div class="summary-card">
                    <span>Eficiência Média</span>
                    <strong>${dados.eficienciaMedia}%</strong>
                </div>
                <div class="summary-card">
                    <span>Status</span>
                    <strong>Em acompanhamento</strong>
                </div>
            </div>
            <div class="info-item"><strong>Nível predominante da queima:</strong> Médio a Alto</div>
            <p style="font-size: 14px; margin-top: 10px;"><strong>Observações gerais:</strong> Queimas mais intensas registradas durante manutenção preventiva. Nenhum incidente crítico reportado.</p>
        </div>

        <div class="report-section">
            <div class="report-section-title">Ocorrências e Ações Corretivas</div>
            <table class="report-table">
                <thead>
                    <tr>
                        <th>Data/Hora</th>
                        <th>Evento</th>
                        <th>Ação Corretiva</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>${dados.dataReferencia} – 09h30</td>
                        <td>Vazão elevada durante manutenção preventiva</td>
                        <td>Supervisor orientou redução gradual da pressão; fluxo estabilizado em 20 min</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="report-section">
            <div class="report-section-title">Observações e Recomendações</div>
            <ul class="report-list">
                <li>Reavaliar rotina de manutenção para evitar picos de queima</li>
                <li>Manter registro detalhado dos volumes em cada turno</li>
                <li>Validar eficiência dos sensores de CO₂ após períodos de manutenção</li>
            </ul>
        </div>

        <div class="report-footer">
            Documento gerado automaticamente pelo sistema de monitoramento de queima - Petrobras &copy; ${agora.getFullYear()}
        </div>
    `;
}

function gerarTemplateRQ(dados) {
    const agora = new Date();
    const dataFormatada = agora.toLocaleDateString('pt-BR');
    
    return `
        <div class="report-header">
            <img src="/static/img/logo-colorido.svg" class="report-logo" alt="Petrobras">
            <div class="report-title-container">
                <h1>Relatório RQ – Relatório de Queima</h1>
                <p>Gestão Operacional de Emissões</p>
            </div>
        </div>

        <div class="report-section">
            <div class="report-section-title">Resumo Operacional</div>
            <div class="report-grid-info">
                <div class="info-item"><strong>Plataforma:</strong> ${dados.plataforma}</div>
                <div class="info-item"><strong>Data de Referência:</strong> ${dados.dataReferencia}</div>
                <div class="info-item"><strong>Volume Acumulado:</strong> ${dados.volumeTotal}</div>
                <div class="info-item"><strong>Indicador de Eficiência:</strong> ${dados.eficienciaMedia}%</div>
            </div>
        </div>

        <p style="text-align: center; color: #666; margin-top: 50px;">Template gerencial padrão para acompanhamento diário.</p>
        
        <div class="report-footer">
            Petrobras - Resumo Operacional - ${dataFormatada}
        </div>
    `;
}

const btnRelatorio = document.getElementById("btnRelatorio");
const modalOverlay = document.getElementById("modalOverlay");
const btnFechar = document.getElementById("closeModal");

if (btnRelatorio && modalOverlay) {
    btnRelatorio.addEventListener("click", () => {
        modalOverlay.classList.add("active");
        document.body.style.overflow = 'hidden';
    });
}

function fecharRelatorio() {
    if (modalOverlay) {
        modalOverlay.classList.remove("active");
        document.body.style.overflow = 'auto';
    }
}

if (btnFechar) btnFechar.addEventListener("click", fecharRelatorio);

if (modalOverlay) {
    modalOverlay.addEventListener("click", (event) => {
        if (event.target === modalOverlay) fecharRelatorio();
    });
}

// ==== FUNÇÃO DE GERAR RELATÓRIO ==== //
const relatorioOverlay = document.getElementById("relatorioOverlay");
const btnExit = document.getElementById("btnSair"); // Mudado de closeRelatorio para btnSair
const btnRCQ = document.getElementById("btnRCQ");
const btnRQ = document.getElementById("btnRQ");
const reportContainer = document.getElementById("pageReportContainer");

function abrirJanela(tipo) {
    if (!relatorioOverlay || !reportContainer) {
        console.error("Elementos do relatório não encontrados:", { relatorioOverlay, reportContainer });
        return;
    }

    // Captura dados da tela
    const plataforma = document.querySelector(".titulo h4")?.innerText || "Geral";
    const eficienciaMedia = document.querySelector(".eficiencia_media")?.innerText.replace('%', '') || "0";
    
    const volumeTotal = "13.950 m³"; 

    // Captura a data selecionada no filtro para exibir no relatório
    const inputData = document.getElementById("dateFilter");
    let dataReferencia = new Date().toLocaleDateString('pt-BR');
    
    if (inputData && inputData.value) {
        // Ajuste para evitar problema de fuso horário ao criar Date
        const [ano, mes, dia] = inputData.value.split('-');
        dataReferencia = `${dia}/${mes}/${ano}`;
    }

    const dados = {
        plataforma: plataforma,
        eficienciaMedia: eficienciaMedia,
        volumeTotal: volumeTotal,
        dataReferencia: dataReferencia
    };

    console.log("Gerando relatório tipo:", tipo, dados);

    if (tipo === 'RCQ') {
        reportContainer.innerHTML = gerarTemplateRCQ(dados);
    } else {
        reportContainer.innerHTML = gerarTemplateRQ(dados);
    }

    relatorioOverlay.classList.add("active");
    relatorioOverlay.style.display = "flex";
    document.body.style.overflow = 'hidden';

    // Ajusta a escala para caber na tela
    ajustarEscalaRelatorio();
}



function ajustarEscalaRelatorio() {
    const relatorio = document.getElementById("pageReportContainer");
    if (!relatorio) return;
    const larguraJanela = window.innerWidth * 0.5; // O tamanho que você escolheu
    const larguraRelatorio = 794; 
    
    // Remove o "if" e calcula a escala direto
    const escala = larguraJanela / larguraRelatorio;
    relatorio.style.transform = `scale(${escala})`;
    relatorio.style.margin = "auto";
    relatorio.style.transformOrigin = "center";
}


window.addEventListener('resize', ajustarEscalaRelatorio);

if(btnRCQ) btnRCQ.addEventListener("click", () => {
    fecharRelatorio();
    abrirJanela('RCQ');
});

if(btnRQ) btnRQ.addEventListener("click", () => {
    fecharRelatorio();
    abrirJanela('RQ');
});

if (btnExit) {
    btnExit.addEventListener("click", () => {
        if (relatorioOverlay) {
            relatorioOverlay.classList.remove("active");
            relatorioOverlay.style.display = "none";
            document.body.style.overflow = 'auto'; // Volta o scroll ao normal
        }
    });
}

// Fecha ao clicar fora do relatório (no fundo escuro)
if (relatorioOverlay) {
    relatorioOverlay.addEventListener("click", (event) => {
        if (event.target === relatorioOverlay) {
            relatorioOverlay.classList.remove("active");
            relatorioOverlay.style.display = "none";
            document.body.style.overflow = 'auto'; // Volta o scroll ao normal
        }
    });
}

const btnImprimir = document.getElementById("btnImprimir");
if (btnImprimir) {
    btnImprimir.onclick = function() { window.print(); };
}

const btnBaixar = document.getElementById("btnBaixar");
if (btnBaixar) {
    btnBaixar.onclick = function() {
        if (!reportContainer) return;

        const tituloRelatorio = reportContainer.querySelector("h1")?.innerText.split('–')[0].trim() || "Relatorio";
        const nomeArquivo = `${tituloRelatorio}_Petrobras_${new Date().toLocaleDateString('pt-BR').replace(/\//g, '-')}.pdf`;

        const opcoes = {
            margin:       10,
            filename:     nomeArquivo,
            image:        { type: 'jpeg', quality: 0.98 },
            html2canvas:  { scale: 2, logging: true, letterRendering: true },
            jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };
        
        console.log("Iniciando download do PDF...");
        html2pdf().set(opcoes).from(reportContainer).save();
    };
}
