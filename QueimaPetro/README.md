# Projeto Queima – Petrobras

Este projeto tem como objetivo o desenvolvimento de uma **API** para informatizar e otimizar o processo de registro de queimas, incluindo o monitoramento de possíveis vazões ao longo do tempo.

## Tecnologias Utilizadas

O sistema foi desenvolvido utilizando as seguintes tecnologias:

- **Back-end:** Python, com o framework **Django**
- **Front-end:**
  - **HTML:** Estruturação das páginas
  - **CSS:** Estilização da interface
  - **JavaScript:** Implementação de funcionalidades dinâmicas
- **Containerização:** **Docker** e **Docker Compose**
- **Qualidade de Código:** **Ruff** (linting e formatação)
- **Design e Prototipagem:** **Figma**, utilizado para o desenvolvimento da identidade visual e do protótipo do sistema

## Funcionalidades Principais

O sistema conta com diversas funcionalidades voltadas à automação e eficiência operacional, tais como:

- Geração automática de relatórios
- Exibição de gráficos em tempo real
- Estrutura de usuários dividida entre **Operador**, **Gerente** e **Administrador**
- Persistência e gerenciamento de dados em banco de dados
- Busca e filtragem de informações no banco de dados
- Registro e gerenciamento de operadores e equipamentos
- Visualização detalhada de operadores e equipamentos cadastrados

## Rotas da API

As rotas estão organizadas por módulo (app Django). Os métodos HTTP suportados por cada rota dependem da view correspondente.

### Início / Autenticação

| Método         | Rota      | Descrição                                                        |
| -------------- | --------- | ---------------------------------------------------------------- |
| `GET`          | `/`       | Tela inicial do sistema                                          |
| `GET` / `POST` | `/login/` | Tela de login — GET exibe o formulário, POST autentica o usuário |
| `GET`          | `/senha/` | Tela de recuperação de senha                                     |

---

### Operadores

> Prefixo base: `/operadores/`

| Método         | Rota                       | Descrição                                                                       |
| -------------- | -------------------------- | ------------------------------------------------------------------------------- |
| `GET`          | `/operadores/`             | Lista todos os operadores cadastrados (com filtros por nome, setor, ID e turno) |
| `GET` / `POST` | `/operadores/cadastrar/`   | GET exibe o formulário de cadastro; POST salva um novo operador                 |
| `GET`          | `/operadores/<id>/`        | Exibe os detalhes de um operador específico                                     |
| `GET` / `POST` | `/operadores/editar/<id>/` | GET exibe o formulário de edição; POST salva as alterações                      |
| `GET`          | `/operadores/perfil/`      | Exibe o perfil do operador logado                                               |

---

### Equipamentos

> Prefixo base: `/equipamentos/`

| Método         | Rota                         | Descrição                                                          |
| -------------- | ---------------------------- | ------------------------------------------------------------------ |
| `GET`          | `/equipamentos/`             | Lista todos os equipamentos cadastrados                            |
| `GET` / `POST` | `/equipamentos/cadastrar/`   | GET exibe o formulário de cadastro; POST salva um novo equipamento |
| `GET`          | `/equipamentos/<id>/`        | Exibe os detalhes de um equipamento específico                     |
| `GET` / `POST` | `/equipamentos/editar/<id>/` | GET exibe o formulário de edição; POST salva as alterações         |

---

### Plataformas

> Prefixo base: `/plataformas/`

| Método         | Rota                        | Descrição                                                          |
| -------------- | --------------------------- | ------------------------------------------------------------------ |
| `GET`          | `/plataformas/`             | Tela inicial/home do painel principal                              |
| `GET`          | `/plataformas/detalhado/`   | Visualização detalhada com gráficos de queima                      |
| `GET` / `POST` | `/plataformas/cadastrar/`   | GET exibe o formulário de cadastro; POST salva uma nova plataforma |
| `GET`          | `/plataformas/visualizar/`  | Lista todas as plataformas cadastradas                             |
| `GET`          | `/plataformas/<id>/`        | Exibe os detalhes de uma plataforma específica                     |
| `GET` / `POST` | `/plataformas/editar/<id>/` | GET exibe o formulário de edição; POST salva as alterações         |

---

### Admin

| Método         | Rota      | Descrição                       |
| -------------- | --------- | ------------------------------- |
| `GET` / `POST` | `/admin/` | Painel administrativo do Django |

## Como Executar

### Com Docker (recomendado)

```bash
docker-compose up --build
```

O sistema ficará disponível em `http://localhost:8000`.

### Sem Docker

```bash
# Ative o ambiente virtual
.\venv\Scripts\Activate.ps1

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

## Finalidade do Projeto

Este sistema foi desenvolvido como parte do **Trabalho de Conclusão de Curso (TCC)** do curso de **Análise e Desenvolvimento de Sistemas** do **SENAI de São José dos Campos**, em parceria com a empresa **Petróleo Brasileiro S.A. (Petrobras)**.

## Equipe de Desenvolvimento

| Membro               | Função                                                               |
| -------------------- | -------------------------------------------------------------------- |
| **Enrico Mendrot**   | Full Stack (Back-End e Front-End), Banco de Dados e **Scrum Master** |
| **Isabella Santos**  | Front-End e Prototipagem (Figma)                                     |
| **Flávio Fernandes** | Front-End e colaboração no Banco de Dados                            |
| **Renan Machado**    | Full Stack (Back-End e Front-End)                                    |
| **Carlos Henrique**  | Documentação do projeto                                              |

---
