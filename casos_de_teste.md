
# Casos de Teste — Classificador de Chamados de TI

## 1. Testes de classificação

| Nº | Descrição | Categoria esperada | Resultado obtido | Situação |
|---|---|---|---|---|
| 01 | Minha impressra não imprime | Problemas de Impressão | Outros Problemas | Falhou |
| 02 | Minha impressora não imprime | Problemas de Impressão | Problemas de Impressão | Passou |
| 03 | Não consigo fazer login no sistema | Problemas de Acesso | Problemas de Acesso | Passou |

## 2. Testes da API REST — Flask

| Nº | Descrição do teste | Resultado esperado | Resultado obtido | Situação |
|---|---|---|---|---|
| 04 | Enviar chamado sobre senha via POST | HTTP 200 e categoria Problemas de Acesso | Categoria Problemas de Acesso retornada com sucesso | Passou |
| 05 | Enviar descrição vazia via POST | HTTP 400 e mensagem de validação | HTTP 400 e mensagem "Informe uma descrição válida." | Passou |

## 3. Erros encontrados durante o desenvolvimento

### Erro 01 — Importação do Flask
- Problema: utilização de `flash` em vez de `flask`.
- Solução: corrigida a importação da biblioteca.

### Erro 02 — Variável request não definida
- Problema: erro HTTP 500 causado pela ausência da importação de `request`.
- Solução: adicionada a importação correta.

### Erro 03 — Variável descricao não definida
- Problema: a API tentava classificar uma descrição antes de extrair seu valor do JSON.
- Solução: adicionada a leitura do campo `descricao` e sua validação.

## 4. Melhorias pendentes

- Melhorar o reconhecimento de palavras digitadas incorretamente.
- Ampliar as categorias de chamados de TI.
- Integrar o classificador com um LLM.
- Testar a aplicação em um container Docker.
- Validar a execução no ambiente da Softex.
