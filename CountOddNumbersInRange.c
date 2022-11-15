#include <stdio.h>
#include <stdlib.h>

int main(){
    int low = 8;
    int high = 10;
    
    int N = (high - low)/2;

    if(((low % 2) != 0) || ((high % 2 ) != 0)){
        N += 1;
    }
    printf("%d", N);
}