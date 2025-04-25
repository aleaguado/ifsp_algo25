from datetime import datetime #Importando as funções datetime da bibliooteca datetime
# Sócio do Clube Delta OU ela tiver mais de 60 = 10,00
# Sócio do Clube Delta + Aniversariante daquele dia =  5,00
# Compra > 100,00
hoje = datetime.today()
socio = 0
maior = 0
aniv = 0
seguir = 1

while seguir == 1:
    valor = float(input("Digite o valor da compra: "))
    dt_nasc = input("Digite sua data de nascimento no formato dd/mm/aaaa: ") # Aqui dt_nasc é uma STRING!
    dt_nasc = datetime.strptime(dt_nasc, "%d/%m/%Y")    # Aqui dt_nasc passa a ser um objeto do tipo DATA!
    idade = hoje.year - dt_nasc.year #calcula a idade a partir da subtração dos anos
    if((dt_nasc.day, dt_nasc.month) > (hoje.day, hoje.month)): #Se a pessoa ainda não fez aniversário esse ano eu desconto 1 ano
        idade = idade -1
    socio = int(input("Digite 1 se você for socio do Clube Delta ou 0 se não: "))

    if(valor < 100):
        valor = valor
    elif ((socio == 1) and ((hoje.day, hoje.month) == (dt_nasc.day, dt_nasc.month))):
        valor = valor - 15.00
    elif ((socio == 1) and ((hoje.day, hoje.month) != (dt_nasc.day, dt_nasc.month))) or (idade >= 60):
        valor = valor - 10.00  
    else:
        valor = valor   

    print(f"Valor total da compra: R$ {valor}")
    seguir = int(input("Digite 1 para continuar ou 0 para sair: "))
print("Obrigado! Supermercado Delta agradece!")