import re
from financeiro import receitas, despesas, utils

def pausar():
    input("\nPressione Enter para voltar ao menu...")

def pedir_data(mensagem):
    while True:
        data = input(mensagem).strip()
        if utils.validar_data(data):
            return data
        else:
            print("Data inválida! Use o formato YYYY-MM-DD.")
            input("Pressione Enter para tentar novamente...")

def pedir_valor(mensagem):
    while True:
        valor_input = input(mensagem).strip()
        regex_brasil = r'^\d{1,3}(\.\d{3})*(,\d{1,2})?$'
        regex_internacional = r'^\d+(\.\d{1,2})?$'
    
        if re.match(regex_brasil, valor_input):
            valor_input = valor_input.replace(".", "").replace(",", ".")
        elif re.match(regex_internacional, valor_input):
            pass
        else:
            print("Valor inválido! Digite um número válido, ex: 1000,50 ou 1000.50")
            input("Pressione Enter para tentar novamente...")
            continue

        valor_validado = utils.validar_valor(valor_input)
        if valor_validado is not None:
            return valor_validado
        else:
            print("Valor inválido! Digite um número positivo.")
            input("Pressione Enter para tentar novamente...")

def menu():
    while True:
        print("\n=== Sistema de Controle Financeiro ===")
        print("1. Adicionar receita")
        print("2. Adicionar despesa")
        print("3. Relatório completo por período")
        print("4. Listar receitas por período")
        print("5. Listar despesas por período")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = pedir_valor("Valor: ")
            descricao = input("Descrição: ")
            data = pedir_data("Data (YYYY-MM-DD): ")
            
            receitas.adicionar_receita(valor, descricao, data)
            print("Dinheiro! Receita adicionada!")
            pausar()

        elif opcao == "2":
            valor = pedir_valor("Valor: ")
            descricao = input("Descrição: ")
            data = pedir_data("Data (YYYY-MM-DD): ")
           
            despesas.adicionar_despesa(valor, descricao, data)
            print("Gastou? Despesa adicionada!")
            pausar()

        elif opcao == "3":
            data_inicio = pedir_data("Data inicial (YYYY-MM-DD): ")
            data_fim = pedir_data("Data final (YYYY-MM-DD): ")

            if data_fim < data_inicio:
                print("Data final deve ser maior ou igual à inicial.")
                pausar()
                continue

            relatorio = utils.relatorio_periodo(data_inicio, data_fim)

            print(f"\nPeríodo: {data_inicio} até {data_fim}")
            print(f"Total Receitas: {relatorio['total_receitas']:.2f}")
            print(f"Total Despesas: {relatorio['total_despesas']:.2f}")
            print(f"Saldo: {relatorio['saldo']:.2f}")
            print(f"Média Receitas: {relatorio['media_receitas']:.2f}")
            print(f"Média Despesas: {relatorio['media_despesas']:.2f}")

            pausar()

        elif opcao == "4":
            data_inicio = pedir_data("Data inicial (YYYY-MM-DD): ")
            data_fim = pedir_data("Data final (YYYY-MM-DD): ")

            lista_receitas = utils.filtrar_periodo(
                receitas.listar_receitas(),
                data_inicio,
                data_fim
            )

            print("\nReceitas no período (mais antigo → mais novo):")
            for rec in lista_receitas:
                print(f"{rec[2]} - {rec[1]}: {rec[0]:.2f}")

            pausar()

        elif opcao == "5":
            data_inicio = pedir_data("Data inicial (YYYY-MM-DD): ")
            data_fim = pedir_data("Data final (YYYY-MM-DD): ")

            lista_despesas = utils.filtrar_periodo(
                despesas.listar_despesas(),
                data_inicio,
                data_fim
            )

            print("\nDespesas no período (mais antigo → mais novo):")
            for desp in lista_despesas:
                print(f"{desp[2]} - {desp[1]}: {desp[0]:.2f}")

            pausar()

        elif opcao == "6":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")
            pausar()


if __name__ == "__main__":
    menu()