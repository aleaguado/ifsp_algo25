def troca(lista, a, b):
    tr = lista[b]
    lista[b] = lista[a]
    lista[a] = tr

vet = []

for i in range(0, 5):
    resp = int(input(f"Digite o número {i+1}: "))
    vet.append(resp)

for i in range(0, 4):
    j=0
    while (j < 4-i):
        if(vet[j] > vet[j+1]):
            troca(vet, j, j+1)
        j+=1

print(vet)