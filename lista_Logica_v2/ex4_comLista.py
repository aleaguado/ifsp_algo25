# 4) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar :
#	a) A menor altura do grupo;
#	b) A maior altura do grupo; 
lista = []
for i in range(1,16):
    lista.append(float(input(f"Digite a altura da pessoa {i}: ")))
print(f"Maior altura: {max(lista)} | Menor altura: {min(lista)}")