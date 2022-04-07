from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python'

print(dicionario)

print(dicionario['outro'])  # diferente do dicionario comum, não gera KeyError e adiciona um novo elemento

print(dicionario)


