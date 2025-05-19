import os
dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
list_semanas = []

for semana in range(0, 3): #rodo 3 vezes, 1 p/ cada semana
    dic_vazio = {} #crio um dicionário vazio
    list_semanas.append(dic_vazio) #adiciono na minha lista de semanas um dicionário vazio
    for dia in range(0,7): #rodo 7 vezes, 1 p/ cada dia da semana
        list_semanas[semana][dias[dia]] = float(input(f"Digite o valor de {dias[dia]} da semana {semana}: ")) 

os.system('clear')

for indice, select_sem in enumerate(list_semanas):
    select_sem["media"]= sum(select_sem.values())/len(select_sem)
    for dia in select_sem:
        if (select_sem[dia] <  select_sem["media"]):
          print(f" Temperatura {select_sem[dia]} de {dia}, Semana {indice}, menor que a média {select_sem['media']}"); 