# 5) Escrever um algoritmo que gera e escreve os números ímpares entre 100 e 200.

#Método sem lista
print("Solucionando sem lista")
for i in range(100, 201):
    if (i % 2) == 1:
        print(f"{i} é impar!")

print("Solucionando com lista")
lista = []
for i in range(100, 201):
    if (i % 2) == 1:
        lista.append(i)
print(f"Lista de números ímpares entre 100 e 200: {lista}")