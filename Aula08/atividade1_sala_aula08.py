"""
Crie uma lista vazia chamada compras
Peça ao usuário para digitar 3 itens
Adicione cada item na lista
Mostre todos os itens da lista ao final
"""
# Laço de repetição
# Metodo para manipular lista
# Lista

# Crie uma lista vazia chamada compras
lista_compra = []

for i in range(3):
    # Peça ao usuário para digitar 3 itens
    item = input("Digite um item: ")
    # Adicione cada item na lista
    lista_compra.append(item)

print("Sua lista de compras: ")
# Mostre todos os itens da lista ao final
for valor in lista_compra:
    print("-",valor)