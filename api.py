from flask import Flask, request, jsonify

app = Flask(__name__)

def classificar_chamado(descricao):
    descricao_lower = descricao.lower()

    palavras_acesso = ["senha", "login", "acess", "bloquead", "permissão"]
    palavras_impressao = ["impressora", "imprimir", "cartucho", "toner"]

    if any(palavra in descricao_lower for palavra in palavras_acesso):
        return "Problemas de Acesso"    
    elif any(palavra in descricao_lower for palavra in palavras_impressao):
        return "Problemas de Impressão"
    else:
        return "Outros Problemas"


@app.route('/classificar', methods=['POST'])
def classificar():
    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({
            "erro": "Dados inválidos. Envie um JSON válido."
        }), 400

    descricao = dados.get("descricao")

    if not isinstance(descricao, str) or not descricao.strip():
        return jsonify({
            "erro": "Informe uma descrição válida."
        }), 400

    categoria = classificar_chamado(descricao)

    return jsonify({
        "descricao": descricao,
        "categoria": categoria
    }), 200

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)