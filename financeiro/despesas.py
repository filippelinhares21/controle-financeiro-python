import os
from datetime import date

ARQUIVO = "dadosdespesas.txt"

def adicionar_despesa(valor, descricao, data=None):
    if data is None:
        data = date.today().isoformat()
    
    if not os.path.exists("dados"):
        os.makedirs("dados")
    
    with open(ARQUIVO, "a", encoding="utf-8") as arquivo_despesas:
        arquivo_despesas.write(f"{valor},{descricao},{data}\n")

def listar_despesas():
    despesas_lidas = []
    
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo_despesas:
            for linha in arquivo_despesas:
                valor, descricao, data = linha.strip().split(",")
                despesas_lidas.append((float(valor), descricao, data))
    
    return despesas_lidas