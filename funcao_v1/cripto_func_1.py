def cript(valor, chave):
    return valor+chave

def decript(valor, chave):
    return valor-chave

vlr = input("Digite os números que deseja separados por ponto e vírgula (;)")
lista = vlr.split(";")
chave = int(input("Digite a chave: "))
op = input("Digite C para Criptografar e D para Descriptografar:")


if(op.upper() == 'C'):
    for i in range(0, len(lista)):
        lista[i] = cript(int(lista[i]), chave)
elif (op.upper() == 'D'):
    for i in range(0, len(lista)):
        lista[i] = decript(int(lista[i]), chave)
else:
    print("Operação não identificada")

for i in lista:
    print(i, end="; ")
print('')