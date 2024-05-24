#include <stdio.h>
#include <stdint.h>
#include <assert.h>

char count_bits( uint32_t n);
char fast_count_bits( uint32_t n);

int main( int argc, char** argv){

    assert(count_bits(0) == 0);
    assert(count_bits(1) == 1);
    assert(count_bits(3) == 2);
    assert(count_bits(8) == 1);
    // harder case:
    assert(count_bits(0xffffffff) == 32);

    printf("OK\n");

    return 0;
}

char count_bits( uint32_t n){
    char bit_n=0;

    for( char i= 32;i> 0; --i){
         bit_n+= (n & 0x1);
         n>>= 1;
    }

    return bit_n;
}

char fast_count_bits( uint32_t n){
    char bit_n=0;

    while(n){
        n&= (n-1);
        bit_n++;
    }

    return bit_n;
}