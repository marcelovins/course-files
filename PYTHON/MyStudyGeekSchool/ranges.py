# Forma 1 (Define-se apenas o tamanho da contagem a partir de 0 e até o final -1)
for num in range(11):
    print(num)

print('\n')
# Forma 2 (O usuário define o intervalo inicial e final)
for num in range(4, 11):
    print(num)

print('\n')
# Forma 3 (Define um intervalo para a contagem)
for num in range(2, 11, 2):
    print(num)

print('\n')
# Forma 4 (Forma inversa)
for num in range(10, -1, -2):
    print(num)

# Forma 5 (Converter um range para uma lista)
lista = list(range(10))
print(lista)
