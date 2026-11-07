descricao = input("Como posso ajudá-lo? Digite o problema encontrado: ")
if descricao.strip() == "":
    print("Por favor, descreva o problema encontrado para que possamos ajudá-lo.")
else:
    descricao_lower = descricao.lower()
    print("Problema encontrado:", descricao)
    palavras_acesso = ["senha", "login", "acess", "bloquead","permissão"]
    palavras_impressao = ["impressora", "imprimir", "cartucho", "toner"]
    if any(palavra in descricao_lower for palavra in palavras_acesso):
        categoria = "Problemas de Acesso"
        orientacao = "Verifique se você está digitando a senha corretamente. Se você esqueceu sua senha, utilize a opção de recuperação de senha no sistema. Caso o problema persista, entre em contato com o suporte técnico."
    elif any(palavra in descricao_lower for palavra in palavras_impressao):
        categoria = "Problemas de Impressão"
        orientacao = "Verifique se a impressora está ligada e conectada corretamente ao computador. Se o problema persistir, entre em contato com o suporte técnico."
    else:
        categoria = "Outros Problemas"
        orientacao = "Para problemas não identificados, por favor, forneça mais detalhes ou entre em contato com o suporte técnico."
        
    print(f"Categoria: {categoria}")
    print(f"Orientação: {orientacao}")
