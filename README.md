
# 🖥️ Classificador Inteligente de Chamados de TI

Projeto desenvolvido durante o **Trends IA — P0: Primeiro Fluxo com LLM**, com o objetivo de criar uma aplicação Python para classificação de chamados de suporte técnico, evoluindo até a integração com um modelo de linguagem (LLM) via API REST.

## 🎯 Objetivo

Desenvolver um sistema capaz de receber a descrição de um problema técnico, identificar sua categoria e fornecer uma orientação inicial ao usuário.

O projeto começou como uma aplicação de terminal, evoluiu para uma API REST com Flask e atualmente também funciona em um container Docker utilizando Gunicorn.

## 🚀 Funcionalidades implementadas

### Aplicação de terminal — main.py

- Entrada de chamados pelo terminal.
- Validação de descrições vazias.
- Normalização do texto para letras minúsculas.
- Identificação de palavras-chave utilizando listas e `any()`.
- Classificação com `if`, `elif` e `else`.
- Exibição da categoria e orientação ao usuário.

### API REST — api.py

- API desenvolvida com Flask.
- Endpoint `/classificar` utilizando o método POST.
- Recebimento de dados no formato JSON.
- Validação do campo `descricao`.
- Classificação por palavras-chave.
- Retorno da descrição e categoria em JSON.
- Resposta HTTP 200 para requisições válidas.
- Resposta HTTP 400 para descrições inválidas ou vazias.

### Containerização com Docker

- Criação do `Dockerfile`.
- Utilização da imagem base `python:3.13-slim`.
- Instalação automática das dependências.
- Configuração do `.dockerignore`.
- Execução da API com Gunicorn 23.0.0.
- Comunicação HTTP entre Windows e container Linux.
- Construção e execução da imagem testadas localmente.

## 📂 Categorias atuais

| Categoria | Palavras-chave |
|---|---|
| Problemas de Acesso | senha, login, acess, bloquead, permissão |
| Problemas de Impressão | impressora, imprimir, cartucho, toner |
| Outros Problemas | Descrições não reconhecidas pelas regras |

## 🛠️ Tecnologias utilizadas

- Python
- Flask 3.1.3
- Gunicorn 23.0.0
- API REST
- HTTP e JSON
- Docker e Docker Desktop
- WSL 2 com Ubuntu
- Git e GitHub
- Visual Studio Code
- PowerShell

## 📁 Estrutura do projeto

```text
P0-classificador-Chamados/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
├── api.py
├── main.py
├── requirements.txt
├── casos_de_teste.md
└── testes/
    ├── teste_get.py
    ├── teste_post.py
    └── testes_erros.py
```

## ▶️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/CrisleiKeliJenuino/P0-classificador-Chamados.git
```

### 2. Acesse a pasta

```bash
cd P0-classificador-Chamados
```

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4. Execute a aplicação de terminal

```bash
python main.py
```

Digite a descrição de um problema técnico quando solicitado.

### 5. Execute a API Flask

```bash
python api.py
```

A API ficará disponível em:

`http://127.0.0.1:5000`

Essa forma de execução utiliza o servidor de desenvolvimento do Flask.

### 6. Teste a API pelo PowerShell

Em outro terminal PowerShell:

```powershell
$dados = @{
    descricao = "Esqueci minha senha"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/classificar" -Method POST -Body $dados -ContentType "application/json; charset=utf-8"
```

Exemplo de resposta:

```json
{
  "categoria": "Problemas de Acesso",
  "descricao": "Esqueci minha senha"
}
```

## 🐳 Executando com Docker

É necessário ter o Docker instalado e em funcionamento.

### 1. Construir a imagem

Na pasta principal do projeto:

```powershell
docker build -t classificador-p0:latest .
```

### 2. Executar o container

```powershell
docker run --rm -p 5001:5000 classificador-p0:latest
```

A API ficará acessível pelo Windows em:

`http://localhost:5001/classificar`

O container utiliza o **Gunicorn** para executar a aplicação Flask na porta 5000.

### 3. Testar a classificação

Em outro terminal PowerShell:

