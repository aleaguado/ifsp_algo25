// 0) Desenvolver um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de três e que se encontram no conjunto dos números de 1 até 500.
#include <stdio.h>

void main(){
    int i;
    int soma = 0;
    for(i=1; i <=500; i++){
        if (((i%2) == 1) && ((i%3) == 0)){
            soma = soma + i;
        }
    }
    printf("A soma dos ímpares multiplos de 3 é %d \n", soma);
}