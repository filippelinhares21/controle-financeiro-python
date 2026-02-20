from financeiro import receitas, despesas
from datetime import datetime

def validar_data(data_str):
    try:
        return datetime.strptime(data_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    
def validar_valor(valor_str):
    try:
        valor = float(valor_str)
        if valor < 0:
            return None
        return valor
    except ValueError:
        return None
    
def filtrar_periodo(lista, data_inicio, data_fim):
    inicio = datetime.strptime(data_inicio, "%Y-%m-%d").date()
    fim = datetime.strptime(data_fim, "%Y-%m-%d").date()

    itens_filtrados = [
        item for item in lista
        if inicio <= datetime.strptime(item[2], "%Y-%m-%d").date() <= fim
    ]

    itens_filtrados.sort(key=lambda x: x[2])

    return itens_filtrados

def relatorio_periodo(data_inicio, data_fim):
    lista_receitas = receitas.listar_receitas()
    lista_despesas = despesas.listar_despesas()

    receitas_filtradas = filtrar_periodo(lista_receitas, data_inicio, data_fim)
    despesas_filtradas = filtrar_periodo(lista_despesas, data_inicio, data_fim)

    total_receitas = sum(r[0] for r in receitas_filtradas)
    total_despesas = sum(d[0] for d in despesas_filtradas)

    saldo = total_receitas - total_despesas

    media_receitas = total_receitas / len(receitas_filtradas) if receitas_filtradas else 0
    media_despesas = total_despesas / len(despesas_filtradas) if despesas_filtradas else 0

    return {
        "receitas": receitas_filtradas,
        "despesas": despesas_filtradas,
        "total_receitas": total_receitas,
        "total_despesas": total_despesas,
        "saldo": saldo,
        "media_receitas": media_receitas,
        "media_despesas": media_despesas
    }


