# Criação da Função de Troca
def troca(lista, a, b):
    tr = lista[b]
    lista[b] = lista[a]
    lista[a] = tr
    return lista

# Criação de ordenação
def sort(lista):
    for i in range(0, len(lista)-1):
        j=0
        while (j < (len(lista)-1)-i):
            if(lista[j] > lista[j+1]):
                lista = troca(lista, j, j+1)
            j+=1
    return lista
#Execução principal do meu código
vet = []

for i in range(0, 5):
    resp = int(input(f"Digite o número {i+1}: "))
    vet.append(resp)

vet = sort(vet)

print(vet)