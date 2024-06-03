"""Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep

print('Suas opções: ')
print('[ 1 ] Pedra')
print('[ 2 ] Papel')
print('[ 3 ] Tesoura')

escolhaJogador = int(input('Escolha sua jogada: '))

if escolhaJogador == 1:
    escolhaJogador = 'Pedra'
elif escolhaJogador == 2:
    escolhaJogador = 'Papel'
else:
    escolhaJogador = 'Tesoura'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')

escolhaComputador = randint(1, 3)

if escolhaComputador == 1:
    escolhaComputador = 'Pedra'
elif escolhaComputador == 2:
    escolhaComputador = 'Papel'
else:
    escolhaComputador = 'Tesoura'

print('=' * 30)
print(f'O computador joga {escolhaComputador}')
print(f'O jogador joga {escolhaJogador}')
print('=' * 30)

if escolhaComputador == 'Pedra':
    if escolhaJogador == 'Pedra':
        print('EMPATE')
    elif escolhaJogador == 'Papel':
        print('O JOGADOR VENCE!')
    elif escolhaJogador == 'Tesoura':
        print('O COMPUTADOR VENCE!')

if escolhaComputador == 'Papel':
    if escolhaJogador == 'Papel':
        print('EMPATE')
    elif escolhaJogador == 'Tesoura':
        print('O JOGADOR VENCE!')
    elif escolhaJogador == 'Pedra':
        print('O COMPUTADOR VENCE!')

if escolhaComputador == 'Tesoura':
    if escolhaJogador == 'Tesoura':
        print('EMPATE')
    elif escolhaJogador == 'Pedra':
        print('O JOGADOR VENCE!')
    elif escolhaJogador == 'Papel':
        print('O COMPUTADOR VENCE!')
