def descricao_vazia(descricao):
    return descricao.strip() == ""

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

    descricao = input("Como posso ajudá-lo? Digite o problema encontrado: ")
if descricao_vazia(descricao):
    print("Por favor, descreva o problema encontrado para que possamos ajudá-lo.")
else:
    categoria = classificar_chamado(descricao)
    print("Problema encontrado:", descricao)
    if categoria == "Problemas de Acesso":
        orientacao = "Verifique se você está digitando a senha corretamente. Se você esqueceu sua senha, utilize a opção de recuperação de senha no sistema. Caso o problema persista, entre em contato com o suporte técnico."
    elif categoria == "Problemas de Impressão":
        orientacao = "Verifique se a impressora está ligada e conectada corretamente ao computador. Se o problema persistir, entre em contato com o suporte técnico."
    else:
        categoria = "Outros Problemas"
        orientacao = "Para problemas não identificados, por favor, forneça mais detalhes ou entre em contato com o suporte técnico."
        
    print(f"Categoria: {categoria}")
    print(f"Orientação: {orientacao}")
