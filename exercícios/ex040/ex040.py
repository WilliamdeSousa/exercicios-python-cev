"""Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

primeiraNota = float(input('Primeira nota: '))
segundaNota = float(input('Segunda nota: '))

media = (primeiraNota + segundaNota) / 2

print(f'Sua média é {media:.1f}')
if media < 5:
    print('Você está reprovado!')
elif media < 7:
    print('Você está em recuperação!')
else:
    print('Parabéns! Você está aprovado!')
