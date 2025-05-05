#include <stdio.h>

void main() {
    int i;
    
    for (i = 100; i <= 200; i++) {
        if (i % 2 == 1) {
            printf("%d e impar!\n", i);
        }
    }
}