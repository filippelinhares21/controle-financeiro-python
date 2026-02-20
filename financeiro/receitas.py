import os
from datetime import date

ARQUIVO = "dadosreceitas.txt"

def adicionar_receita(valor, descricao, data=None):
    if data is None:
        data = date.today().isoformat()
    
    if not os.path.exists("dados"):
        os.makedirs("dados")
    
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo_receitas:
        arquivo_receitas.write(f"{valor},{descricao},{data}\n")

def listar_receitas():
    receitas_lidas = []
    
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo_receitas:
            for linha in arquivo_receitas:
                valor, descricao, data = linha.strip().split(",")
                receitas_lidas.append((float(valor), descricao, data))
    
    return receitas_lidas