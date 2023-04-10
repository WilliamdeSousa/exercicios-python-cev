nome = input('Digite seu nome completo: ')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
nome = nome.split()
print(f'Seu nome tem ao todo {len("".join(nome))}')
nome = nome[0]
print(f'Seu primeiro nome é {nome} e ele tem {nome.__len__()} letras')