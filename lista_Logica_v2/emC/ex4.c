#include <stdio.h>

void main() {
    float alt, maior, menor;
    int i;
    
    for (i = 1; i <= 15; i++) {
        printf("Digite a altura da pessoa %d: ", i);
        scanf("%f", &alt);
        
        if (i == 1) { // Definindo o primeiro valor como referência
            maior = alt;
            menor = alt;
        }
        
        if (alt > maior) {
            maior = alt;
        }
        
        if (alt < menor) {
            menor = alt;
        }
    }
    
    printf("Maior altura: %f | Menor altura: %f\n", maior, menor);
}