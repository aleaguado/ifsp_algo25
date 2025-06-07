# Em Python, crie uma lista que contenha todas as letras do alfabeto, de forma ordenada. Ao final, percorra a lista com um laço de repetição, imprimindo as letras;
alfabeto = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u', 'v','w','x','y','z']

def criptografa(pl, key):
    cripto = []
    for letra in pl:
        i = alfabeto.index(letra)
        i = i+key #Ao invés de somar 1, somo a chave
        i = i%26
        cripto.append(alfabeto[i])
    return cripto

def descripto(pl, key):
    cripto = []
    for letra in pl:
        i = alfabeto.index(letra)
        i = i-key #Ao invés de somar, vou subtrair
        while (i < 0): #Enquanto for negativo
            i = i+26
        cripto.append(alfabeto[i])
    return cripto

#Pedir usuario uma palavra
palavra = input("Digite uma palavra: ")
chave = int(input("Digite a chave criptografica: ")) #Pergunte a chave p/ usuario
op = input("Digite C para criptografar ou D para descriptografar: ")

match(op.upper()):
    case 'C':
        lista = criptografa(palavra, chave)
    case 'D':
        lista = descripto(palavra, chave)       
    case _:
        print("Operação Inválida")
        exit()

print(lista)