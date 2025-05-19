#include <stdio.h>

void main(){
    float temp[] =  {27, 30, 27.6, 23.5, 29.3, 24, 21};
    float media = 0;
    int i;

    for (i = 0; i<7; i++) {
        media = media + temp[i];
    }
    media = media / i;

    for (i = 0; i<7; i++) {
        if (temp[i] < media){
            switch (i) {
                case 0:
                    printf("Temperatura de Segunda-Feira abaixo da média: %.2f:", temp[i]);
                    break;
                case 1:    
                    printf("Temperatura de Terça-Feira abaixo da média: %.2f:", temp[i]);
                    break;
                case 2:  
                    printf("Temperatura de Quarta-Feira abaixo da média: %.2f:", temp[i]);
                    break;
                case 3:  
                    printf("Temperatura de Quinta-Feira abaixo da média: %.2f:\n", temp[i]);
                    break;
                case 4:  
                    printf("Temperatura de Sexta-Feira abaixo da média: %.2f:\n", temp[i]);
                    break;
                case 5:
                    printf("Temperatura de Sábado abaixo da média: %.2f:\n", temp[i]);
                    break;
                case 6:    
                    printf("Temperatura de Domingo abaixo da média: %.2f:\n", temp[i]);
                    break;
                default:
                    printf("Algo errado!\n");
            }
    }
}
}