# 3) Escreva um algoritmo que leia n valores numéricos (quantos o usuário quiser digitar) e encontre o maior, o menor deles e a média aritmética. Mostre o resultado.

continua = 1
lista = []
while (continua != 0):
    lista.append(float(input("Digite um número: ")))
    continua = int(input("Digite 0 para sair ou 1 para continuar: "))

print(f"Maior número: {max(lista)} | Menor número: {min(lista)} | Média: {(sum(lista) / len(lista)):.2f}")