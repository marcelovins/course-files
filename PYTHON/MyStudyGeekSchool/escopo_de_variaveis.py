'''
Escopo de Variáveis

Dois casos de escopo:

1- Variáveis globais;
Variáveis reconhecida em todo o programa

2- Variáveis locais;
São reconhecidas apenas no bloco onde foram declaradas
'''
numero = 8
print(numero) #Exemplo de variável global, é a mesma em todo o programa

if numero>10:   #Aqui a variável novo é um exemplo de variável local, que só faz parte de uma parte do programa
    novo=numero+10 #Se numero for menor que 10, novo(local) nunca será criada, porém, numero(global) pode ser chamada
    print(novo)