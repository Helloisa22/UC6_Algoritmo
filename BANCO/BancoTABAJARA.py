# BANCO Tabajara
import pandas as pd
import os

# Variaveis
nome_cliente = ""
tipo_conta = ""
numero_conta = 0
cpf = 0
agencia = 0
extrato_bancario = 0
deposito = 0
saque = 0

dados_cliente = {
    "nome_cliente": [nome_cliente],
    "cpf": [cpf],
    "tipo_conta": [tipo_conta],
    "numero_conta": [numero_conta],
    "agencia": [agencia],
    "extrato_bancario": [extrato_bancario],
    "deposito": [deposito],
    "saque": [saque]
}

#Melhor opção é criar uma lista vazia e adicionar com append meu dicionario toda vez que executar o codigo ele cria uma lista com base no meu dicionario
lista_clientes = []
lista_clientes.append(dados_cliente)

caminho_excel = "BANCO\Banco_Tabajara.xlsx"

print("================================================")
print("                 BANCO TABAJARA")
print("                                 ")
print("                 Escolha uma opção")
print("                 1 - Criar conta")
print("                 2 - Acessar conta")
print("================================================\n")
opcao = int(input("R: "))


# 1 - Criar conta > Solicitar ao usuario as seguintes informações:
# - nome_cliente
# - cpf
# - tipo_conta
if opcao == 1:
    # dados_cliente["nome_cliente"] = input("Nome completo: ")
    # dados_cliente["cpf"] = input("CPF: ")
    # dados_cliente["tipo_conta"] = input("Tipo da conta que deseja criar:  ")
    
    if not os.path.exists(caminho_excel):
        dados_cliente["nome_cliente"] = str(input("Nome completo: "))
        dados_cliente["cpf"] = int(input("CPF: "))
        dados_cliente["tipo_conta"] = str(input("Tipo da conta que deseja criar:  "))

        dados_cliente["numero_conta"] = 0
        dados_cliente["agencia"] = 400
        dados_cliente["extrato_bancario"] = 0
        dados_cliente["deposito"] = 0
        dados_cliente["saque"] = 0

        excel = pd.DataFrame(lista_clientes)

        excel.to_excel(caminho_excel, index=False)

    else:
        dados_cliente["nome_cliente"] = input("Nome completo: ")
        dados_cliente["cpf"] = input("CPF: ")
        dados_cliente["tipo_conta"] = input("Tipo da conta que deseja criar:  ")
        
        # - numero_conta = Será gerada de forma sequencial começando do 0 até 100
        # for valor in lista_clientes:
        #     valor["numero_conta"] += 1
        
        # # - agencia = será gerado de forma sequencial começando do 400 até 700
        # for valor in lista_clientes:
        #     valor["agencia"] += 1

        excel = pd.read_excel(caminho_excel)

        nova_linha = len(excel)

        dados_cliente["numero_conta"] += 1
        dados_cliente["agencia"] += 1

        excel.loc[nova_linha, "nome_cliente"] = dados_cliente["nome_cliente"]
        excel.loc[nova_linha, "cpf"] = dados_cliente["cpf"]
        excel.loc[nova_linha, "tipo_conta"] = dados_cliente["tipo_conta"]
        excel.loc[nova_linha, "numero_conta"] = dados_cliente["numero_conta"]
        excel.loc[nova_linha, "agencia"] = dados_cliente["agencia"]

        excel.to_excel(caminho_excel)

else:
    print("Erro")