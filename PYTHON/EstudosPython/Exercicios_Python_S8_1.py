'''
def dobro_inteiro(num1):
    num1 = num1 * 2
    return num1


num = int(input(f'Digite o numero:'))
print(f'\nO dobro do número {num} é: {dobro_inteiro(num)}')
'''


def data_extenso():
    ano = int(input(f'\nDigite o ano: '))
    mes = input(f'\nDigite o mês com dois dígitos: ')
    dia = int(input(f'\nDigite o dia: '))
    print('\n')
    meses = {'01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril', '05': 'maio', '06': 'junho', '07': 'julho', '08': 'agosto', '09': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}
    mes_extenso = meses.get(mes)
    return print(f'{dia} de {mes_extenso} de {ano}')


print(data_extenso())


