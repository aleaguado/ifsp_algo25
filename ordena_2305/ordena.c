#include <stdio.h>

void main(){
    int vet[5];
    int i, j, troca;

    for(i=0;i<5;i++){ //Alimenta o vetor vet!
        printf("Digite o número %d: ", i+1);
        scanf("%d", &vet[i]);
    }

    for(i=0; i<4; i++){ //Ordena!
        for(j=0; j<4-i; j++){
            if(vet[j] > vet[j+1]) {
                troca = vet[j+1];
                vet[j+1] = vet[j];
                vet[j] = troca;
            }
        }
    }

    for(i=0;i<5;i++){ //Alimenta o vetor vet!
        printf("\nPosição %d: %d ",i+1, vet[i]);
    }
}