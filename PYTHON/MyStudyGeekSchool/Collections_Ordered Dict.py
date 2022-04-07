from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items():
    print(f'chave = {chave}: valor = {valor}')

from passlib.hash import pbkdf2_sha256 as cryp

