def criar_cliente(nome, nome_conta, numero_conta, cpf, agencia):
    return {
        "nome_cliente": nome,
        "nome_conta": nome_conta,
        "numero_conta": numero_conta,
        "cpf": cpf,
        "agencia": agencia,
    }

cliente1 = criar_cliente("Heloisa","Corrente",12466, 99999999999, 123)

print(cliente1)