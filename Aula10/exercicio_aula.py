import pandas as pd
nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
# Arquivo excel
dados = {
    "Nome": [nome],
    "Idade": [idade]
}

df = pd.DataFrame(dados)

df.to_excel("Aula10\cadastro.xlsx", index=False)


# Arquivo txt
# with open("Aula10\cadastro.txt", "a") as cadastro:
#     cadastro.write(nome + " - " + idade + "\n")
#     print("Cadastrado com sucesso!")