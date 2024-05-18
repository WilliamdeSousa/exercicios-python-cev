"""Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
roxo = '\033[35;1m'

velocidade = float(input("Informe sua velocidade: (km/h) "))

if velocidade < 80:
    print(f'{azul}Parabéns por dirigir com responsabilidade! Tenha um bom dia!')
else:
    multa = 7 * (velocidade - 80)

    print(f'{vermelho}Parado! A velocidade máxima desta via é de 80km/h')
    print(f'Você excedeu a velocidade máxima permetida em {velocidade - 80}km/h')
    print(f'Por isso você terar que pagar uma multa de {verde}R${multa:.2f}')
    print(f'{roxo}Dirija com responsabilidade!')
