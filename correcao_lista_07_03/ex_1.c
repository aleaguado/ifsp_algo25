#include <stdio.h>

void main(){
    float temp[] =  {27, 30, 27.6, 23.5, 29.3, 24, 21};
    float maior, menor;
    int i;

    for (i = 0; i<7; i++) {
        if ((i==0) || (temp[i] < menor)){
            menor = temp[i];
        }
        if ((i==0) || (temp[i] > maior)){
            maior = temp[i];
        }
    }
    printf("A menor temperatura identificada foi %.2f e a maior temperatura foi %.2f. \n", menor, maior);
}