# 4) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar :
#	a) A menor altura do grupo;
#	b) A maior altura do grupo; 

for i in range(1,16):
    alt = float(input(f"Digite a altura da pessoa {i}: "))
    if (i == 1): # Para colocar o primeiro valor como maior e menor, ou seja, o referencial inicial
        maior = alt
        menor = alt    
    if (alt > maior):
        maior = alt
    if (alt < menor):
        menor = alt
print(f"Maior altura: {maior} | Menor altura: {menor}")