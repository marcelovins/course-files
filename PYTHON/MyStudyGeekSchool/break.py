# Exemplo 1
for numero in range(1, 10):
    if numero == 6:
        break # Usamos o break para sair do loop
    else:
        print(numero)
print('vc saiu do loop!\n\n')

# Exemplo 2
while True:
    comando = input('digite sair para sair:')
    if comando == 'sair':
        break

