"""Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA
MARATONA."""

frase = str(input('Digite uma frase: '))

frase = ''.join(frase.upper().strip().split())

if frase == frase[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')