```powershell
$dados = @{
    descricao = "Minha impressora não está funcionando"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5001/classificar" -Method POST -Body $dados -ContentType "application/json; charset=utf-8"
```

Resposta obtida nos testes:

```json
{
  "categoria": "Problemas de Impressão",
  "descricao": "Minha impressora não está funcionando"
}
```

### 4. Verificar o tamanho da imagem

```powershell
docker images classificador-p0
```

Resultado registrado em 23/11/2026:

| Indicador | Resultado |
|---|---|
| Imagem | classificador-p0:latest |
| Servidor | Gunicorn 23.0.0 |
| Uso de disco | 200 MB |
| Content size | 48,7 MB |
| Limite de referência | 1024 MB |
| Situação | Dentro do limite |

Os valores podem variar conforme a versão da imagem e o ambiente Docker.

## 🧪 Testes realizados

| Teste | Resultado |
|---|---|
| Reconhecimento de chamado sobre login | Passou |
| Reconhecimento de chamado sobre impressora | Passou |
| Reconhecimento de palavra digitada incorretamente | Falhou |
| Requisição POST com descrição válida | Passou |
| Validação de descrição vazia via API | Passou |
| Construção da imagem Docker | Passou |
| Inicialização da API no Docker com Flask | Passou |
| Inicialização da API com Gunicorn | Passou |
| Requisição POST para API no Docker com Gunicorn | Passou |

Os registros iniciais estão disponíveis em `casos_de_teste.md`.

Os testes de Docker e Gunicorn foram realizados manualmente pelo terminal.

## 📈 Evolução do projeto

- [x] Etapa 1 — Entrada de dados e validação.
- [x] Etapa 2 — Classificação inicial com if, elif e else.
- [x] Etapa 3 — Separação de categoria e orientação.
- [x] Etapa 4 — Utilização de f-strings.
- [x] Etapa 5 — Organização das palavras-chave com listas e any().
- [x] Etapa 6 — Normalização do texto.
- [x] Etapa 7 — Organização do código em funções.
- [x] Etapa 8 — Instalação e configuração do Flask.
- [x] Etapa 9 — Desenvolvimento da primeira API REST.
- [x] Etapa 10 — Testes HTTP POST e validação de entrada.
- [x] Etapa 11 — Instalação do WSL 2 e Docker Desktop.
- [x] Etapa 12 — Criação e teste da imagem Docker.
- [x] Etapa 13 — Configuração do .dockerignore.
- [x] Etapa 14 — Configuração do Gunicorn.
- [x] Etapa 15 — Teste da API com Gunicorn dentro do Docker.
- [ ] Etapa 16 — Integração com o LLM da Softex.
- [ ] Etapa 17 — Testes da integração com LLM.
- [ ] Etapa 18 — Preparação da imagem para entrega.
- [ ] Etapa 19 — Publicação e validação no portal, conforme os requisitos oficiais.
- [ ] Etapa 20 — Revisão final da documentação e dos testes.

## ⚠️ Limitações atuais

O classificador ainda utiliza regras baseadas em palavras-chave.

A aplicação pode não reconhecer erros de digitação, termos ambíguos ou descrições sem palavras cadastradas.

A API ainda não está integrada a um modelo de linguagem (LLM).

As orientações iniciais são fornecidas pela aplicação de terminal. A API retorna a descrição e a categoria.

A imagem Docker foi construída e testada localmente, mas ainda não foi publicada no ambiente de entrega.

## 🔜 Próximos passos

- Conferir os requisitos oficiais do P0.
- Integrar a aplicação ao LLM disponibilizado pela Softex.
- Validar as respostas e implementar o tratamento de erros necessário.
- Testar novamente a aplicação no Docker após a integração.
- Preparar o arquivo de imagem para entrega no formato exigido.
- Revisar os testes e finalizar a documentação.

## 👩‍💻 Autora

**Crislei Keli Jenuino**

Projeto educacional desenvolvido durante o programa Trends IA, com foco no aprendizado prático de Python, APIs REST, inteligência artificial, Git, GitHub e Docker.