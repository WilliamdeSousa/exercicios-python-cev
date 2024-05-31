"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo
 será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if (m := max(l1, l2, l3)) < l1 + l2 + l3 - m:
    print('Os lados informados podem formar um triângulo!')

    # ex042
    if l1 == l2 == l3:
        print('O triângulo formado será equilátero!')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('O triângulo formado setá isósceles!')
    else:
        print('O triângulo formado será escaleno!')
else:
    print('Os lados informados não podem formar um triẫngulo!')
