# 3) Escreva um algoritmo que leia n valores numéricos (quantos o usuário quiser digitar) e encontre o maior, o menor deles e a média aritmética. Mostre o resultado.

continua = 1
cont = 0
soma = 0
while (continua != 0):
    num = float(input("Digite um número: "))
    if (cont == 0): # Para colocar o primeiro valor como maior e menor, ou seja, o referencial inicial
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1
    continua = int(input("Digite 0 para sair ou 1 para continuar: "))

print(f"Maior número: {maior} | Menor número: {menor} | Média: {(soma / cont):.2f}")