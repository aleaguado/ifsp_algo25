#include <stdio.h>

void main(){
    float temp[3][7];
    int li, co;

    for(li = 0; li <3; li++){
        for(co = 0; co < 7; co++){
            printf("Digite o valor do dia %d da semana %d: ", (co+1), (li+1));
            scanf("%f", &temp[li][co]);    
        }
    }

    for(li = 0; li <3; li++){
        for(co = 0; co < 7; co++){
            printf(" Temperatura do dia %d - Semana %d : %.2f\n", (co+1), (li+1), temp[li][co]); 
        }
    }
}