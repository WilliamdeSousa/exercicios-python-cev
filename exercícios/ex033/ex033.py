"""Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))

maior = menor = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
