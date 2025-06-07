# Em Python, crie uma lista que contenha todas as letras do alfabeto, de forma ordenada. Ao final, percorra a lista com um laço de repetição, imprimindo as letras;
alfabeto = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u', 'v','w','x','y','z']

#Como resolver o problema de estouro das letras?
# Imagine as posições de alfabeto como uma contagem infinita, circular, onde a posiçãoo 0 também é a posição 26
# e também a posição 52 ... e assim por diante.
# A partir disso, SE sempre que o index for maior que 25 eu subtrair dele 26, chegarei na posição que quero!
# Ainda assim, teremos um problema quando a chave for maior que 51! Aí precisamos subtrair 26 por 2 vezes!
# Ou seja ... ENQUANTO o indice desejado for maior que 25, eu preciso subtrair 26 dele, afinal, o
# indice 0, 26, 52, refere-se a mesma casa!!! Vamos implementar!

def troca(pl, key): #Adicionando um parametro pra receber a chave
    cripto = []
    for letra in pl:
        i = alfabeto.index(letra)
        i = i+key #Ao invés de somar 1, somo a chave
        #while (i > 25): #Resolvendo o problema do estouro!
        #    i = i-26
        i = i%26
        cripto.append(alfabeto[i])
    return cripto


#Pedir usuario uma palavra
palavra = input("Digite uma palavra: ")
chave = int(input("Digite a chave criptografica: ")) #Pergunte a chave p/ usuario

lista = troca(palavra, chave) #Adicione a chave na passagem de parâmetro

print(lista)