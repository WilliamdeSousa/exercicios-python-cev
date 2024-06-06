"""Exercício Python 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
print('Os números pares entre 1 e 50 são: ')
for i in range(2, 51, 2):
    match i:
        case 50:
            end = '.'
        case 48:
            end = ' e '
        case _:
            end = ', '
    print(i, end=end)

