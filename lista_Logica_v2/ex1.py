# 1) Escreva um algoritmo que receba 7 valores numéricos e retorne na tela a mensagem:
#	“Entre os 7 valores, X são números negativos!”.
soma = 0
for i in range(1, 8):
    vlr = int(input("Digite um número: "))
    if (vlr < 0):
        soma += 1
print(f"Entre os 7 valores, {soma} são números negativos.")
