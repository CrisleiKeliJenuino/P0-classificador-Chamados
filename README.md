
# 🖥️ Classificador Inteligente de Chamados de TI

Projeto desenvolvido durante o **Trends IA — P0: Primeiro Fluxo com LLM**, com o objetivo de criar uma aplicação Python para classificação de chamados de suporte técnico, evoluindo até a integração com um modelo de linguagem (LLM) via API REST.

## 🎯 Objetivo

Desenvolver um sistema capaz de receber a descrição de um problema técnico, identificar sua categoria e fornecer uma orientação inicial ao usuário.

O projeto começou como uma aplicação de terminal e evoluiu para uma API REST utilizando Flask.

## 🚀 Funcionalidades implementadas

### Aplicação de terminal — main.py

- Entrada de chamados pelo terminal.
- Validação de descrições vazias.
- Normalização do texto para letras minúsculas.
- Identificação de palavras-chave utilizando listas e `any()`.
- Classificação com `if`, `elif` e `else`.
- Exibição da categoria e orientação ao usuário.

### API REST — api.py

- Criação de uma API utilizando Flask.
- Endpoint `/classificar` com método POST.
- Recebimento de dados no formato JSON.
- Extração e validação do campo `descricao`.
- Classificação de chamados por palavras-chave.
- Retorno da descrição e categoria em JSON.
- Resposta HTTP 200 para requisições válidas.
- Resposta HTTP 400 para descrições inválidas ou vazias.

## 📂 Categorias atuais

| Categoria | Palavras-chave |
|---|---|
| Problemas de Acesso | senha, login, acess, bloquead, permissão |
| Problemas de Impressão | impressora, imprimir, cartucho, toner |
| Outros Problemas | Descrições não reconhecidas pelas regras |

## 🛠️ Tecnologias utilizadas

- Python
- Flask 3.1.3
- API REST
- HTTP e JSON
- Git e GitHub
- Visual Studio Code
- PowerShell
- WSL 2 com Ubuntu
- Docker Desktop

## ▶️ Como executar

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

Caso o arquivo `requirements.txt` ainda não esteja presente, instale o Flask com:

```bash
python -m pip install Flask==3.1.3
```

### 4. Execute a aplicação de terminal

```bash
python main.py
```

Digite a descrição de um problema técnico quando solicitado.

### 5. Execute a API REST

```bash
python api.py
```

A API ficará disponível localmente em:

`http://127.0.0.1:5000`

### 6. Teste a API pelo PowerShell

Em outro terminal PowerShell, execute:

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

## 🧪 Testes realizados

| Teste | Resultado |
|---|---|
| Reconhecimento de chamado sobre login | Passou |
| Reconhecimento de chamado sobre impressora | Passou |
| Reconhecimento de palavra digitada incorretamente | Falhou |
| Requisição POST com descrição válida | Passou |
| Validação de descrição vazia via API | Passou |

Os registros detalhados estão disponíveis em `casos_de_teste.md`.

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
- [ ] Etapa 12 — Criar e testar a imagem Docker.
- [ ] Etapa 13 — Integrar a aplicação com o LLM da Softex.
- [ ] Etapa 14 — Realizar testes da integração com LLM.
- [ ] Etapa 15 — Publicar e validar a aplicação no portal.
- [ ] Etapa 16 — Revisar documentação e testes finais.

## ⚠️ Limitações atuais

O classificador ainda utiliza regras baseadas em palavras-chave.

A aplicação pode não reconhecer erros de digitação, termos ambíguos ou descrições que não contenham palavras cadastradas.

A API REST já está funcionando localmente, mas ainda não possui integração com um LLM.

O ambiente Docker está instalado, porém a imagem da aplicação ainda não foi construída ou publicada.

As orientações iniciais são fornecidas pela aplicação de terminal. A API atual retorna a descrição e a categoria.

## 🔜 Próximos passos

- Preparar a aplicação para execução em container.
- Criar o Dockerfile e testar a imagem localmente.
- Integrar o endpoint interno do LLM da Softex.
- Validar respostas e tratamento de erros.
- Gerar a imagem TAR para envio ao portal.
- Finalizar os testes e a documentação.

## 👩‍💻 Autora

**Crislei Keli Jenuino**

Projeto educacional desenvolvido durante o programa Trends IA, com foco no aprendizado prático de Python, APIs REST, inteligência artificial, Git, GitHub e Docker.
