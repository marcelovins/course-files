idade = 21

if idade < 18:
    print('é menor de 18\n')
elif idade == 18:
    print('É de maior\n')
elif idade <= 30:
    print('É menor de 30 anos\n')
else:
    print('Não está dentro da idade permitida\n')

ativo = False
logado = False
if not ativo:  # O if somente checa se uma variável é verdadeira(True), senão, irá direto para else.
    print('Você precisa logar sua conta\n') # No nosso caso, if not, está nos dando a condição False, contrário!
else:
    print('Bem vindo, usuário!\n')

print(ativo is True)  # is é binário, nos retorna como uma pergunta. Ativo é True? a resposta é False
# A linguagem Python é de alto nível, porque ela se aproxima da linguagem humana (inglês)
# Ela também é de typagem dinâmica, porque não preciso dizer qual o tipo da variável
nome = 'marcelo'
print(nome.isupper())

'''#geralmente estas funções com is retornam algo True ou False, neste caso retorna se nome
#está em maiúsculo'''
