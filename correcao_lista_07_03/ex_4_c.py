import os

sem = {"Dom": 0, "Seg":0, "Ter": 0, "Qua":0, "Qui":0, "Sex": 0, "Sab":0}

list_semanas = [dict(sem), dic(sem), dict(sem)] #O uso da função dict é muito importante para criar uma nova cópia independente de sem

for ind, semana in enumerate(list_semanas): #rodo 3 vezes, 1 p/ cada semana
    for dia in semana: #rodo 7 vezes, 1 p/ cada dia da semana
        semana[dia] = float(input(f"Digite o valor de {dia} da semana {ind}: ")) 

os.system('clear')

for indice, select_sem in enumerate(list_semanas):
    select_sem["media"]= sum(select_sem.values())/len(select_sem)
    for dia in select_sem:
        if (select_sem[dia] <  select_sem["media"]):
          print(f" Temperatura {select_sem[dia]} de {dia}, Semana {indice}, menor que a média {select_sem['media']}"); 