# 6) Faça um programa que mostre a tabuada de qualquer número escolhido pelo usuário (considerar tabuada do número 1 ao 10).

num = int(input("Digite um número"))
print(f"===== TABUADO DO {num} =====")
for i in range(1, 11):
    print(f"{num} x {i} = {(num*i)}")
