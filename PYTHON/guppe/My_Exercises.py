"""
Exercises_Marcelo

# Exercise 01  -- @property

class Contributors:

    def __init__(self, name, value, hour_work):
        self.__name = name
        self.__value = value
        self.__hour_work = hour_work

    def deposit(self):
        return f'The collaborator will receive {self.__value * self.__hour_work} pounds this month'

    def hour_worked(self):
        return f'The collaborator has worked {self.__hour_work} hours per day'

    def named(self):
        return f'{self.__name} is our collaborator'

    def annual_wage(self, month):
        return f"The annual payment is {self.__hour_work * self.__value * month} pounds "

    @property
    def name(self):
        return self.__name

    @property
    def hour_work(self):
        return self.__hour_work

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, newvalue):
        self.__value = newvalue


colab_01 = Contributors('Marcelo', 20, 30)
colab_02 = Contributors('Pamela', 20, 30)

print(colab_01.named())
print(colab_01.hour_worked())
print(colab_01.deposit())
print(colab_01.annual_wage(12))
print(f'My collaborators cost to me {colab_02.value + colab_01.value} per hour')
colab_01.value = 50
print(f'My collaborators cost to me {colab_02.value + colab_01.value} per hour')


# Exercise 02 -- All and Any

# Remembering all() and any()

print(all(num for num in [0, 1, 2, 3, 4, 5] if num % 2 == 0))  # Return a boolean
print(any(num for num in [0, 1, 2, 3, 4, 5] if num % 2 == 0))  # Return a boolean
print(list(num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0))  # Result when a created a list


# Exercise 03  -- *args

def congrats(*args):
    if 'Marcelo' in args:
        return "Congrats! You're Right!"
    return "You're wrong. Try again!"


phrase = 'Marcelo'

print(congrats(phrase))
print(congrats('Marcelo', True, 123, 'Geek'))
print(congrats('Julia', True, 123, 'Geek'))

# print(dir(phrase))

def verifica_info(*args):
    if 'Geek' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem você é ...'


print(verifica_info('geek'))
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

# Exercise 04 -- atributos

class Product:
    # Class Attribute
    counter = 0
    list_promotion = []

    # Instance Attribute

    def __init__(self, price, weight, name):
        self.__price = price
        self.__weight = weight
        self.__name = name
        self.__id = Product.counter + 1
        Product.counter = self.__id

    @property
    def price(self):
        return self.__price

    @property
    def weight(self):
        return self.__weight

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    def weight_separator(self):
        if self.__weight > 1000:
            return f'{self.__name} is heavier than allowed'
        return f'Product allowed'

    def promotion_price(self):
        if self.__price < 1000:
            Product.list_promotion = self.__name
        return Product.list_promotion


store_data1 = Product(1500, 255, 'iphone x')
store_data2 = Product(800, 1200, 'Playstation')

print(store_data1.weight_separator())
print(store_data1.promotion_price())
print('')
print(store_data2.weight_separator())
print(store_data2.promotion_price())
print('')
print(store_data1.__dict__)
print(store_data2.__dict__)


# Exercise 05 -- **kwargs


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é ...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)
"""


# Exercise 06 -- dictionary comprehension

value = [55, 45, 32, 40, 25]
name = ['marcelo', 'julia', 'tiago', 'carlos', 'tiao']

res = {name[i]: value[i] for i in range(0, len(name))}

print(res)

# Exercise 06 -- list comprehension

res = [num + 1 for num in [1, 2, 4, 6, 7]]
print(res)


