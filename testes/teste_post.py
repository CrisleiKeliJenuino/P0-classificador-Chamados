import urllib.request
import json

url = "https://jsonplaceholder.typicode.com/posts"

dados = {
    "title": "Teste de chamado de TI",
    "body": "Não consigo acessar meu e-mail",
    "userId": 1
}

dados_json = json.dumps(dados).encode("utf-8")

requisicao = urllib.request.Request(
    url,
    data=dados_json,
    headers={"Content-Type": "application/json"},
    method="POST"
)

resposta = urllib.request.urlopen(requisicao, timeout=10)

print(resposta.status)

conteudo = resposta.read().decode("utf-8")
print(conteudo)

resultado = json.loads(conteudo)
print(resultado["id"])