"""
Recebendo dados do usuário
"""
# Entrada de Dados

#Exemplo Python 2.x antigo

# forma antiga de recebimento de dados
# print("Qual é o seu nome?")
# nome = input() # input é o scanf
# print("E sua idade?")
# idade = input()

# Nova forma de recebimento de dados

nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))

# Exemplo de print Python 3.x até 3.6

print("Seja bem vindo(a) {0}".format(nome))

# Exemplo de print Python 3.7

print(f"Seja bem vindo(a) {nome}")

# int(idade) => Cast
# Cast é a conversão de um tipo de dado para outro
# Todo dado recebido via input() é uma string
'''
Em Python tudo que está entre aspas simples, duplas ou triplas(simples e duplas) é uma string
'''
# print(f'{nome} nasceu em {2022 - int(idade)}')
"""
Também posso usar o Cast já no momento no input, conforme exemplo abaixo
idade = int(input('Qual sua idade?'))
"""
print(f'{nome} nasceu no ano {2022-idade}')

# Processamento

# Saída
# Antigo formato
print("Seja bem vindo(a) %s, %s tem %s anos" % (nome, nome, idade))
"""se existe mais de uma variável é necessário
colocar entre parenteses as variáveis"""
# Novo formato
print(f'{nome} tem {idade} anos!')
