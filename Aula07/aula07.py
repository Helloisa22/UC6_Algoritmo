#Dicionarios em Python

aluno = {
    # "chave" : valor
    "nome_aluno": "Pedro",
    "idade": 19,
    "nota": 8,
    "curso": "TÉCNICO EM INFORMÁTICA PARA INTERNET",
    # Array
    "Array": [30, True, "Texto"],
    #          0    1       2
    # Dicionario dentro de outro dicionario
    "endereco": {
        "cidade": "SP",
        "estado": "SP",
        "numero": 234
    }
}

# mostrar o dicionario principal
print(aluno)
# # retorna nome do aluno
# print(aluno["nome_aluno"])
# # retorna o array
# print(aluno["Array"])
# # retorna o endereco, estamos acessando um dicionario dentro de outro dicionario
# print(aluno["endereco"])
# # acessar apenas um unico campo do dicionario endereco
# print(aluno["endereco"]["estado"])
# # acessando campo especifico dentro de um array
# print(aluno["Array"][1])

#ALTERAR DADOS DO DICIONARIO
# aluno["idade"] = 20
# print(aluno["idade"])

#Alterar dados dentro de um array que está dentro do dicionario
# aluno["Array"][2] = 9
# print(aluno["Array"][2])
# print(aluno["Array"])

# Alterar dados do dicionario endereco que esta dentro do dicionario aluno
# Sempre que precisar acessar uma chave dentro de um dicionario usaremos colchetes
# aluno["endereco"]["cidade"] = "São Paulo"
# print(aluno["endereco"])
# print(aluno["endereco"]["cidade"])

# ADICIONAR UM NOVO CAMPO
# aluno["periodo"] = "Noturno"
# print(aluno)

# Deletar uma informação
# del aluno["idade"]
# # deletar mais de uma informacao na mesma linha
# del aluno["endereco"], aluno["curso"]
# print(aluno)

# Percorrer um dicionario usando laco de repeticao para retornar as chaves
# for chave in aluno:
#     print(chave)

# Percorrer um dicionario usando laco de repeticao para retornar as valores
# for valor in aluno.values():
#     print(valor)

# Percorrer um dicionario e retornar chave e valor
# for chave, valor in aluno.items():
#     print(chave, ":", valor)

nota = {
    "nota1": "",
    "nota2": "",
    "nota3": ""
}