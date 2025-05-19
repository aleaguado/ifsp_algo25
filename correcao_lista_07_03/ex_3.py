temp = []
media = [0]*3

clear

temp.append([0] * 7)
temp.append([0] * 7)
temp.append([0] * 7)

for li in range(0,3):
    for co in range(0,7):
        temp[li][co] = float(input(f"Digite o valor do dia {co} da semana {li}:  "))

for li in range(0,3):
    media[li] = sum(temp[li]) / len(temp[li])
    for co in range(0,7):
        if (temp[li][co] < media[li]):
          print(f" Temperatura do dia {co} - Semana {li}, {temp[li][co]}, menor que a média {media[li]}"); 