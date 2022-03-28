'''
Em Python é considerado uma string sempe que estiver entre aspas simples, duplas, triplas
'''

nome = 'marcelo vinicius'
print(nome.upper())
print(nome.lower())
print(nome.__len__()) #retorna a quantidade de caracteres
print(nome.split()) #transforma numa lista de strings, dividindo as palavras
print(nome[0:6]) #imprime um intervalo/chamado Slice de string
print(nome.split()[1]) #retorna a string da lista em relação a posição [] informada
print(nome[::-1]) #inverte a ordem das letras
print(nome.replace('i', 'a')) #troca a letra da primeira posição pela segunda dentro da variável

