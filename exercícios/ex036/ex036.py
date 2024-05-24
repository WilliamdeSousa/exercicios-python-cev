"""Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
salário ou então o empréstimo será negado."""
valorCasa = float(input('Qual o valor da casa? '))
salarioComprador = float(input('Qual seu salário do comprador? '))
anosParaPagar = int(input('Por quantos anos deseja pagar a casa? '))
prestacaoMensal = valorCasa / (anosParaPagar * 12)
print(f'A prestação fica R$ {prestacaoMensal:.2f}!')
if prestacaoMensal <= 0.3 * salarioComprador:
    print(f'Parabéns! O empréstimo foi aprovado!')
else:
    print(f'A prestação representa {prestacaoMensal / salarioComprador * 100:.1f}% do seu salário. Empréstimo negado!')
