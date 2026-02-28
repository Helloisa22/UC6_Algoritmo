"""
dicionario {} -> Para acessar dados usamos o nome da chave
listas [] -> Para acessar dados usamos a posicao da lista
"""
# notas = [10, 8, 5, 10, True, 7, "Andre"]
# #         0  1  2   3    4   5     6

# notas.append("SENAC")
# print(notas)

# notas.insert(0, False)
# print(notas)

# # nova_lista = ["Olá mundo", 1980, 24.7]
# # nova_lista.extend(notas)
# # print(nova_lista)

# notas.remove(10)
# print(notas)
# notas.remove(True)
# print(notas)
# notas.remove("SENAC")
# print(notas)
# notas.remove("Andre")
# # O metodo remove e case sensitive


nomes_numeros = [390, "Adenilson", 19, "Anna", 45, "Iara", 390]
# POP
# nomes_numeros.pop()
# print(nomes_numeros)
# CLEAR
# print(nomes_numeros.clear())
# INDEX
print(nomes_numeros.index("Adenilson"))
print(nomes_numeros)

print(nomes_numeros.count(390))


numeros = [34, 45, 67, 89, 43, 44, 26, 58, 66, 33, 90]
# numeros.sort()
# print(numeros)
# REVERSE
numeros.reverse()
print(numeros)

nome = ["Adenilson", "Anna", "Beatriz", "Anne", "Bianca"]
# nome.sort()
# print(nome)
nome.reverse()
print(nome)