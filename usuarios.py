def validar_email(email):
    """
    Valida um endereço de e-mail com base nos critérios estritos do projeto.
    """
    # 1. Rejeitar None e garantir que é uma string
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
        
    # 6. Domínio com duas partes não vazias (ex: empresa.com)
    partes_dominio = dominio.split(".")
    if len(partes_dominio) != 2 or not partes_dominio[0] or not partes_dominio[1]:
        return False
        
    return True