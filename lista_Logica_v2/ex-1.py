# -1) Faça um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 emita uma mensagem: “Múltiplo de 10”.


i = 1
while i <= 100:
    print(f"{i}")
    if ((i%10) == 0):
        print("Múltiplo de 10!")
    i=i+1