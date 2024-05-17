"""Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se
o usuário venceu ou perdeu."""
from random import randint
from time import sleep

print(f'\033[33;1m{"-=" * 30}')
print(f'\033[34;1m{"Vou pensar em um número entre 0 e 5. Tente adivinhar!".center(60)}')
print(f'\033[33;1m{"-=" * 30}')

numeroPensado = randint(0, 5)

numeroChutado = int(input('\033[38;1mEm que número eu pensei? '))

print('\033[35mPROCESSANDO...')
sleep(3)

if numeroChutado == numeroPensado:
    print('\033[32;1mPARABÉNS! Você conseguiu me vencer!')
else:
    print(f'\033[31;GANHEI! Pensei no número {numeroPensado} e não no {numeroChutado}!')
