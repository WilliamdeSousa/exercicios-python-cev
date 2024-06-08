"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo
de 1 até 500."""
quantidadeNumeros = 0
somaNumeros = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 == 1:
        quantidadeNumeros += 1
        somaNumeros += i
print(f'A soma de todos os {quantidadeNumeros} valores solicitados é {somaNumeros}')
