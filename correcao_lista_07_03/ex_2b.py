
temp = {"segunda":27, "terça": 30 , "quarta": 27.6, "quinta":23.5, "sexta": 29.3, "sabado": 24, "domingo": 21};

media = sum(temp.values()) / len(temp)

for dia, valor in temp.items():
    if(valor < media):
        print(f"Menor que média: {dia} : {valor}")
