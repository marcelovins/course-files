tuplas=("tiago", "marcelo", "amanda")#cria uma tupla que diferente duma lista nao pode ser mudada
print (tuplas)
print (tuplas[0])#função para verificar uma posição na tupla
print (tuplas[1])
print (tuplas[2])
print (tuplas[0:2])#função para verificar um intervalo na tupla
print (tuplas[0:1])
print (tuplas[0:3])
print (len(tuplas))#função para contar as tuplas, como em string (str)
print (tuplas+tuplas)#função para concatenar tuplas
print (tuplas*3)#função para concatenar por multiplicação
print (4 in tuplas)#função para verificar um item na tupla e retornar false ou true
print ('amanda' in tuplas)
lista=[1,4,'tiago']#cria lista
print (lista)
tuplas2=tuple(lista)#função para transformar lista em tuplas
print (tuplas2)#no print é possível verificar(idle) que os colchetes mudam para parênteses
#é importante lembrar que listas nada mais são que vetores em c++
