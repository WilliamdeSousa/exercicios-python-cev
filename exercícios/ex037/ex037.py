"""Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."""
numero = int(input('Informe um número inteiro: '))

print(f"""OPÇÕES DE CONVERSÃO:
[ 1 ] PARA BINÁRIO
[ 2 ] PARA OCTAL
[ 3 ] PARA HEXADECIMAL""")

opcao = int(input('Selecione a opção: '))

match opcao:
    case 1:
        print(f'O decimal {numero} em binário é {bin(numero)}')
    case 2:
        print(f'O decimal {numero} em octal é {oct(numero)}')
    case 3:
        print(f'O decimal {numero} em hexadecimal é {hex(numero)}')
    case _:
        print(f'Opção inválida!')
