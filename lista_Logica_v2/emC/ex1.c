#include <stdio.h>

void main(){
    int i, vlr;
    int soma = 0;
    for(i=1; i <=7; i++){
        printf("Digite um número: ");
        scanf("%d", &vlr);
        if (vlr < 0){
            soma = soma + 1;
        }
    }
    printf("Entre os 7 valores, %d são números negativos \n", soma);
}