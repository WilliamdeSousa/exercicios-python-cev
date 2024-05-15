"""Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
último nome separadamente.

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza."""
nome = str(input('Olá, qual o seu nome completo? ')).title().split()
primeiroNome, ultimoNome = nome[0], nome[-1]
print(f'Seja bem vindo, seu primeiro nome é {primeiroNome} e seu último nome é {ultimoNome}!')
