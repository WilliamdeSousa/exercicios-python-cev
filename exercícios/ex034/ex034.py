"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%."""

salario = float(input("Qual o seu salário? R$"))

if salario > 1250:
    percentual = 10
else:
    percentual = 15
novoSalario = salario * (1 + percentual / 100)

print(f'O novo salário é de R${novoSalario:.2f}, um aumento de {percentual}%!')
