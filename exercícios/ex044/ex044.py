"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

valorProduto = float(input('Valor a ser pago: R$'))

print('OPÇÕES DE PAGAMENTO:')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] cartão de crédito')

opcaoPagamento = int(input('Escolha a forma de pagamento: '))

if opcaoPagamento == 1:
    print(f'O total é de R${valorProduto * 0.9:.2f}, com 10% de desconto!')
else:
    divididoNoCartao = int(input('Quantas prestações no cartão? '))

    if divididoNoCartao == 1:
        print(f'O total a ser pago será de R${valorProduto * 0.95:.2f}, com 5% de desconto!')
    elif divididoNoCartao == 2:
        print(f'O total a ser pago será de R${valorProduto:.2f}, o valor formal do produto!')
        print(f'Será pago em 2x de R${valorProduto / 2:.2f}!')
    else:
        print(f'O total a ser pago será de R${(totalASerPago := valorProduto * 1.2):.2f}, 20% de juros!')
        print(f'Será pago em {divididoNoCartao}x de R${totalASerPago / divididoNoCartao:.2f}!')
