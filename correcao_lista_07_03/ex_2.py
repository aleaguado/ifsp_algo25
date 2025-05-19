
temp = [27, 30, 27.6, 23.5, 29.3, 24, 21];
media = sum(temp) / len(temp)

for i, valor in enumerate(temp):
    if valor < media:
        match(i):
            case 0:
                print(f"Temperatura de segunda abaixo da média: {valor}:") 
            case 1:
                print(f"Temperatura de terça abaixo da média: {valor}:") 
            case 2:
                print(f"Temperatura de quarta abaixo da média: {valor}:") 
            case 3:
                print(f"Temperatura de quinta abaixo da média: {valor}:") 
            case 4:
                print(f"Temperatura de sexta abaixo da média: {valor}:") 
            case 5:
                print(f"Temperatura de sábado abaixo da média: {valor}:") 
            case 6:
                print(f"Temperatura de domingo abaixo da média: {valor}:") 
            case _:
                print("Algo errado aí!")                                                                            