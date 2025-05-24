vet = []

for i in range(0, 5):
    resp = int(input(f"Digite o número {i+1}: "))
    vet.append(resp)

vet.sort()

print(vet)