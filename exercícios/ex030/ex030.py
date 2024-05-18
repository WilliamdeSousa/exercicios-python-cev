"""Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""
roxo = "\033[35m"
azul = "\033[34m"
branco = "\033[38m"

numero = int(input(f'{roxo}Informe um número qualquer: '))
print(f'{branco}Este número é {azul}{"ÍMPAR" if numero % 2 == 1 else "PAR"}')
