import urllib.request
import json
import urllib.error

url = "https://jsonplaceholder.typicode.com/todos/999999"

try:
    resposta = urllib.request.urlopen(url, timeout=10)
except urllib.error.HTTPError as erro:
    print("Erro HTTP:", erro.code)
else: 
    print("Requisição realizada com sucesso!")

    print(resposta.status)

dados = json.loads(resposta.read().decode("utf-8"))

print(dados["title"])

if dados["completed"] == False:
    print("A Tarefa ainda está pendente")
else:
    print("A Tarefa já foi concluída")

print(type(dados["completed"]))