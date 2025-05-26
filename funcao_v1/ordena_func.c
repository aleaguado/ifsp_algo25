#include <stdio.h>

void troca(int* v, int a, int b){
    int tr;
    tr = v[b];
    v[b] = v[a];
    v[a] = tr;
}

void main() {
    int i, j;
    int vet[5];

    for (i=0; i<5;i++){
        printf("Digite o número %d: ", i+1);
        scanf("%d", &vet[i]);
    }

    for(i=0;i<4;i++){
        for(j=0;j<4-i;j++){
            if(vet[j] > vet[j+1]){
                troca(vet, j, j+1);
            }
        }
    }

    for (i=0; i<5;i++){
        printf("Posição %d: %d \n", i+1, vet[i]);
    }
}
