"""Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
não formar um triângulo."""
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))


# 3 5 6
if (m := max(l1, l2, l3)) < l1 + l2 + l3 - m:
    print('Os lados informados podem formar um triângulo!')
else:
    print('Os lados informados não podem formar um triẫngulo!')
