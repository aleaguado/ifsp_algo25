#include <stdio.h>

void main() {
    int continua = 1;
    int cont = 0;
    float soma = 0;
    float num, maior, menor;
    
    while (continua != 0) {
        printf("Digite um numero: ");
        scanf("%f", &num);
        
        if (cont == 0) { // Para colocar o primeiro valor como maior e menor
            maior = num;
            menor = num;
        }
        
        if (num > maior) {
            maior = num;
        }
        
        if (num < menor) {
            menor = num;
        }
        
        soma = soma + num;
        cont = cont + 1;
        
        printf("Digite 0 para sair ou 1 para continuar: ");
        scanf("%d", &continua);
    }
    printf("Maior numero: %f | Menor numero: %f | Media: %f\n", maior, menor, (soma/cont));
}