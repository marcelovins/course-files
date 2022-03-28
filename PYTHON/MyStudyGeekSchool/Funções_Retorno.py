'''
Funções com Retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)

print(f'Retonro de print: {ret_pr}')

Obs: Em Python, quando uma função não retorna nenhum valor, o retorno é None

Obs: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

Obs: Não preciisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos pasar a
execução da função para outras funções

Obs: Sobre a palavra reservada return

1- Ela finaliza a função, ou seja, ela sai da execução da função;
2- Podemos ter, em uma função, diferentes returns;
3- Podemos, em um função, retornar qualquer tipo de dado e até mesmo múltiplos valores;
'''

def quadrado_de_7():
    return 7*7
ret = quadrado_de_7()

print(f'\n\nRetorno {ret}\n')

def nova_funcao():
    variavel = True
    if variavel:  #deixa-se assim quando queremos o True - if variavel = True...
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(f' \n\n Retorna  == {nova_funcao()}\n\n')

# Criar função joga moeda

from random import random  # Retorna valores aleatórios entre 0 e 1

def joga_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

for n in range(5):
    print(joga_moeda())

    # Por usar o return não é necessário else, ele já é um valor a ser retornado e será executado no fim da linha
    # Evitar esse erro de codificação!



