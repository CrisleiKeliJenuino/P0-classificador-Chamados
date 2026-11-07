
# 🖥️ Classificador Inteligente de Chamados de TI

Projeto desenvolvido durante o **Trends IA — P0: Primeiro Fluxo com LLM**, com o objetivo de criar uma aplicação em Python para classificação de chamados de suporte técnico, evoluindo até a integração com uma LLM via API REST.

## 🎯 Objetivo

Desenvolver um sistema capaz de receber a descrição de um problema técnico, identificar sua categoria e fornecer uma orientação inicial ao usuário.

## 🚀 Funcionalidades implementadas

- Entrada de chamados pelo terminal.
- Validação de descrições vazias.
- Normalização do texto para letras minúsculas.
- Identificação de palavras-chave utilizando listas e `any()`.
- Classificação de chamados com `if`, `elif` e `else`.
- Exibição da categoria e da orientação em linhas separadas.

## 📂 Categorias atuais

| Categoria | Palavras-chave |
|---|---|
| Problemas de Acesso | senha, login, acess, bloquead, permissão |
| Problemas de Impressão | impressora, imprimir, cartucho, toner |
| Outros Problemas | Descrições não reconhecidas pelas regras |

## 🛠️ Tecnologias utilizadas

- Python
- Git e GitHub
- Visual Studio Code

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/CrisleiKeliJenuino/P0-classificador-Chamados.git
```

### 2. Acesse a pasta

```bash
cd P0-classificador-Chamados
```

### 3. Execute o programa

```bash
python main.py
```

Digite a descrição de um problema técnico quando solicitado.

## 📈 Evolução do projeto

- [x] Etapa 1 — Entrada de dados e validação.
- [x] Etapa 2 — Classificação inicial com `if`, `elif` e `else`.
- [x] Etapa 3 — Separação de categoria e orientação em variáveis.
- [x] Etapa 4 — Utilização de f-strings para apresentar resultados.
- [x] Etapa 5 — Organização das palavras-chave com listas e `any()`.
- [x] Etapa 6 — Normalização da descrição e redução de código repetido.
- [ ] Etapa 7 — Organização do código em funções.
- [ ] Etapa 8 — Integração com uma LLM via API REST.
- [ ] Etapa 9 — Testes e documentação final.

## ⚠️ Limitações atuais

O sistema utiliza regras baseadas em palavras-chave e ainda não possui integração com inteligência artificial.

Algumas descrições podem ser classificadas incorretamente quando contêm palavras ambíguas ou termos não cadastrados.

A integração com uma LLM está planejada para melhorar a interpretação dos chamados.

## 👩‍💻 Autora

**Crislei Keli Jenuino**

Projeto educacional desenvolvido durante o programa Trends IA, com foco no aprendizado prático de Python, Git, GitHub e integração com APIs.
