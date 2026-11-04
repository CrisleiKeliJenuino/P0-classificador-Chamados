descricao = input("Como posso ajudá-lo? Digite o problema encontrado: ")
if descricao.strip() == "":
    print("Por favor, descreva o problema encontrado para que possamos ajudá-lo.")
else:
    print("Problema encontrado:", descricao)
    if "senha" in descricao.lower() or "login" in descricao.lower():
        print("Categoria: Acesso e Senhas. Por favor, tente redefinir sua senha ou entre em contato com o suporte técnico.")    
    elif "impressora" in descricao.lower():
        print("Problema relacionado à impressora. Verifique se a impressora está ligada e conectada corretamente ao computador. Se o problema persistir, entre em contato com o suporte técnico.")
    else:
        print("Problema não identificado. Por favor, forneça mais detalhes ou entre em contato com o suporte técnico.")    
