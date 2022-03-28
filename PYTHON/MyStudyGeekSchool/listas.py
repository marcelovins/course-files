'''
Listas em python funcionam como vetores/matrizes/arrays, com a diferença de serem dinâmicos e de podermos colocar
vários tipos de dados
As listas em PYthon são representadas por colchete
'''

lista1 = [2, 5, 6, 8, 3, 1, 2, 10, 1, 2]
lista2 = ['k', 2, 9, 'G', 25]
lista3 = []
lista4 = list(range(11))
lista5 = list('geek university')
'''
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

# Podemos encontrar um valor numa lista
numero = 5
if numero in lista1:
    print(f'numero {numero} encontrado')
else:
    print(f'numero {numero} não encontrado')

# Podemos ordenar uma lista
lista1.sort()
print(lista1)
lista5.sort()
print(lista5) # Sort só funciona em lista de mesmo tipo de variáveis
# Podemos contar o número de caracteres de uma lista
print(lista1.count(2    ))
# Adicionar elementos
print(lista1)
lista1.append(42)
print(lista1)
# Obs: com append só se adiciona um elemento por vez, porém um elemento do tipo lista é possível
print(lista1)
lista1.append([5, 6, 99]) # Coloca a lista como elemento único
print(lista1)
# Podemos inclusive verificar o elemento lista dentro da lista através do if, pois se torna um caracter único
lista1.extend([22, 55, 66]) # .extend adiciona item por item, diferente do append que coloca a lista como elemento único
print(lista1)
# Podemos inserir um elemento informando a posição dentro da lista
lista1.insert(2, 'novo valor')
print(lista1) # isso não substitui valores, só os desloca de posição
# Podemos juntar duas listas
lista6 = lista1 + lista2
# também pode lista1.extend(lista2) vc terá o mesmo resultado da soma
print(lista6)
# Podemos facilmente inverter uma lista utilizando o reverse
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)
# também podemos utilizar o slice para inverter
# print(lista1[::-1]) teremos o mesmo resultado
# Copiar uma lista
lista6 = lista2.copy()
print(lista6)
# Podemos utilizar o len para saber o tamanho de uma lista
print(lista2.__len__()) # Irá te retornar o tamanho da lista, como em strings
# Podemos remover o último elemento de uma lista
print(lista5)
lista5.pop()
print(lista5)  # O .pop não somente remove o último elemento, mas também o retorna se vc o imprimir
# Podemos remover um elemento pelo índice
print(lista5)
lista5.pop(2)
print(lista5)  # Os elemento a direita são deslocados para esquerda
# se não houver elemento na posição informada teremos o 'index erro'
# podemos também remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)
# Podemos também concatenar listas como em strings através de operações matemáticas
listanova = [1, 2, 3]
print(listanova*3)
# Podemos transformar uma string numa lista com .split
texto = 'meu nome é marcelo'
print(texto.split())
# o .split utiliza o espaço para definir uma palavra, mas podemos também utilizar outros elementos com ','
texto = 'meu, ,nome,é,marcelo'
texto = texto.split(',')
print(texto)
# Posso também transformar uma lista em string
print(texto)
string = ' '.join(texto) # O espaço entre aspas simples aqui ' ' serve para que seja adicionado espaços entre cada elemento
print(string)
# Outro exemplo de .join usando $ em vez de espaço. posso colocar o que eu quiser
print(texto)
string = '$'.join(texto)
print(string)
# Posso colocar qualquer tipo de dado numa lista
lista7 = [1, True, 'Geek', [1, 2, 3]]
# Iterando sobre listas
# Exemplo 1
soma = 0
for elemento in lista4: # é preciso analisar o tipo de dado da lista para somar
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 (utilizando while) Principalmente para criar listas

produto = ' '
carrinho = []

while produto != 'sair':
    print('Adicione um produto no carrinho ou digite "sair" para sair: ')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
print('Segue abaixo lista de produtos: ')
for produto in carrinho:
    print(produto)

# Podemos criar uma lista de variáveis
print('')
num1 = 1
num2 = 2
num3 = 3
num4 = 4
listanum = [num1, num2, num3, num4]
print(listanum)

print('')
# Podemos acessar os elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[2])

print('')
# Para o inverso podemos imaginar que as posições negativas são anteriores ao zero. ex:
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])
print(cores[-2])


cores = ['verde', 'amarelo', 'azul', 'branco']
for cor in cores:
    print(cor)
    
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Enumerate
print('')
cores = ['verde', 'amarelo', 'azul', 'branco']
# Gerar índice em um for
for indice, cor in enumerate(cores): # enumerate gera pares, chave e valor - o for está colocando chave em indice e valor em cor
    print(indice, cor)
    

print('')
# Listas aceitam número repetidos
lista8 = []
lista8.append(42)
lista8.append(42)
lista8.append(42)
lista8.append(42)
print(lista8)

print('')
# Encontar o índice de um elemento na lista
numeroslista = [5, 9, 8, 6, 9, 8]
# Em qual índice da lista está o valor 9?
print(numeroslista.index(9)) #lembrando que retorna o índice começando de zero
# Obs:  caso o elemento não exista na lista será retornado um erro ValueError
# Podemos fazer a busca dentro de um range
print(numeroslista.index(9, 2)) # o 9 é o elemento buscado e o 2 o índice a partir do qual queremos
print(numeroslista.index(9, 2, 6)) # o 9 é o elemento buscado e o 2 a 6 o intervalo que queremos

print('')
# Revisão de Slicing

# lista[inicio:fim:passo]
# range(inicio:fim:passo)

lista9 = [1, 2, 3, 4]
print(lista9[1:4:2]) # começou no indice 1, foi até o quarto indice e pulou de 2 em 2

print('')
# Invertendo valores em uma lista
nomes = ['geek', 'university']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes = ['geek', 'university']
nomes.reverse() # Forma mais Pythonica de fazer isso
print(nomes)

print('')
# Soma, valor máximo, valor mínimo e tamanho da lista (Se os valores forem todos inteiros ou reais)
lista = [1, 2, 3, 4, 5, 6, 7]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

print('')
# Transformar lista em Tupla
lista = [1, 2, 3, 4, 5, 6, 7]
print(lista)
print(type(lista))

lista = tuple(lista)
print(lista)
print(type(lista))

print('')
# Desempacotamento de lista
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num3)
print(num2)
print(num1)
# Dessa forma eu adiciono cada item da lista numa variável que eu determino
# Não posso ter nem mais nem menos variáveis que elementos na lista para desempacotar. ValueError

# Copiando uma lista para outra (Shallow copy e Deep Copy)

# Forma Deep Copy
lista = [1, 2, 3]
print(lista)
nova = lista.copy()
print(nova)
nova.append(55)
print(lista)
print(nova)
# Obs: As duas listas são independentes

# Forma Shallow Copy
lista = [1, 2, 3]
print(lista)
nova = lista
print(nova)
nova.append(55)
print(lista)
print(nova)
# Veja que agora a modificação ocorreu nas duas lista, pois foram copiadas por atribuição
'''




