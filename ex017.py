co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1 / 2)
print(f'A hipotenusa vai medir {hip:.2f}')
