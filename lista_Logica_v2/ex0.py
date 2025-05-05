# 0) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.
soma = 0
for i in range (1, 501):
    if (i%2 == 1) and (i%3 == 0):
        soma += i
print(f"A soma dos ímpares multiplos de 3 é {soma}")