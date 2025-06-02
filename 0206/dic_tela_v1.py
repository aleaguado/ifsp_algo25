nomes = []
entrada = ''
while entrada.upper() != 'S':
    entrada = input("Digite um nome: ")
    if entrada.upper() != 'S':
        nomes.append(entrada)

for nome in nomes:
    print(nome)
