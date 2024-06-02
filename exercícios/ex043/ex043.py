"""Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida"""

peso = float(input('Peso: (Kg) '))
altura = float(input('Altura: (m) '))

imc = peso / (altura ** 2)

print(f'Seu IMC é de {imc:.2f}!')

if peso < 18.5:
    print('Você está na faixa de peso Abaixo do Peso')
elif peso < 25:
    print('Parabéns! Você está na faixa de peso Peso Ideal')
elif peso < 30:
    print('Você está na faixa de peso Sobrepeso')
elif peso < 40:
    print('Você está na faixa de peso Obesidade')
else:
    print('Você está na faixa de peso Obesidade Mórbida')
