"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

primeiroValor = int(input('Primeiro valor: '))
segundoValor = int(input('Segundo valor: '))

if primeiroValor > segundoValor:
    print('O primeiro valor é maior')
elif segundoValor > primeiroValor:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')