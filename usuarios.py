def validar_email(email):
    """
    Valida um endereço de e-mail com base nos critérios do projeto,
    suportando domínios internacionais e locais (como .com.br).
    """
    # 1. Rejeitar explicitamente None e garantir que é uma string
    if email is None or not isinstance(email, str):
        return False
        
    # 2. Não pode conter espaços comuns
    if " " in email:
        return False
        
    # 3. Conter exatamente um @
    if email.count("@") != 1:
        return False
        
    usuario, dominio = email.split("@")
    
    # 4. Ter parte anterior ao @ não vazia
    if not usuario:
        return False
        
    # 5. Rejeitar domínio terminado em ponto
    if dominio.endswith("."):
        return False
        
    # 6. O domínio precisa ter pelo menos um ponto para separar as partes
    if "." not in dominio:
        return False
        
    # 7. Garantir que NENHUMA das partes do domínio esteja vazia
    # Isso resolve casos como "ana@.com", "ana@empresa..com" ou "ana@empresa."
    partes_dominio = dominio.split(".")
    for parte in partes_dominio:
        if not parte:  # Se qualquer parte for vazia "", rejeita
            return False
            
    return True
