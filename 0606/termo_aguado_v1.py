import random
import os
letras_descartadas = []
lista_fixa = ['EURECA', 'MADRINHA', 'TRICOLOR', 'HACKER', 'VIDA']

def escolhe(): #Função que retorna a palavra escolhida
    i = random.randint(0,(len(lista_fixa)))
    return lista_fixa[i]

os.system("clear")
#Parte 1 - Escolher a palavra, dar uma mensagem de boas vindas para o usuário, imprimir mascara da palavra
palavra = escolhe()
print(" ################################")
print("Bem-Vindo/a ao Termo - Aguado!")
print(" ################################")
print("Instruções")
print("A cada tentativa você verá em minúsculo as letras que existem na palavra mas estão fora do lugar, enquanto as letras na posição correta estarão maíusculas!")
print(" ################################\n\n")
print("Sua Palavra:\n\n")
provisoria = []
for i in palavra:
    print("_", end=' ')
    provisoria.append('_')
print('')

#Parte 2 - Por 6 tentativas
for tent in range(1,7):
    #a) Pedir para o usuário digitar uma palavra com a quantidade de caracteres
    resp = ''
    while len(resp) != len(palavra):
        resp = input(f"\nTentativa {tent} - Digite uma palavra de {len(palavra)} caracteres: ")
    
    #b) Para cada letra ver se ela está na palavra e na posição correta OU está na palavra na posição errada
    ## ou não está na palavra
    for i, letra in enumerate(resp.upper()): #vou executar as tarefas abaixo p/ cada letra!
        if letra == palavra[i]: # a letra está na posição correta? 
            provisoria[i] = letra.upper() #se sim, adicionamos a lista provisoria!
        elif letra in palavra: #a letra existe na palavra?
            if (letra not in provisoria) and (provisoria[i].isupper()  == False): #e a letra ainda não está representada na provisoria nem já está marcada maiscula?
                provisoria[i] = letra.lower() #colocamos ela na provisoria minuscula pq posicao está errada
        else: #a letra não existe na palavra?
            if letra not in letras_descartadas: #e ainda não colocamos nas letras descartadas? 
                letras_descartadas.append(letra) #adicionamos nas letras descartadas
    #c) Verificar se acertou a palavra completa
    if(provisoria == list(palavra)): #se o usuário acertou a palavra
        break #interrompemos as tentativas
    #d) Não acertou ainda, então imprimimos a palavra provisória e as letras descartadas
    print("Palavra: ", end='')
    for i in provisoria:
        print(i, end=' ')
    print("\nLetras descartadas: ", end='')
    for i in letras_descartadas:
        print(i, end=' ')

if tent == 7:
    print(f"Não foi dessa vez! A palavra é {palavra}")
else:
    print(f"Parabéns! A palavra é {palavra}")
