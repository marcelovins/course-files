'''
A diferença do While é que ele utiliza uma expressão booleana, diferente do for que utiliza na maioria um range
O bloco while será executado até que a expressão booleana seja falsa, enquanto verdadeiro ele executa!
'''
# Exemplo 1
numero = 1
while numero < 10:
    print(numero)
    numero += 1

# Em um loop while é importante o critério de parada para não gerar um loop infinito. Alguns softwares usam loop infinito.

# Exemplo 2
resposta = ''
while resposta != 'sim':
    resposta = input('Já acabou, Marcelo?')

print('\nParabéns! Você terminou a tarefa!\n')

