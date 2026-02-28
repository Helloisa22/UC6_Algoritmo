print("*")
usuario = {
    "nome": "",
    "notas": [0, 0, 0, 0, 0]
}

usuario["nome"] = input("Digite o seu nome: ")

i = 0
while i <= 4:
    usuario["notas"][i] = input("Digite a nota: ")
    i+=1

nota=0
for valor in usuario["notas"]:
    nota += valor