"""Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

divisivel = '\033[32;1m'
naoDivisivel = '\033[31;1m'
padrao = '\033[m'

numero = int(input('Digite um número: '))

numerosDivisiveis = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        print(divisivel, end='')
        numerosDivisiveis += 1
    else:
        print(naoDivisivel, end='')
    print(f'{i} ', end='')
print(padrao)
print(f'O número {numero} foi divisível {numerosDivisiveis} vezes')
print(f'E por isso ele {"" if numerosDivisiveis == 2 else "NÃO "}É PRIMO!')
