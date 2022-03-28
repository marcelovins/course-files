'''
Definindo Funções
-  Funções são pequenos trechos de código que realizam tarefas específicas;
já utilizamos funções, como print, mas agora iremos criar nossas próprias funções
- Pode ou não retornar e receber dados

Obs: Procure escrever funções simples
'''
'''
# Exemplo de utilização

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programação em Python'

print(curso) # as funções em python recebem dados específicos, se eu tentasse colocar um append em algo que não é lista
teria um erro '''

'''
Em PYthon, a forma geral de definir uma função é:

def nome_da_função(parametros_de_entrada):
    bloco_da_função
    
Onde:

nome_da_função -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case)
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece. 
Neste bloco, pode ter ou não retorno da função.

Obs: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo 
uma função. Também abrimos o bloco de código com o já conhecido dois pontos: (usado para definir bloco em PYthon)

'''

# Definindo a primeira função

def diz_oi():
    print('\n\noi!')

# Utilizando uma função

diz_oi()

for n in range(5):
    diz_oi()
