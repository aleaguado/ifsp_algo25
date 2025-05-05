#include <stdio.h>

void main() {
    int num, i;
    
    printf("Digite um numero: ");
    scanf("%d", &num);
    
    printf("===== TABUADA DO %d =====\n", num);
    
    for (i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", num, i, num*i);
    }
}