"""Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import  datetime

anoAtual = datetime.today().year

menorDeIdade = 0

for i in range(7):
    idade = anoAtual - int(input(f'Ano de Nascimento da {i + 1}ª pessoa: '))

    if idade < 18:
        menorDeIdade += 1

maiorDeIdade = 7 - menorDeIdade

print(f'No ano de {anoAtual}, {menorDeIdade} pessoas são menores de idade e {maiorDeIdade} são maiores de idade!')