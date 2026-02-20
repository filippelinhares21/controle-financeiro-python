# 💰📊 Sistema de Controle Financeiro em Python

Projeto em Python para controle de receitas e despesas pessoais, com foco em **análise de períodos personalizados**. Permite registrar valores, datas e descrições, e gerar relatórios completos de saldo e médias em qualquer intervalo definido pelo usuário.

---

## 🔹 Funcionalidades

- Adicionar **receitas** e **despesas** com:
  - Valor (aceita vírgula ou ponto como decimal)
  - Descrição
  - Data (YYYY-MM-DD)
- Consultar **saldo total** em um período específico
- Calcular **média de receitas e despesas** dentro de um período
- Listar **receitas e despesas em ordem cronológica** no período selecionado
- Períodos personalizáveis: escolha **data inicial e final**, podendo analisar um intervalo específico definido pelo usuário
- Validação de entradas para evitar datas ou valores incorretos

---

## 🔹 Exemplo de uso do menu
=== Sistema de Controle Financeiro ===

1. Adicionar receita
2. Adicionar despesa
3. Relatório completo por período
4. Listar receitas por período
5. Listar despesas por período
6. Sair

- O usuário escolhe uma opção digitando o número correspondente.  
- Ao adicionar receita/despesa, digita valor, descrição e data.  
- Para relatórios, define **data inicial e final**, e o programa calcula automaticamente:
   - Total de receitas e despesas  
   - Saldo final  
   - Média de receitas e despesas  
   - Listagem cronológica de receitas e despesas

---

## 🔹 Como executar

1. Clone o repositório:
git clone https://github.com/filippelinhares21/controle-financeiro-python.git

2. Entre na pasta do projeto:
cd "Controle Financeiro"

3. Execute o programa:
python main.py

---

## 🔹 Observações importantes

- Valores podem ser digitados com vírgula ou ponto como decimal (1000,50 ou 1000.50)
- Datas devem ser no formato YYYY-MM-DD (ex: 01 de fevereiro de 2025 se escreve 2025-02-01)
- O programa não fecha após mensagens de erro; sempre retorna para o menu principal



AUTOR: FILIPPE LINHARES
https://github.com/filippelinhares21




