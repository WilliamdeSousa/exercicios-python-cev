"""Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

distanciaEmKm = float(input('Informe a distânica da sua viagem: (km) '))
valorCobrado = distanciaEmKm * (.5 if distanciaEmKm <= 200 else .45)

print(f'O total a ser pago por esta viagem é R${valorCobrado:.2f}!')
