#include <stdio.h>

void main() {
    float sal = 0;
    float somaSal = 0;
    float maiorSal = 0.0;
    int filhos = 0;
    int continua = 1;
    int cont = 0;
    int ateMil = 0;
    int filhos_familia;

    while (continua != 0) {
        printf("Digite o salario da familia %d: ", cont + 1);
        scanf("%f", &sal);
        
        printf("Digite quantos filhos/as tem a familia %d: ", cont + 1);

        scanf("%d", &filhos_familia);
        filhos += filhos_familia;
        
        if (sal > maiorSal) {
            maiorSal = sal;
        }
        
        if (sal <= 1000.00) {
            ateMil = ateMil + 1;
        }
        
        somaSal += sal;
        cont += 1;
        
        printf("Digite 0 para sair ou 1 para continuar: ");
        scanf("%d", &continua);
    }
    
    printf("A media do salario da populacao e %.2f\n", (somaSal / cont));
    printf("A media do numero de filhos e %.2f\n", ((float)filhos / cont));
    printf("O maior salario e %.2f\n", maiorSal);
    printf("O percentual de pessoas com salario ate R$ 1000,00 e de %.2f %%\n", ((ateMil * 100.0) / cont));

}