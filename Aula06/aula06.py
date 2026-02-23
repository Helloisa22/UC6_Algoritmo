"""
 S E N A C"
 0 1 2 3 4
-5 -4 -3 -2 -1
"""

texto1 = "SENAC"
print(texto1[0])
print(texto1[3])
print(texto1[-1])

# FUNCAO len()
texto2 = "Ola Pa"

print(len(texto2))

# FUNCAO MAI/MIN
texto3 = "ola mundinho"
print(texto3.upper())

texto4 = "OLA MUNDAO"
print(texto4.lower())

print(texto3.capitalize())

print(texto3.title())

texto5 = "Python"
"""
P Y T H O N
0 1 2 3 4 5
"""
print(texto5[0:3])
print(texto5[0:5])

# REPLACE
texto6 = "Hoje é aula da Heloisa"
novo_texto = texto6.replace("da Heloisa", "do José Milton")
print(novo_texto)

# ESPACO EM BRANCO
texto7 = "        Ola Mundo     "
print(texto7.strip() + "String") # remove direita e esquerda
print(texto7.lstrip() + "String") # remove esquerda
print(texto7.rstrip() + "String") # remove direita

# METODOS STRING
texto8 = "A Pulei carnaval, mas hoje estou estudando."
print("CARNAVAL" in texto8)
# Case sensitive = Sensivel a letras maiusculas e minusculas

print(texto8.find("estudando")) # 31
print(texto8[31]) # e

print(texto8.count("a"))

texto9 = "Eu amo Java"
print(texto9.startswith("Eu"))
print(texto9.endswith("va"))