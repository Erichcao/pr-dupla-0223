from usuarios import validar_email

def test_valido():
    assert validar_email("ana@exemplo.com") is True

def test_sem_arroba():
    assert validar_email("://exemplo.com") is False

# REMOVIDO O (self) DAQUI PARA BAIXO:

def test_none():
    assert validar_email(None) is False

def test_dominio_incompleto():
    assert validar_email("ana@") is False

def test_usuario_vazio():
    assert validar_email("@exemplo.com") is False

# DICA: Aproveite para colocar o caso do seu revisor (.com.br) para testar!
def test_dominio_com_br():
    assert validar_email("ana@empresa.com.br") is True
