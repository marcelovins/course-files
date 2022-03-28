# Iterando em uma string
nome = 'marcelo'
lista = [1, 2, 3, 8, 7, 2, 9]
numeros = range(1, 10)

for letra in nome:
    print(letra)

# Iterando em uma lista

for numero in lista:
    print(numero)

# Iterando sobre um range

print('\n')
for numero in range(1, 10):
    print(numero)

# Quando não precisamos de um valor, podemos descartá-lo utilizando um underline
print('\n')
for indice, letra in enumerate(nome):
    print(letra)

# Enumerate cria indices Ex: ((0, 'm'), (1, 'a'), (2, 'r'), (3, 'c') ...)

for valor in enumerate(nome):
    print(valor)
# Ele irá printar o enumerate
# Se eu colocasse valor[1] ele traria somente a letra, se valor[0] traria a posição (1,2,3...)

# definindo loop pelo usuário
print('\n')
'''qtd = int(input('Quantas vezes esse loop deve rodar? ')) #coloquei assim pra não rodar toda hora
for n in range(1, qtd+1):
    print(f'imprimindo {n}')'''

""" O Python coloca \n por default em sua execução, se eu quiser imprimir 
sem isso eu devo usar o end=''"""
print('\n\n')
for letra in nome:
    print(letra, end='')

print('\n\n')
# Quando vc aperta Ctl+click na função o Pycharm abre o documento explicativo da função (builtins.py)

# Tabela de emojis unicode (procurar no google para usar)
# Original = U+1F60D
# Modificado para Python = U0001F60D

for num in range(1, 10):
    print('\U0001F60D'* num) # É possível concatenar strings com operadores matemáticos


