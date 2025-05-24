vet = []

for i in range(0, 5):
    resp = int(input(f"Digite o número {i+1}: "))
    vet.append(resp)

for i in range(0, 4):
    j=0
    while (j < 4-i):
        if(vet[j] > vet[j+1]):
            troca = vet[j+1]
            vet[j+1] = vet[j]
            vet[j] = troca
        j+=1

print(vet)
