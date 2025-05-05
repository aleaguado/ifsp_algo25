# 2) A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:  
    # a) média do salário da população;
    # b) média do número de filhos;
    # c) maior salário;
    # d) percentual de pessoas com salário até R$1000,00.
# Faça um software que permita a coleta desses dados e ao final, imprima na tela as informações desejadas.

sal = 0
SomaSal = 0
maiorSal = 0.0
filhos = 0
continua = 1
cont = 0
ateMil = 0
while (continua != 0):
    sal = float(input(f"Digite o salario da família {cont + 1}: "))
    filhos += int(input(f"Digite quantos filhos/as tem a família {cont + 1}: "))
    if (sal > maiorSal):
        maiorSal = sal
    if (sal <= 1000.00):
        ateMil = ateMil+1
    SomaSal += sal
    cont += 1
    continua = int(input("Digite 0 para sair ou 1 para continuar: "))

print(f"A média do salário da população é {(SomaSal / cont):.2f}")
print(f"A média do número de filhos é {(filhos / cont):.2f}")
print(f"O maior salário é {maiorSal:.2f}")
print(f"O percentual de pessoas com salário até R$ 1000,00 é de {((ateMil*100) / cont):.2f} %")