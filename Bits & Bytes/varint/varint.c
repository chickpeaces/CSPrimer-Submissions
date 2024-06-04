#include <stdio.h>
#include <stdint.h>

/* VARINT encoded expected output */
#define C_ONE_ENC 0x1
#define C_150_ENC 0x9601
#define C_256_ENC 0x8002
#define C_MAX_ENC 0xffffffffffffffffff01ull
/* VARINT decoded expected output*/
#define C_ONE_DEC 1
#define C_150_DEC 150
#define C_256_DEC 256
#define C_MAX_DEC 18446744073709551615ull

uint64_t encode( uint64_t n ){
    uint64_t p=0, out=0;
    while(n){
        p= n & 0x7f;
        n>>= 7;
        p|= n ? 0x80 : 0x00;
        out= (out<< 8) | p;
    }

    return out;
}

uint64_t decode( uint64_t n){
    uint64_t out=0;
    while(n){
        out<<= 7;
        out|= n & 0x7f;
        n>>= 8;
    }
    return out;
}

int main( int argc, char** argv){

    printf("\n%llx\n", encode( C_MAX_DEC));
    printf("\n%llu\n", decode( C_MAX_ENC));

    char fail= 0;
    // for(uint64_t i= 0; i< C_MAX_DEC; i++){
    //     if( !(decode( encode(i)) == i)){
    //         printf( "enc/dec failed at %llu", i);
    //         fail=1;
    //         break;
    //     }
    // }
    if( !fail)
        printf("OK");

}