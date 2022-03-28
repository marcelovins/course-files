"""
Funções com Parâmetro de entrada
- Funções que recebem dados para serem processados dentro da mesma;
Se a gente pensar em um programa qualqauer, gerlamente temos:
entrda -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;
"""

# Refatorando uma função

def quadrado (numero):  #Essa função recebe um parâmetro; é obrigatório informar um parãmetro
    return numero ** 2

print(quadrado(2))
print(quadrado(5))
print(quadrado(7))
# print(quadrado()) Type error por não informar o parâmetro


def cantar_parabens(aniversariante):
    print(f'\n\nParabéns pra vc nesta data querida, muitas felicidades! Vivá {aniversariante}!')


cantar_parabens('Marcelo')


# Funções podem ter n parâmetros de entrada. OU seja, podemos receber como entrada em uma função
# quantros parâmetros forem necessários. Eles são separados por vírgula.


def soma(a, b):
    return a + b


def multiplica(n1, n2):
    return n1 * n2


def outra(n1, b, msg):
    return (n1 + b) * msg


print(soma(2, 5))

print(multiplica(4, 5))

print(outra(2, 3, 'geek'))
# Teremos um TypeError se não informarmos a quantidade exata de parâmetros de nossa função


def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'


print(nome_completo('Marcelo', 'Vinícius'))


# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;


print(nome_completo(nome='Marcelo', sobrenome='Vinz'))

print(nome_completo(sobrenome='Vini', nome='Marcel'))


def soma_impares(numeros):
    total = 0
    for num in numeros:    # Objetos inteiros não são iteráveis. Bom guardar esse conceito!
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
teste = 1, 2
print(soma_impares(lista))
print(soma_impares(teste))


