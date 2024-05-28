"""Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
 alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import datetime

anoAtual = datetime.today().year

anoNascimento = int(input('Em que ano você nasceu? '))

idade = anoAtual - anoNascimento
anoAlistamento =  anoNascimento + 18

print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {anoAlistamento}!')
elif idade > 18:
    print(f'O alistamento já passou! Deveria ser em {anoAlistamento}.')
else:
    print(f'Está no ano do seu alistamento. Corra para se alistar!')
