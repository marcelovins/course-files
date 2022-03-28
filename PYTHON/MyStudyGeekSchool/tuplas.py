# Tuplas (tuple)

'''
Tuplas são parecidas com listas, diferem basicamente em dois pontos:
1 - Tuplas são representadas por parênteses ()
2 - Tuplas são imutáveis - Toda operação em uma tupla gera uma nova tupla

OBs:
1-  Quando não colocamos parênteses o python logo entende os dados separados por vírgula como sendo uma tupla também
2- Quano existe apenas um elemento entre parênteses o python não considera como tupla, apenas com mais de 2.
sendo assim, podemos entender que tuplas são definidas pelas vírgulas e não por parênteses. Pois, um elemento
com vírgula (4,) já seria considerado uma tupla, diferente de (4) que seria um int
(4) -> não é tupla
(4,) -> é uma tupla
4, -> é uma tupla

# Podemos gerar uma tupla dinâmica com range
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Aceita todas as mesmas manipulações que a lista (list)
tupla = 'geek university','Programação em Python'
escola, curso = tupla
print(escola)
print(curso)

# Métodos de adição e remoção em tuplas não existem, pois são imutáveis. um .append não muda a tupla

# Aceita todas as mesmas manipulações que a lista (list)
tupla = 'geek university','Programação em Python'
escola, curso = tupla
print(escola)
print(curso)

# Aceita todas as mesmas manipulações que a lista (list)
tupla = 1, 2, 3
for n in tupla:
    print(n)
'''


# Tuplas são usadas quando não queremos modificar os dados em uma coleção!!

meses = 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'
print(meses[5])
print(meses[1:5])
print(meses[:5])

# Tuplas são mais rápidas que listas
# Tuplas deixam seu código mais seguro por não permitirem mudanças
# Tuplas não têm o problema de Shallow copy
